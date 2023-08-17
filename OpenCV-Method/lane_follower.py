# the driver of the LaneFollower class
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
from PIL import Image
from LaneFollower import LaneFollower

def main():
    lf = LaneFollower("lanes/forward_lane.jpg")
    lf.plot()
    boundary_points = np.array([[0,1200], [1600, 1200], [1400, 800], [600, 800]])
    print(lf.get_shape())
    lf.crop(boundary_points)

main()