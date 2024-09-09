
import cv2
import numpy as np

def onChange(x):
    pass

def filteringTrackbar():
    img = cv2.imread('data\noise.bmp', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Image not found or failed to load.")
        return
    cv2.namedWindow('filtering')
    cv2.createTrackbar('SIZE', 'filtering', 1, 20, onChange)
    cv2.imshow('filtering', img)

    while True:
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break

        size = cv2.getTrackbarPos('SIZE', 'filtering')
        if size == 0:
            size = 1

        kernel = np.ones((size, size), np.float32) / (size * size)
        dst = cv2.filter2D(img, -1, kernel)

        cv2.imshow('filtering', dst)
    cv2.destroyAllWindows()

filteringTrackbar()