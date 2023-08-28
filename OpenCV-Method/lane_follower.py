# the driver of the LaneFollower class
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
from LaneFollower import LaneFollower

def main():
    lf = LaneFollower("lanes/forward_lane.jpg")
    # Not needed anymore, as I have my bounding points. 
    #lf.plot()
    cropped_file_path = "cropped_lane.jpg"
    boundary_points = np.array([[150,950], [1600, 950], [1100, 682], [750, 682]])
    print("[lane_follower.py] shape of the image:", lf.get_shape())
    cropped = lf.crop(boundary_points, cropped_file_path)
    #print("original points: ", boundary_points)
    #print("modified points: ", cropped)
    #lf.show_cv_img(3, cropped, "Mask")
    lf.detect_lanes(cropped_file_path)

main()