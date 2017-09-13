#!/usr/bin/env python

'''
This is a test code fot Ec601 class, we use this example to detect upright people in images using HOG features
Usage format:
    peopledetect.py <image_names>
Press Escape to Stop code
'''

#could only detect peaple that are really obvious in the images

# Compatibile with Python 2/3
from __future__ import print_function

import numpy as np
import cv2


def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh


def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)


if __name__ == '__main__':
    import sys
    from glob import glob
    import itertools as it

    print(__doc__)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )

    default = ['../data/basketball2.png '] if len(sys.argv[1:]) == 0 else []

    for fn in it.chain(*map(glob, default + sys.argv[1:])):
        print(fn, ' - ',)
        try:
            img = cv2.imread(fn)
            if img is None:
                print('Sorry, this image cannot be processed:', fn)
                continue
        except:
            print('loading error')
            continue

        found, w = hog.detectMultiScale(img, winStride=(8,8), padding=(32,32), scale=1.05)
        found_filtered = []
        for ri, r in enumerate(found):
            for qi, q in enumerate(found):
                if ri != qi and inside(r, q):
                    break
            else:
                found_filtered.append(r)
        draw_detections(img, found)
        draw_detections(img, found_filtered, 3)
        print('The number of people found in the image are %d, the total number of raw data points found was(%d)' % (len(found_filtered), len(found)))
 # //The lines beyond this point don't run due to lack of a reciprocative library
 #       cv2.imshow('img', img)
 #       ch = cv2.waitKey()
 #       if ch == 27:
 #           break
 #     cv2.destroyAllWindows()
