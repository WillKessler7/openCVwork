import numpy as np
import argparse
import cv2

def displayImage(image, label, text):
    if text != None:
        cv2.putText(image, text, (400, 775), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 2)
    cv2.imshow(label, image)
    k = cv2.waitKey(0)
    return k

def overlay(background, foreground, secondImage):

    numImages = 0
    if secondImage != None:
        numImages = 1
    
    for i in range(numImages):
        if i == 1:
            background = foreground
            foreground = secondImage
        backgroundCopy = background.copy()

        rows, cols, channels = foreground.shape
        # add region of interest
        roi = background[0:rows, 0:cols]

        foregroundGray = cv2.cvtColor(foreground, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(foregroundGray, 253, 255, cv2.THRESH_BINARY_INV)
        mask_inv = cv2.bitwise_not(mask)

        background_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

        foreground_fg = cv2.bitwise_and(foreground, foreground, mask = mask)





def main():
    garage = "garage.jpg"
    standingMorty = "Morty_Smith.png"
    standingRick = "Rick_Sanchez.png"
    introSlide = "RMtitle.png"


    garageImg = cv2.imread(garage)
    standingMortyImg = cv2.imread(standingMorty)
    standingRickImg = cv2.imread(standingRick)
    introSlideImg = cv2.imread(introSlide)

    introduction = displayImage(introSlideImg\
    , "Welcome to Rick and Morty's adventure", "Press any key to start.")
    cv2.destroyAllWindows()

    combinedImages, garageCopy = overlay(garageImg, standingRickImg, standingMortyImg)


main()
