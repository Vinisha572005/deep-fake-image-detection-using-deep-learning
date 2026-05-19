import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
from PIL import ImageFile

# Fix image loading issues
ImageFile.LOAD_TRUNCATED_IMAGES = True

# ======================
# PATH CHECK
# ======================
train_dir = "train"
test_dir = "test"

if not os.path.exists(train_dir):
    print("❌ train folder not found!")
    exit()

if not os.path.exists(test_dir):
    print("❌ test folder not found!")
    exit()

# ======================
# DATA PREPROCESSING
# ======================
train_datagen = ImageDataGenerator(
    rescale=1./255,
    horizontal_flip=True,
    zoom_range=0.2,
    rotation_range=20,
    shear_range=0.2
)

test_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_dir,
    target_size=(128,128),
    batch_size=32,
    class_mode='binary'
)

test_data = test_datagen.flow_from_directory(
    test_dir,
    target_size=(128,128),
    batch_size=32,
    class_mode='binary'
)

print("\n🔍 Class Labels:", train_data.class_indices)

if len(train_data.class_indices) < 2:
    print("❌ Need at least TWO classes (real & fake)")
    exit()

# ======================
# BASE MODEL
# ======================
base_model = MobileNetV2(
    input_shape=(128,128,3),
    include_top=False,
    weights='imagenet'
)

# Fine-tuning setup
base_model.trainable = True

for layer in base_model.layers[:-20]:
    layer.trainable = False

# ======================
# CUSTOM MODEL
# ======================
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.BatchNormalization(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(1, activation='sigmoid')
])

# ======================
# SUMMARY
# ======================
print("\n📊 Model Summary:")
model.summary()

# ======================
# COMPILE
# ======================
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# ======================
# CALLBACKS
# ======================
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

# ======================
# TRAIN
# ======================
print("\n🚀 Training started...\n")

history = model.fit(
    train_data,
    epochs=20,
    validation_data=test_data,
    callbacks=[early_stop]
)

# ======================
# SAVE MODEL
# ======================
model.save("deepfake_model_final.keras")

print("\n✅ Training completed successfully!")

# ======================
# PLOT RESULTS
# ======================
plt.figure()
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'])
plt.show()

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'])
plt.show()