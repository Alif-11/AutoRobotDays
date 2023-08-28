08/10/2023 20:50 
- I've made this repo, the README and this devlog
- The first two steps to the wheel assembly seem a bit complicated to do while tired at night, so I'll wait until tomorrow morning to do them

8/11/2023 22:23
- I've completed step 1, which was to complete the wheel assembly of one wheel, of the 27 step user manual to building this car.
- I have began training Sully Chen's code on my MacBook. I'll keep it running as I sleep tonight and I'll check the results tomorrow.
- The MacBook is hot to the touch, and I am scared if I continue training, it will overheat my laptop. I will have to find another way to train Chen's model.

8/13/2023 10:07
- Forgot to update last night so I'm updating now.
- Tried to train Chen's ML model on my Macbook. Worked until I realized my Macbook might as well have been taking off into the sky with the noises it made and decided to try Google Colab
- Turns out dropping 3 Gigs of images on Google Drive crashes it, so I had to zip it. Turns out unzipping 3 Gigs of images on Google Drive is a hassle, so I ran my gaming laptop all through the night of 8/12 to unzip the images. I am now almost done unzipping 44,000 images (41,000 have been unzipped).

8/14/2023 16:08 
- Finished step 7 of the robot. I finished both wheel assemblies, mounting servos to the camera pan-tilt mechanism, as well as mounting the batteries and battery holder to the main frame of the robot.

8/15/2023 23:40
- Attached the Raspberry Pi, Raspberry Pi Sunfounder Robot HAT, and Sunfounder Servo controller onto the main frame of the car.

8/16/2023 20:45
- Attached both motors to the tail end of the mainframe. Attached the driven wheels to the motors. Wired up the motors, and the Robot HAT and Servo controller to each other.

8/24 19:43
- Wired up all three servos, completing wiring. Had to remove the steering servo as it was blocking access to HDMI port, which I needed for Raspberry Pi setup.
- Finished up the code to crop an image to obtain just the lane lines. Researching how to obtain lane lines from the cropped photo.
