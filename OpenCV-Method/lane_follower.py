# the driver of the LaneFollower class
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
from LaneFollower import LaneFollower

def main():
    lf = LaneFollower("lanes/forward_lane.jpg")
    lf.plot()
    lf.show_cv_img(1, img_title="Forward Lane")

main()