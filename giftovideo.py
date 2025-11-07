import os
import sys
import argparse
import questionary
from contextlib import contextmanager
from moviepy import VideoFileClip

# Hiding output via context.
@contextmanager
def suppress_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout


# Checking file existence.
def isNotFileExists(src):
    if os.path.exists(src):
        return questionary.confirm(
                'The file {src} already exists. Do you want to overwrite it?'
        ).ask()
    else:
        return True


# Convert video to audio file (format mp3).
def convertToVideo(src='video.mp4'):
    with suppress_stdout():
        video = VideoFileClip(src)

    # Extract audio.
    basesrc = os.path.basename(src)
    filename = os.path.splitext(basesrc)[0]
    videoSrc = f'{filename}.mp4'
    if isNotFileExists(videoSrc):
        video.write_videofile(
            filename=videoSrc,
            audio=False
        )

    # Close.
    video.close()


# Checking video file extension.
def isGif(src='source'):
    if (src.split('.')[-1] == 'gif'):
        try:
            print(f'Processing file: {src}')

            with suppress_stdout():
                clip = VideoFileClip(src)
                clip.close()  # Closed the clip if it was successfully opened.
            return True
        except Exception as e:
            print(f'{src} is not a gif file or runtime error: {e}')
            return False
    else:
        print(f'{src} is not a gif file')
        return False


# Converting video files.
def convert(src):
    if os.path.exists(src):
        if isGif(src):
            convertToVideo(src)
    else:
        print(f'{src}: File does not exist')


def main(files):
    print('Processing file list.')

    for file in files:
        convert(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Processing file list.')
    parser.add_argument('files', nargs='+', help='List of files to process')

    args = parser.parse_args()
    main(args.files)
