import cv2
import os
import glob

def images_to_video(image_folder, output_video_file, fps=30):
    """
    Convert a set of images in a folder to a video.

    :param image_folder: Folder containing images.
    :param output_video_file: Output video file path.
    :param fps: Frames per second for the output video.
    """
    # Get all image file paths
    image_files = sorted(glob.glob(os.path.join(image_folder, '*.jpg')))
    # Read the first image to determine the video size
    frame = cv2.imread(image_files[0])
    height, width, layers = frame.shape

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec used to compress the frames
    out = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

    for image_file in image_files:
        frame = cv2.imread(image_file)
        out.write(frame)  # Write the frame to the video file

    out.release()  # Release the VideoWriter

# Example usage
image_folder = 'C:/Users/WCL/Desktop/qwe'  # Update this to your images folder path
output_video_file = 'C:/Users/WCL/Desktop/output_video.mp4'
fps = 30  # Frames per second
images_to_video(image_folder, output_video_file, fps)
