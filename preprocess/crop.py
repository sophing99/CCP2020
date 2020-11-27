#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Filename : crop
# @Date : 2020-11-21-19-01
# @Project : ccp
# @Author : seungmin

import numpy as np
import cv2
from PIL import Image


class PolygonDrawer(object):

    def __init__(self, window_name, frame):
        self.window_name = window_name
        self.frame = frame
        self.FINAL_LINE_COLOR = (255, 255, 255)
        self.WORKING_LINE_COLOR = (127, 127, 127)
        self.done = False
        self.done_all = False
        self.current = (0, 0)
        self.points = []

    def on_mouse(self, event, x, y, buttons, user_param):

        if event == cv2.EVENT_MOUSEMOVE:
            self.current = (x, y)

        elif event == cv2.EVENT_LBUTTONDOWN:
            print("Adding point #%d with position(%d,%d)" % (len(self.points), x, y))
            self.points.append((x, y))

        elif event == cv2.EVENT_RBUTTONDOWN:
            print("Completing polygon with %d points." % len(self.points))
            self.done = True

        if self.done:
            return

    def run(self):
        canvas = cv2.imread(self.frame)
        cv2.namedWindow(self.window_name, flags=cv2.WINDOW_AUTOSIZE)
        cv2.imshow(self.window_name, canvas)
        cv2.waitKey(1)

        while (not self.done_all):

            canvas = canvas.copy()
            cv2.setMouseCallback(self.window_name, self.on_mouse)

            if (len(self.points) > 0):
                cv2.polylines(canvas, np.array([self.points]), False, self.FINAL_LINE_COLOR, 2)
                cv2.line(canvas, self.points[-1], self.current, self.WORKING_LINE_COLOR)

            cv2.imshow(self.window_name, canvas)

            #if (len(self.points) > 0):
            #    cv2.fillPoly(canvas, np.array([self.points]), self.FINAL_LINE_COLOR)

            if cv2.waitKey(1) & 0xFF == 27:
                self.done_all = True

        xy = np.array(self.points)

        top_left_x = min(xy[:,0])
        top_left_y = min(xy[:,1])
        bot_right_x = max(xy[:,0])
        bot_right_y = max(xy[:,1])

        canvas = canvas[top_left_y:bot_right_y + 1, top_left_x:bot_right_x + 1]
        canvas = Image.fromarray(canvas)
        cv2.destroyWindow(self.window_name)
        return canvas.save("./input/crop_" + self.frame.split('/')[-1])
