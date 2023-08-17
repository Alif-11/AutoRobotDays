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
    
    def show_cv_img(self, duration, img_title="Lane"):
        """
            Displays the OpenCV image

            Params: 
            - duration (int): time to display the image in seconds
            - img_title (string): the title of the window in which the image is displayed
            
            Returns:
            - None, only displays the image using OpenCV
        """
        cv.imshow(img_title, self.cv_img)
        cv.waitKey(duration*1000)
        cv.destroyAllWindows()
    
    def crop(self, boundary_pts):
        """
            Returns a cropped region of interest

            Params:
            - boundary_pts (numpy array): A numpy array of ordered pairs of points that specify the perimeter
                                          of the region of interest
              example: [[0,0], [0, 100], [100, 100], [100,0]]
            
            Returns:
            - The cropped region of the image
        """


    # TODO:
    # Figure out a way to crop the image so the lane lines are
    # the central focus of your image.
    # https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
    # Adapt the above stackoverflow code into your current program
