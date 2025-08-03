import cv2 # OpenCV Library

# Image to detect shapes on below
image = cv2.imread(r"C:\Users\omar1\OneDrive\Documents\Shape Detection\shape.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Converting to gray image

# Setting threshold value to get new image (In simpler terms: this function checks every pixel, and depending on how
# dark the pixel is, the threshold value will convert the pixel to either black or white (0 or 1)).
_, thresh_image = cv2.threshold(gray_image, 220, 255, cv2.THRESH_BINARY)

# Retrieving outer-edge coordinates in the new threshold image
contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Iterating through each contour to retrieve coordinates of each shape
for i, contour in enumerate(contours):
    if i == 0:
        continue

    epsilon = 0.01*cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    cv2.drawContours(image, contour, 0, (0, 0, 0), 4)

    x, y, w, h= cv2.boundingRect(approx)
    x_mid = int(x + (w/3)) # This is an estimation of where the middle of the shape is in terms of the x-axis.
    y_mid = int(y + (h/1.5)) # This is an estimation of where the middle of the shape is in terms of the y-axis.

    # Setting some variables which will be used to display text on the final image
    coords = (x_mid, y_mid)
    colour = (0, 0, 0)
    font = cv2.FONT_HERSHEY_DUPLEX


    if len(approx) == 3:
        cv2.putText(image, "Triangle", coords, font, 1, colour, 1) # Text on the image
    elif len(approx) == 4:
        cv2.putText(image, "Quadrilateral", coords, font, 1, colour, 1)
    elif len(approx) == 5:
        cv2.putText(image, "Pentagon", coords, font, 1, colour, 1)
    elif len(approx) == 6:
        cv2.putText(image, "Hexagon", coords, font, 1, colour, 1)
    else:
        # If the length is not any of the above, guess the shape to be a circle.
        cv2.putText(image, "Circle", coords, font, 1, colour, 1)
    
# Displaying the image with the detected shapes onto the screen
cv2.imshow("shapes_detected", image)

cv2.waitKey(0)
