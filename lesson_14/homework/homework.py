#task1
import numpy as np

# Function
def fahrenheit_to_celsius(F):
    return (F - 32) * 5 / 9

# Vectorized function
vec_f_to_c = np.vectorize(fahrenheit_to_celsius)

# Input array
temps_f = np.array([32, 68, 100, 212, 77])

# Apply conversion
temps_c = vec_f_to_c(temps_f)

print("Celsius:", temps_c)
#task2
# Function
def power_func(x, p):
    return x ** p

# Vectorized version
vec_power = np.vectorize(power_func)

# Input arrays
numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

# Apply function
result = vec_power(numbers, powers)

print("Power result:", result)
#task3
A = np.array([
    [4, 5, 6],
    [3, -1, 1],
    [2, 1, -2]
])

b = np.array([7, 4, 5])

solution = np.linalg.solve(A, b)

print("x, y, z =", solution)
#task4
A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])

b = np.array([12, -5, 15])

currents = np.linalg.solve(A, b)

print("I1, I2, I3 =", currents)
#bonus
from PIL import Image
import numpy as np
def flip_image(img_array):
    flipped_lr = np.fliplr(img_array)
    flipped_ud = np.flipud(img_array)
    return flipped_lr, flipped_ud
def add_noise(img_array, noise_level=30):
    noise = np.random.randint(-noise_level, noise_level, img_array.shape)
    noisy_img = img_array + noise
    return np.clip(noisy_img, 0, 255).astype(np.uint8)
def brighten_red_channel(img_array, value=40):
    img_array = img_array.copy()
    img_array[:, :, 0] = np.clip(img_array[:, :, 0] + value, 0, 255)
    return img_array
def apply_mask(img_array, mask_size=100):
    h, w, _ = img_array.shape
    start_x = w // 2 - mask_size // 2
    start_y = h // 2 - mask_size // 2

    img_array[start_y:start_y+mask_size, start_x:start_x+mask_size] = [0, 0, 0]
    return img_array
# Load image
image = Image.open("images/birds.jpg")
img_array = np.array(image)

# Flip image
flip_lr, flip_ud = flip_image(img_array)

# Add noise
noisy_img = add_noise(img_array)

# Brighten red channel
bright_img = brighten_red_channel(img_array)

# Apply mask
masked_img = apply_mask(img_array.copy())

# Save outputs
Image.fromarray(flip_lr).save("birds_flipped_lr.jpg")
Image.fromarray(flip_ud).save("birds_flipped_ud.jpg")
Image.fromarray(noisy_img).save("birds_noisy.jpg")
Image.fromarray(bright_img).save("birds_bright_red.jpg")
Image.fromarray(masked_img).save("birds_masked.jpg")
