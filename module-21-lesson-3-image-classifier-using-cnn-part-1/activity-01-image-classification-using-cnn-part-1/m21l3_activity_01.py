# M21 Lesson 3 - Activity 1: Image Classification using CNN - Part 1
# (data preprocessing + baseline model, CIFAR-10)
# Adapted to run in VS Code: the Colab "!wget" / "!tar" lines are replaced by Python code that
# downloads and unpacks the dataset into a "cifar10" folder next to this script (about 160 MB,
# downloaded once). Needs: pip install tensorflow pillow matplotlib --break-system-packages
import os
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

for i in range(9):
    plt.subplot(330 + 1 + i)
    plt.imshow(x_train[i])
plt.show()

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
model.summary()
