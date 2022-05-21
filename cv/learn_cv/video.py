import numpy as np
import cv2


def load_video(video):
    cap = cv2.VideoCapture(video)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH),
          cap.get(cv2.CAP_PROP_FRAME_HEIGHT),
          cap.get(cv2.CAP_PROP_FPS))
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv2.imshow('frame', frame)
        print(frame.shape)
        if cv2.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()




if __name__ == '__main__':
    load_video('../data/vtest.avi')

