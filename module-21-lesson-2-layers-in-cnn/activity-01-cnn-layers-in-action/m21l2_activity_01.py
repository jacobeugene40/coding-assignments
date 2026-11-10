# M21 Lesson 2 - Activity 1: CNN Layers in Action (convolution, pooling, Keras)
# Needs: pip install tensorflow matplotlib numpy --break-system-packages
import numpy as np
import matplotlib.pyplot as plt

# Step 2: a small image and a filter
image = np.array([
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0],
])

kernel = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1],
])

print(image)

# Step 3: slide the filter to get a feature map
def convolve(image, kernel):
    k = kernel.shape[0]
    out_size = image.shape[0] - k + 1
    result = np.zeros((out_size, out_size))
    for i in range(out_size):
        for j in range(out_size):
            patch = image[i:i+k, j:j+k]
            result[i, j] = np.sum(patch * kernel)
    return result

feature_map = convolve(image, kernel)
print(feature_map)

# Step 4: shrink it with max pooling
def max_pool(feature_map, size=2):
    out_size = feature_map.shape[0] // size
    result = np.zeros((out_size, out_size))
    for i in range(out_size):
        for j in range(out_size):
            window = feature_map[i*size:(i+1)*size, j*size:(j+1)*size]
            result[i, j] = np.max(window)
    return result

pooled = max_pool(feature_map, size=2)
print(pooled)

# Step 5: flatten the pooled map
flattened = pooled.flatten()
print(flattened)

# Step 6: the same layers in Keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential()
model.add(Input(shape=(6, 6, 1)))
model.add(Conv2D(4, kernel_size=(3, 3), activation='relu'))
print('after Conv2D:', model.output_shape)

# Step 7: pooling, flattening and a dense layer
model.add(MaxPooling2D(pool_size=(2, 2)))
print('after MaxPooling2D:', model.output_shape)

model.add(Flatten())
print('after Flatten:', model.output_shape)

model.add(Dense(10, activation='softmax'))
print('after Dense:', model.output_shape)

# Step 8: visualize every stage
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].imshow(image, cmap='gray')
axes[0].set_title('Original Image (6x6)')

axes[1].imshow(feature_map, cmap='gray')
axes[1].set_title('After Convolution (4x4)')

axes[2].imshow(pooled, cmap='gray')
axes[2].set_title('After Max Pooling (2x2)')

plt.show()
