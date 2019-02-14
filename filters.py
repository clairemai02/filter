from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(image):
    return Image.open(image)


# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(object):
    object.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(object, filename):
    object.save(filename, "jpeg")


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    pixel = image.getdata()
    new = []
    for i in range(len(pixel)):
        # pixelvalue = pixel[i]
        red = pixel[i][0]
        green = pixel[i][1]
        blue = pixel[i][2]
        if red + green + blue < 182:
            new.append((0, 51, 76))
        if red + green + blue <= 182 and red + green + blue > 364:
            new.append((217, 26, 33))
            # new[i] =
        if 364 <= red + green + blue >= 546:
            new.append((112, 150, 158))
            # new[i] =
        if red + green + blue > 546:
            new.append((252, 227, 166))
            # new[i] = (252, 227, 166)
    newpic = Image.new("RGB", image.size)
    return newpic.putdata(new)
        #sum rgb values --> based on the sum change the color
