import cv2
import imutils
import numpy as np
from imutils import paths
from imutils.object_detection import non_max_suppression


def hog_clf(descriptor_type='default'):
    if descriptor_type == 'daimler':
        winSize = (48, 96)
        blockSize = (16, 16)
        blockStride = (8, 8)
        cellSize = (8, 8)
        nbins = 9
        hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins)
        hog.setSVMDetector(cv2.HOGDescriptor_getDaimlerPeopleDetector())
        return hog
    else:
        winSize = (64, 128)
        blockSize = (16, 16)
        blockStride = (8, 8)
        cellSize = (8, 8)
        nbins = 9
        hog = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins)
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        return hog


def detect_image(hog, image):
    # image = cv2.imread(image_path)
    image = imutils.resize(image, width=min(400, image.shape[1]))
    orig = image.copy()

    # detect people in the image
    (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                            padding=(8, 8), scale=1.1)

    # draw the original bounding boxes
    for (x, y, w, h) in rects:
        cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # apply non-maxima suppression to the bounding boxes using a
    # fairly large overlap threshold to try to maintain overlapping
    # boxes that are still people
    rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

    # draw the final bounding boxes
    for (xA, yA, xB, yB) in pick:
        cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # show some information on the number of bounding boxes
    print("[INFO] {} original boxes, {} after suppression".format(
        len(rects), len(pick)))
    return image


def detect_images(hog, images_path):
    # loop over the image paths
    for image_path in paths.list_images(images_path):
        # load the image and resize it to (1) reduce detection time
        # and (2) improve detection accuracy
        orig = cv2.imread(image_path)
        image = detect_image(hog, orig)

        # show the output images
        cv2.imshow("Before NMS", orig)
        cv2.imshow("After NMS", image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break


def detect_video(hog, video_path):
    cap = cv2.VideoCapture(video_path)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        detected = detect_image(hog, frame)
        cv2.imshow("capture", detected)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    # ap = argparse.ArgumentParser()
    # ap.add_argument("-i", "--images", required=True, help="path to images directory")
    # args = vars(ap.parse_args())
    # detect_images(args['images'])

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    hog = hog_clf()
    images_path = '../data/imgs/persons'
    detect_images(hog, images_path)

    video_path = '../data/video/vtest.avi'
    detect_video(hog, video_path)
