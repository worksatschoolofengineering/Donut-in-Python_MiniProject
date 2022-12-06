# Import the math and time modules
import math
import time

# Create two variables to control the animation
angle_1 = 0
angle_2 = 0

# Clear the screen
print("\x1b[2J", end='')

# Loop indefinitely to create the animation
while True:
    # Create a list of zeros to store the depth values for each pixel
    depths = [0] * 1760

    # Create a list of empty strings to store the characters for each pixel
    pixels = [' '] * 1760

    # Loop over the angles
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            # Calculate some trigonometric values
            sin_i = math.sin(i)
            cos_j = math.cos(j)
            sin_a = math.sin(angle_1)
            sin_j = math.sin(j)
            cos_a = math.cos(angle_1)
            d = cos_j + 2
            depth = 1 / (sin_i * d * sin_a + sin_j * cos_a + 5)
            cos_i = math.cos(i)
            cos_b = math.cos(angle_2)
            sin_b = math.sin(angle_2)
            t = sin_i * d * cos_a - sin_j * sin_a
            x = int(40 + 30 * depth * (cos_i * d * cos_b - t * sin_b))
            y = int(12 + 15 * depth * (cos_i * d * sin_b + t * cos_b))
            o = int(x + 80 * y)
            n = int(8 * ((sin_j * sin_a - sin_i * cos_j * cos_a) * cos_b - sin_i * cos_j * sin_a - sin_j * cos_a - cos_i * cos_j * sin_b))
            # Only draw the pixel if it is in bounds and has a greater depth than the current pixel at that position
            if 22 > y and y > 0 and x > 0 and 80 > x and depth > depths[o]:
                depths[o] = depth
                pixels[o] = ".,-~:;=!*#$@"[n if n > 0 else 0]