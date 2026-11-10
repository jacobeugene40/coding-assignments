# M21 Lesson 6 - Activity 1: Digit Recognition using CNN - Part 2
# (train, evaluate and use the MNIST digit model)
# The lesson continues the Part 1 notebook; in VS Code this script repeats the Part 1 steps
# (load data, preprocess, build the model) so it runs on its own.
# MNIST downloads automatically the first time you run it (needs internet).
# Needs: pip install tensorflow matplotlib --break-system-packages
# Usage:  python3 m21l6_activity_01.py [path/to/digit_image.png]
import os
import sys
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.utils import to_categorical, load_img, img_to_array
from tensorflow.keras.optimizers import SGD
from numpy import argmax
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath(__file__))

# Step 2: load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print('Train Dataset (x):', x_train.shape)
print('Train Dataset (y):', y_train.shape)
print('Test Dataset (x):', x_test.shape)
print('Test Dataset (y):', y_test.shape)

# Step 3: preprocess the dataset
# The full MNIST set has 60,000 training images. That's more than a CPU needs to learn
# digits well, so this keeps a smaller slice to train faster. Raise these numbers if you
# have a GPU and more time.
train_size = 8000
test_size = 2000
x_train = x_train[:train_size]
y_train = y_train[:train_size]
x_test = x_test[:test_size]
y_test = y_test[:test_size]

x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
input_shape = (28, 28, 1)

num_classes = 10
y_train = to_categorical(y_train, num_classes)
y_test = to_categorical(y_test, num_classes)

x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# Step 4: build the baseline model
batch_size = 128
epochs = 10

model = Sequential()
model.add(Input(shape=input_shape))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

opt = SGD(learning_rate=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Step 5: train the model
model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test))
print('The model has successfully trained')

model_path = os.path.join(here, 'mnist.keras')
model.save(model_path)
print('Saving the model as mnist.keras')

# Step 6: evaluate the model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

# Step 7: choose a new digit image (replaces the Colab file upload)
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = input('Path to an image of a digit (e.g. digit.png): ').strip().strip('"\'')

# Step 8: predict the digit
def load_image(filename):
    img = load_img(filename, color_mode='grayscale', target_size=(28, 28))
    img = img_to_array(img)
    if img.mean() > 127:      # dark digit on light paper -> flip to white on black like MNIST
        img = 255 - img
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32') / 255.0
    return img

def run_example():
    img = load_image(filename)
    loaded_model = load_model(model_path)
    predict_value = loaded_model.predict(img)
    digit = argmax(predict_value)
    print('Predicted digit:', digit)

if os.path.isfile(filename):
    run_example()
else:
    print('Image not found:', filename)
