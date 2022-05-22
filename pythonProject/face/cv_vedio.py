import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('images/andy2.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter('output.avi',fourcc,fps,size)

while True:
    ret,frame = cap.read()
    cv2.imshow('camera',frame)
    k = cv2.waitKey(1)
    out.write(frame)
    if k == ord('s'):
        break

cap.release()
cv2.destroyWindow()