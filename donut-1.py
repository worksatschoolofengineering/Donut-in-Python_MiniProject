import time

# create a list of donut shapes
shapes = [
    " O ",
    "---"
]

# create a spinning animation
while True:
    for shape in shapes:
        # print each shape on a new line
        print(shape)
        time.sleep(0.1)

