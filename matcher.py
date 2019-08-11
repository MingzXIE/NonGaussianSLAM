#!/usr/bin/env python2
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

target_point = 0
current_frame = 0
flag = -1
single_point = []
start_index = 18

file = open('coordinates.txt','w')
check = open('check.txt','w')
while (True):
    img1_path = './data/frame' + str(current_frame) + '.png'
    img2_path = './data/frame' + str(current_frame+1) + '.png'
    if os.path.exists(img2_path):
        img1 = cv.imread(img1_path,0) # queryImage
        img2 = cv.imread(img2_path,0) # trainImage
        # Initiate ORB detector
        orb = cv.ORB_create(nfeatures = 3000)
        # find the keypoints and descriptors with ORB
        kp1, des1 = orb.detectAndCompute(img1,None)
        kp2, des2 = orb.detectAndCompute(img2,None)
        # create BFMatcher object
        bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
        # Match descriptors.
        matches = bf.match(des1,des2)
        # Sort them in the order of their distance.
        matches = sorted(matches, key = lambda x:x.distance)

        # other matches
        if flag>0 :
            print current_frame
            find_flag = False
            for mat in matches:
                # find the target point
                # ensure tracking the same point
                if mat.queryIdx == target_point :
                    img1_index = mat.queryIdx
                    img2_index = mat.trainIdx
                    target_point = img2_index

                    (x1,y1) = kp1[img1_index].pt
                    file.write(str(x1)+','+str(y1))
                    file.write("\n")

                    target_point = img2_index
                    find_flag = True
                    print "Location:" + str(target_point)
                    break
            if not find_flag:
                print "tracking lost\n"
                break

        # first match
        else:
            print "Start"
            img1_index = matches[start_index].queryIdx
            img2_index = matches[start_index].trainIdx

            (x1,y1) = kp1[img1_index].pt
            (x2,y2) = kp2[img2_index].pt
            file.write(str(x1)+','+str(y1))
            file.write("\n")
            target_point = img2_index
            check.write(str(target_point))
            check.write("\n")
            flag = 1
        # # Initialize lists
        # list_kp1 = []
        # list_kp2 = []
        # # For each match...
        # for mat in matches:
        #
        #     # Get the matching keypoints for each of the images
        #     img1_idx = mat.queryIdx
        #     img2_idx = mat.trainIdx
        #
        #     # x - columns
        #     # y - rows
        #     # Get the coordinates
        #     (x1,y1) = kp1[img1_idx].pt
        #     (x2,y2) = kp2[img2_idx].pt
        #
        #     # Append to each list
        #     list_kp1.append((x1, y1))
        #     list_kp2.append((x2, y2))
        current_frame +=1
    else:
        print "Finish\n"
        break
