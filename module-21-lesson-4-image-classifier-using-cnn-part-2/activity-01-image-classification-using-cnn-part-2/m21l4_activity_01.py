# M21 Lesson 4 - Activity 1: Image Classification using CNN - Part 2
# (train, evaluate and use the CIFAR-10 model)
# The lesson continues the Part 1 notebook; in VS Code this script repeats the Part 1
# steps (load data, preprocess, build the model) so it runs on its own.
# The CIFAR-10 data is downloaded once into a "cifar10" folder next to this script.
# Training takes a while (10 epochs); a GPU is not required but is faster.
# Needs: pip install tensorflow pillow matplotlib --break-system-packages
# Usage:  python3 m21l4_activity_01.py [path/to/your_image.jpg]
import os
import sys
import tarfile
import urllib.request

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy import argmax
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Dense, Flatten, Dropout, Conv2D, MaxPooling2D
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.utils import to_categorical, load_img, img_to_array
from tensorflow.keras.optimizers import SGD

here = os.path.dirname(os.path.abspath(__file__))


# Step 2: download the dataset (skipped if the cifar10 folder already exists)
DATA_URL = 'https://s3.amazonaws.com/fast-ai-imageclas/cifar10.tgz'
data_dir = os.path.join(here, 'cifar10')
if not os.path.isdir(data_dir):
    archive = os.path.join(here, 'cifar10.tgz')
    print('Downloading CIFAR-10 (this can take a few minutes)...')
    urllib.request.urlretrieve(DATA_URL, archive)
    with tarfile.open(archive, 'r:gz') as tar:
        tar.extractall(here)
    os.remove(archive)

# Step 3: load the images into arrays
def load_split(folder):
    class_names = sorted(os.listdir(folder))
    images, labels = [], []
    for label, class_name in enumerate(class_names):
        class_dir = os.path.join(folder, class_name)
        for filename in os.listdir(class_dir):
            img = Image.open(os.path.join(class_dir, filename)).convert('RGB')
            images.append(np.array(img))
            labels.append(label)
    x = np.array(images)
    y = np.array(labels).reshape(-1, 1)
    # images are loaded one class folder at a time, so shuffle them together
    shuffle_order = np.random.permutation(len(x))
    return x[shuffle_order], y[shuffle_order], class_names

x_train, y_train, class_names = load_split(os.path.join(data_dir, 'train'))
x_test, y_test, _ = load_split(os.path.join(data_dir, 'test'))

print(class_names)

# Step 4: preprocess the dataset
num_classes = len(class_names)

train_size = 8000
test_size = 2000
x_train = x_train[:train_size]
y_train = y_train[:train_size]
x_test = x_test[:test_size]
y_test = y_test[:test_size]

y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Step 5: build the baseline model
model = Sequential()
model.add(Input(shape=(32, 32, 3)))
model.add(Conv2D(16, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu', kernel_constraint=max_norm(3)))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

opt = SGD(learning_rate=0.01, momentum=0.9, nesterov=False)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Step 6: train the model
model.fit(x_train, y_train, batch_size=32, epochs=10, verbose=1, validation_data=(x_test, y_test))
print('The model has successfully trained')

model_path = os.path.join(here, 'classifier.keras')
model.save(model_path)
print('Saving the model as classifier.keras')

# Step 7: evaluate the model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Step 8: choose a new image to classify (replaces the Colab file upload)
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('Path to an image to classify (e.g. dog.jpg): ').strip().strip('"\'')

# Step 9: predict what is in the image
def load_image(filename):
    img = load_img(filename, target_size=(32, 32))
    img = img_to_array(img)
    img = img.astype('float32') / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def run_example():
    img = load_image(filename)
    loaded_model = load_model(model_path)
    result = loaded_model.predict(img)
    predicted_index = argmax(result[0])
    print('Predicted class:', class_names[predicted_index].title())

if os.path.isfile(filename):
    run_example()
else:
    print('Image not found:', filename)
