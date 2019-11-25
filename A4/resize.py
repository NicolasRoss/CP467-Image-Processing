import numpy as np
import cv2

img = cv2.imread("alphabet.png")
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

_, imgthreshold = cv2.threshold(gray, 127, 255, 0)
contours, b = cv2.findContours(255 - imgthreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

number_imgs = []
number_btm_mid_pos = []
for cnt in contours:
    (x, y, w, h) = cv2.boundingRect(cnt)
    number_imgs.append(img[y: y + h, x: x + w])
    number_btm_mid_pos.append((int(x + w / 2), y + h))

# resize symbols and put them back
output_img = np.ones_like(img) * 255
resize_ratio = 0.5
for (i, num_im) in enumerate(number_imgs):
    num_im = cv2.resize(num_im, (0,0), fx=resize_ratio, fy=resize_ratio)
    (img_h, img_w) = num_im.shape[:2]
    # x1, y1, x2, y2
    btm_x, btm_y = number_btm_mid_pos[i]
    x1 = btm_x - int(img_w / 2)
    y1 = btm_y - img_h
    x2 = x1 + img_w
    y2 = y1 + img_h
    output_img[y1:y2, x1:x2] = num_im

cv2.imwrite("output.png", output_img)