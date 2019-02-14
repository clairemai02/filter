import filters

def main():
    filename = input("Enter an image file to edit: ")
    im = filters.load_img(filename)
    filters.save_img(im, "picture.jpeg")
    filters.show_img(im)
    new_img = filters.obamicon(im)
    filters.show_img(new_img)
main()
