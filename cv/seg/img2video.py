import cv2
import os
from tqdm import tqdm

image_folder = './video_seg/v2j'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_name, fourcc, 10, (width,height))
images.sort(key=lambda s: int(s.split('.')[0].split('-')[1]))
for image in tqdm(images):
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()


# import os
# import moviepy.video.io.ImageSequenceClip
# image_folder = './video_seg/v2j'
# fps = 10
#
# image_files = [os.path.join(image_folder,img)
#                for img in os.listdir(image_folder)
#                if img.endswith(".jpg")]
# clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
# clip.write_videofile('my_video.mp4')