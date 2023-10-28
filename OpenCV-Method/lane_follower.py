# the driver of the LaneFollower class
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
from LaneFollower import LaneFollower


def main():
    lf = LaneFollower()
    source_image_path = "lanes/forward_lane.jpg"
    source_image = lf.read(source_image_path)
    # Not needed anymore, as I have my bounding points.
    # lf.plot()
    cropped_image_path = "cropped_lane.jpg"
    boundary_points = np.array(
        [[150, 950], [1600, 950], [1100, 682], [750, 682]])
    print("[lane_follower.py, line 14] shape of the image:",
          lf.get_shape(source_image))
    cropped_roi = lf.crop_roi(
        boundary_points, source_image)
    # print("original points: ", boundary_points)
    # print("modified points: ", cropped)
    # lf.show_cv_img(3, cropped, "Mask")
    lf.detect_lanes(cropped_roi)


main()
