# -*- coding: utf-8 -*-
"""
MP4 -> 旋转90度 -> 600x800 -> 1 bit/pixel -> binary
每帧: 600 bits/row = 75 bytes, 800 rows = 60000 bytes
"""
import cv2
import numpy as np
import os

VIDEO  = r'C:\Users\admin\Downloads\badapple.mp4'
OUTPUT = 'badapple.bin'

W, H = 600, 800      # 旋转后
W_O, H_O = 800, 600  # 旋转前（4:3）

cap = cv2.VideoCapture(VIDEO)
if not cap.isOpened():
    raise SystemExit('Cannot open: ' + VIDEO)

fps = cap.get(cv2.CAP_PROP_FPS)
print(f'fps = {fps:.2f}')

FRAME_BYTES = W * H // 8    # 60000
n = 0
with open(OUTPUT, 'wb') as f:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (W_O, H_O), interpolation=cv2.INTER_AREA)
        rotated = cv2.rotate(resized, cv2.ROTATE_90_COUNTERCLOCKWISE)  # 600x800

        # 1 = white, 0 = black
        binary = (rotated > 127).astype(np.uint8)
        packed = np.packbits(binary, axis=1)   # (800, 75), MSB first
        f.write(packed.tobytes())

        n += 1
        if n % 100 == 0:
            print(f'  frame {n}')

cap.release()
size = os.path.getsize(OUTPUT)
print(f'done: {n} frames, {size/1024/1024:.1f} MB')
print(f'per frame: {FRAME_BYTES} bytes')
