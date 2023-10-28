import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image

forward_lane_path = "lanes/forward_lane.jpg"

# A class that handles lane following on images


class LaneFollower:
    def __init__(self):
        pass

    def read(self, img_path):
        """
            Reads in the image located at [img_path].
            Throws an exception if the image cannot be properly read

            Params:
            - img_path (string): path location of the image

            Returns:
            - The image read from [img_path]
        """
        image = cv.imread(img_path)
        if image is None:
            raise Exception("Image could not be read properly.")
        else:
            return image

    def get_shape(self, image):
        """
            Returns the size of the image

            Params:
            - image (Mat): the input image

            Returns:
            - A tuple where:
                - index 0 is the height of the image in pixels
                - index 1 is the width of the image in pixels
        """

        # The third element contains the type of CvMat object, which I won't need in this project.
        return image.shape[0:2]

    def plot(self, img_path):
        """ 
            A function that plots the object's image on a 
            graph whose axes are the width and height of said image

            Params: 
            - img_path (string): path location of the image

            Returns: 
            - None, only plots the image
        """
        graph = np.asarray(Image.open(img_path))
        plt.imshow(graph)
        plt.show()

    def show_cv_img(self, duration, img_path, img_title="Lane"):
        """
            Displays the OpenCV image

            Params: 
            - duration (int): time to display the image in seconds
            - img_title (string): the title of the window in which the image is displayed
            - img_path (string): path location of the image

            Returns:
            - None, only displays the image using OpenCV
        """
        img = self.read(img_path)
        cv.imshow(img_title, img)
        cv.waitKey(duration*1000)
        cv.destroyAllWindows()

    # NOTE: The code written below was adapted from: https://stackoverflow.com/questions/48301186/cropping-concave-polygon-from-image-using-opencv-python
    def crop_roi(self, bound_pts, source_image):
        """
            Takes in the input image of [source_image], crops it based on 
            [bound_pts], and returns the cropped image

            Params:
            - bound_pts (Numpy array): 
                        a numpy array of ordered pairs of points 
                        that specify the perimeter of the region of interest
                        example: [[0,0], [0, 100], [100, 100], [100,0]]
            - source_image (Mat): our input image

            Returns:
            - The cropped image
        """

        # Create a rectangle that encompasses the entire area of interest.
        bound_rect = cv.boundingRect(bound_pts)
        print("[LaneFollower.py] (x, y, width, height) = ", bound_rect)
        print("[LaneFollower.py] Note: x and y in the above print statement are the coordinates of the top left point of the bounding polygon")
        x, y, w, h = bound_rect
        # read in the image
        cropped = source_image[y:y+h, x:x+w].copy()

        # Subtract each column of data values by the smallest number in its column
        bound_pts = bound_pts - bound_pts.min(axis=0)
        mask = np.zeros(cropped.shape[:2], np.uint8)

        # NOTE: Making sure the 5th parameter, thickness, is negative is important for the bitwise operation below
        # having it not be negative means your contour area is not filled in, in the mask. when you go to apply your mask
        # onto your cropped image, it means you'll only see the the tiny sliver of the boundary of your cropped image
        cv.drawContours(mask, [bound_pts], -1, (255, 255, 255), -1, cv.LINE_AA)

        # Applies the mask to your cropped image, allowing you to go from rectangle crop to polygon crop.
        dst = cv.bitwise_and(cropped, cropped, mask=mask)

        # Return the cropped image
        return dst

    # TODO
    def crop_by_color(self, color_range, image):
        """
            Takes in the input image stored at [file], applies a mask to it 
            which selects for pixels whose BGR values fall within [color_range],
            and stores the modified image to PATH [file]

            Params:
            - color_range (double (triple int tuple) tuple): 
                          any pixels in [file] whose BGR values fall between
                          the first and second components of [color_range] will
                          appear in the returned file

            - image (Mat): the input image

            Returns:
            - A modified [image] which has been cropped based on [color_range]
        """
        pass

    # NOTE: The code written below was adapted from: https://stackoverflow.com/questions/45322630/how-to-detect-lines-in-opencv
    def detect_lanes(self, cropped):
        """
            Returns an array containing the identified lane lines in the photo

            Params:
            - cropped (Mat): the cropped image

            Returns: 
            - an array of all the detected lanes in the photo. each lane in the array,
              i.e. each element of the array, is represented by four data points:
              the x and y coordinate of the starting point, and 
              the x and y coordinate of the ending point
        """
        # This line converts the color space of one image to another color space.
        # 7 corresponds to the RGB2GRAY conversion, making RGB images Gray Scale
        gray_cropped = cv.cvtColor(cropped, 7)
        # cv.imshow("Gray Scale Cropped Image", gray_cropped)
        # cv.waitKey(2000)

        # Runs a Gaussian Blur on the image. The dimensions of the kernel size
        # (the tuple) must be two odd numbers, not necessarily the same
        blur_gray_cropped = cv.GaussianBlur(gray_cropped, (5, 5), 0)
        cv.imshow("Blur Gray Scale", blur_gray_cropped)
        cv.waitKey(2000)

        low_threshold = 50
        high_threshold = 150
        # Runs Canny Edge detection on the image. The thresholds specify the range of
        # potentially acceptable edge intensities. Those above the high_threshold are guaranteed to be edges.
        cropped_edges = cv.Canny(
            blur_gray_cropped, low_threshold, high_threshold)

        cv.imshow("Edges", cropped_edges)
        cv.waitKey(2000)
        cv.destroyAllWindows()

        lane_lines = list()
        # IMPLEMENTATION HERE
        return lane_lines
