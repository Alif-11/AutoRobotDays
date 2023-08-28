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
    
    # NOTE: The code written below was adapted from: https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
    def crop(self, bound_pts, file):
        """
            Returns a cropped region of interest

            Params:
            - bound_pts (Numpy array): A numpy array of ordered pairs of points that specify the perimeter
                                       of the region of interest
                                       example: [[0,0], [0, 100], [100, 100], [100,0]]
            - file (string): the location to which the cropped photo should be saved
            
            Returns:
            - The cropped region of the image
        """

        # Create a rectangle that encompasses the entire area of interest.
        bound_rect = cv.boundingRect(bound_pts)
        print("[LaneFollower.py] (x, y, width, height) = ", bound_rect)
        print("[LaneFollower.py] Note: x and y in the above print statement are the coordinates of the top left point of the bounding polygon")
        x, y, w, h = bound_rect
        cropped = self.cv_img[y:y+h, x:x+w].copy()

        # Subtract each column of data values by the smallest number in its column
        bound_pts = bound_pts - bound_pts.min(axis=0)
        #print("[LaneFollower.py] cropped.shape: ", cropped.shape)
        mask = np.zeros(cropped.shape[:2], np.uint8)

        # NOTE: Making sure the 5th parameter, thickness, is negative is important for the bitwise operation below
        # having it not be negative means your contour area is not filled in, in the mask. when you go to apply your mask
        # onto your cropped image, it means you'll only see the the tiny sliver of the boundary of your cropped image
        cv.drawContours(mask, [bound_pts], -1, (255, 255, 255), -1, cv.LINE_AA)

        # Applies the mask to your cropped image, allowing you to go from rectangle crop to polygon crop.
        dst = cv.bitwise_and(cropped, cropped, mask=mask)
        cv.imwrite(file, dst)

        # Return the cropped image
        return dst
    
    # NOTE: The code written below was adapted from: https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
    def detect_lanes(self, lane):
        """
            Returns an array containing the identified lane lines in the photo
            
            Params:
            - lane (string): contains the path that leads to the cropped jpeg file

            Returns: 
            - an array of all the detected lanes in the photo. each lane in the array,
              i.e. each element of the array, is represented by four data points:
              the x and y coordinate of the starting point, and 
              the x and y coordinate of the ending point
        """
        cropped = cv.imread(lane)
        # This line converts the color space of one image to another color space. 
        # 7 corresponds to the RGB2GRAY conversion, making RGB images Gray Scale
        gray_cropped = cv.cvtColor(cropped, 7)
        #cv.imshow("Gray Scale Cropped Image", gray_cropped)
        #cv.waitKey(2000)

        # Runs a Gaussian Blur on the image. The dimensions of the kernel size 
        # (the tuple) must be two odd numbers, not necessarily the same
        blur_gray_cropped = cv.GaussianBlur(gray_cropped, (5, 5), 0)
        cv.imshow("Blur Gray Scale", blur_gray_cropped)
        cv.waitKey(2000)

        low_threshold = 50
        high_threshold = 150
        # Runs Canny Edge detection on the image. The thresholds specify the range of
        # potentially acceptable edge intensities. Those above the high_threshold are guaranteed to be edges.
        cropped_edges = cv.Canny(blur_gray_cropped, low_threshold, high_threshold)

        cv.imshow("Edges", cropped_edges)
        cv.waitKey(2000)
        cv.destroyAllWindows()

        lane_lines = list()
        # IMPLEMENTATION HERE
        return lane_lines
