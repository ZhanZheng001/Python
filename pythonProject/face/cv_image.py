import cv2

#读取图片
frame = cv2.imread('images/andy.png')

#显示图片
cv2.imshow('andy',frame)
#键盘绑定函数
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('images/andy_copy.png',frame)
#销毁所有窗口
cv2.destroyWindow()