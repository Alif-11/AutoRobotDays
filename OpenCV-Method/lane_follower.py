import cv2 as cv

forward_lane_path = "lanes/forward_lane.jpg"

# forward_lane now contains an OpenCV Mat object of the image
forward_lane = cv.imread(forward_lane_path)

if forward_lane is None:
    print("Forward lane could not be read in correctly")
else:
    cv.imshow("Forward Lane", forward_lane)
    # waits for a user to press a key, in this case for 1000 milliseconds
    cv.waitKey(1000)
    cv.destroyAllWindows()