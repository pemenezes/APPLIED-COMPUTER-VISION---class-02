# this program needs to convert an colored image in a scale of gray

import cv2

'''
ABOVE, WE ARE IMPORTING THE LIBRARY OPENCV, WICH WILL HELP US IN THE IMAGE MANIPULATION 
'''

import matplotlib.pyplot as plt

'''
LIBRARY TO DISPLAY GRAPHICAL ELEMENTS
'''

#===== FUNCTION BLOCK TO MANIPULATE THE IMAGES =====#
'''
1st step: define the image that will be uploaded
'''

def load_image(path):

    image = cv2.imread(path) #reading the image

    if image is None:
        raise ValueError("Image not found")
    else:
        return image

'''
2nd step: define a function that will convert the image in a scale of gray
'''

def convert_gray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''
3rd step: define the function of the histogram
'''

def histograma(image):
    plt.hist(image.ravel(), bins=256, range= [0, 256])
    plt.title("Intensity histogram")
    plt.xlabel("Intensity")
    plt.ylabel("pixels quantity")
    plt.show()

'''
4th step: define the function that shows the image
'''

def show_image(image, title="Image"):
    plt.imshow(image, cmap='gray') #imgshow = show the image
    plt.title(title)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    img = load_image("goat.jpg")
    gray = convert_gray(img)
    show_image(gray, "Gray scale image")
    histograma(gray)

