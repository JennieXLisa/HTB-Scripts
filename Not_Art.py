from __future__ import print_function
from PIL import Image

# Setup variables
filename = "not_art.png"

# Convert pixel to string value
def pix2str(pixel):
    str = ""
    for x in pixel:
        if x == 0:
            str += '0'
        elif x == 192:
            str += '1'
        elif x == 255:
            str += '2'
    return str

# Create array of converted pixels
def getArray(image):
    arr = []
    width, height = image.size
    rgb = image.convert("RGB")
    for y in range(0, width, 10):
        arr.append([])
        for x in range(0, height, 10):
            pixel = rgb.getpixel((x,y))
            cpix = pix2str(pixel)
            arr[y / 10].append(cpix)
    return arr

# Show 2D array
def showArray(arr, justSize = 5):
    for j in range(len(arr)):
        for i in range(len(arr[j])):
            print(str(arr[j][i]).rjust(justSize, " "), end="")
        print("")

# Conversion base3 to base10
def changeBase(num):
    val = 0
    snum = str(num)[::-1]
    for i in range(len(snum)):
        digit = int(snum[i])
        val += digit * (3**i)
    return val

# Get char from number (already ROT13)
def num2text(num):
    dict = "NOPQRSTUVWXYZABCDEFGHIJKLM"
    return dict[num]

# Main function
def main():
    image = Image.open(filename)
    values = getArray(image)
    for j in range(len(values)):
        for i in range(len(values[j])):
            values[j][i] = changeBase(values[j][i])
            values[j][i] = num2text(values[j][i] - 1)
    showArray(values, 1)

if __name__ == '__main__':
    main()
