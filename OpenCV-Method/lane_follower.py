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
    boundary_points = np.array([[0,950], [1600, 950], [1400, 682], [600, 682]])
    print("[lane_follower.py] shape of the image:", lf.get_shape())
    cropped = lf.crop(boundary_points)
    #print("original points: ", boundary_points)
    #print("modified points: ", cropped)
    lf.show_cv_img(3, cropped, "Mask")

main()