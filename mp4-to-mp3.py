from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
import os

from concurrent.futures import ThreadPoolExecutor
from moviepy.video.io.VideoFileClip import VideoFileClip
from pydub import AudioSegment
import os

def convert_mp4_to_mp3(mp4_file, output_folder):
    video_clip = VideoFileClip(mp4_file)
    audio_clip = video_clip.audio

    mp3_file = os.path.join(output_folder, os.path.splitext(os.path.basename(mp4_file))[0] + ".mp3")
    audio_clip.write_audiofile(mp3_file, codec='mp3')

    # Close the video and audio clips to release resources
    video_clip.close()
    audio_clip.close()

def process_file(file_tuple):
    mp4_file, output_folder = file_tuple
    convert_mp4_to_mp3(mp4_file, output_folder)
    os.remove(mp4_file)
    print(f"Conversion complete: {os.path.basename(mp4_file)}, original MP4 file removed.")

def batch_convert_mp4_to_mp3_parallel(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Collect file tuples
    file_tuples = [(os.path.join(input_folder, file_name), output_folder) for file_name in os.listdir(input_folder) if file_name.endswith(".mp4")]

    with ThreadPoolExecutor() as executor:
        executor.map(process_file, file_tuples)
if __name__ == "__main__":
    # Specify your input and output folders
    input_folder = "./Music"
    output_folder = "./Music"

    batch_convert_mp4_to_mp3_parallel(input_folder, output_folder)
