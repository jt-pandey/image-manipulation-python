import os
from PIL import Image, ImageFilter
file=input("Please enter file name: ")
img=Image.open(file)
choice=1
print("-"*50,"\n", "\tIMAGE MANIPULATION PROGRAM\t\n")
print("-"*50)

while(choice!=0):
    print("*"*50)
    print("Please choose from the following choices: ")
    print("\
          1)Open Image\n\
          2)Display image properties\n\
          3)Rotate image\n\
          4)Convert image to another format\n\
          5)Resize image\n\
          6)Blur image\n\
          7)Flip image\n\
          8)Crop image\n\
          9)Convert to Grayscale\n\
          0)Exit Menu")
    choice=int(input("Please enter your choice: "))

    #Display Image
    if(choice==1):
        img.show()

    #Displaying image properties
    elif(choice==2):
        print("Size of image: ",img.size)
        print("Width of image: ", img.width)
        print("Height of image: ", img.height)

    #Rotating Image by a certain angle
    elif(choice==3):
        angle=int(input("Please enter the angle by which the image is to be rotated: "))
        rotated_img=img.rotate(angle)
        print("Image rotated successfully!")
        rotated_img.show()

    #Converting image from one format to another
    elif(choice==4):
        curr, mod=input("Please enter the current format: "), input("Please enter the format the image is to be saved in: ")
        im=Image.open(file).convert("RGB")
        img.save(file[0:file.find(curr)-1],mod)
        print("Image Saved Successfully!")

    #Resizing images
    elif(choice==5):
        height, width=int(input("Please enter the height: ")), int(input("Please enter the width: "))
        sImg=img.resize((height, width))
        print("Image resized successfully!")
        sImg.show()

    #Blurring image
    elif(choice==6):
        blur_img=img.filter(filter=ImageFilter.BLUR)
        print("Image blurred successfully!")
        blur_img.show()

    #Flipping image (Mirror Image)
    elif(choice==7):
        flip_img=img.transpose(Image.FLIP_LEFT_RIGHT)
        print("Image flipped successfully!")
        flip_img.show()

    #Cropping image
    elif(choice==8):
        print("Please enter the details in the following order separated by spaces (LEFT, UPPER, RIGHT, LOWER)")
        l,u,r,lo=int(input()), int(input()), int(input()),int(input())
        cropped_img=img.crop((l,u,r,lo))
        print("Image cropped successfully!")
        cropped_img.show()

    #Converting image to grayscale
    elif(choice==9):
        gray_img=img.convert("L")
        print("Image converted to grayscale succcessfully!")
        gray_img.show()

    #Exit option
    elif(choice==0):
        print("Thank you for using our Image Manipulation Program!")
        print("Quitting...")
        print("*"*50)
        break

    #Default option
    else:
        print("Invalid Choice\nPlease try again!")
        continue

print("Program completed successfully!")
print("*"*50)
