import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image

forward_lane_path = "lanes/forward_lane.jpg"

# A class that handles lane following on images
class LaneFollower:
    def __init__(self, lane_img_path):
        self.lane_path = lane_img_path
        self.cv_img = cv.imread(lane_img_path)
        if self.cv_img is None:
            print("The lane image could not be read in correctly. Please try again.")
    
    def get_shape(self):
        """
            Returns the size of the image

            Params:
            - None

            Returns:
            - A tuple where:
                - index 0 is the height of the image in pixels
                - index 1 is the width of the image in pixels
        """

        # The third element contains the type of CvMat object, which I won't need in this project.
        return self.cv_img.shape[0:2]

    def plot(self):
        """ 
            A function that plots the object's image on a 
            graph whose axes are the width and height of said image

            Params: 
            - None

            Returns: 
            - None, only plots the image
        """
        graph = np.asarray(Image.open(self.lane_path))
        plt.imshow(graph)
        plt.show()
    
    def show_cv_img(self, duration, img=None, img_title="Lane"):
        """
            Displays the OpenCV image

            Params: 
            - duration (int): time to display the image in seconds
            - img_title (string): the title of the window in which the image is displayed
            - img (OpenCV array): the image to be displayed
            
            Returns:
            - None, only displays the image using OpenCV
        """
        if img is None:
            img = self.cv_img
        cv.imshow(img_title, img)
        cv.waitKey(duration*1000)
        cv.destroyAllWindows()
    
    def crop(self, bound_pts):
        """
            Returns a cropped region of interest

            Params:
            - boundary_pts (numpy array): A numpy array of ordered pairs of points that specify the perimeter
                                          of the region of interest
              example: [[0,0], [0, 100], [100, 100], [100,0]]
            
            Returns:
            - The cropped region of the image
        """

        # Create a rectangle that encompasses the entire area of interest.
        bound_rect = cv.boundingRect(bound_pts)
        print("[LaneFollower.py] (x, y, width, height) = ", bound_rect)
        print("[LaneFollower.py] Note: x and y in the above print statement are the coordinates of the top left point of the bounding polygon")
        x, y, w, h = bound_rect
        # TODO: use bound_rect to crop out the region of interest
        cropped = self.cv_img[y:y+h, x:x+w].copy()

        # subtract each column of data values by the smallest number in its column
        bound_pts = bound_pts - bound_pts.min(axis=0)
        #print("[LaneFollower.py] cropped.shape: ", cropped.shape)
        mask = np.zeros(cropped.shape[:2], np.uint8)
        # returning cropped to do intermediate testing
        #return cropped
        #return bound_pts
        # a black and white image where the 
        # black is the background
        # and the white is the region bounded by the contours
        #
        # NOTE: making sure the 5th parameter, thickness, is negative is important for the bitwise operation below
        # having it not be negative means your contour area is not filled in, in the mask. when you go to apply your mask
        # onto your cropped image, it means you'll only see the the tiny sliver of the boundary of your cropped image
        cv.drawContours(mask, [bound_pts], -1, (255, 255, 255), -1, cv.LINE_AA)

        # Applies the mask to your cropped image, allowing you to go from rectangle crop to polygon crop.
        dst = cv.bitwise_and(cropped, cropped, mask=mask)
        return dst

    # TODO:
    # Continue out a way to crop the image so the lane lines are
    # the central focus of your image.
    # https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
    # Adapt the above stackoverflow code into your current program
