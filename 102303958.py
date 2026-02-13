import sys
import os
import yt_dlp
from moviepy import VideoFileClip
from pydub import AudioSegment


# ---------------- DOWNLOAD VIDEOS ----------------
def download_videos(singer, num):
    print("Downloading videos...")

    os.makedirs("videos", exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'videos/%(id)s.%(ext)s',
        'noplaylist': True,
        'quiet': False
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_query = f"ytsearch{num}:{singer} official song"
        ydl.download([search_query])


# ---------------- CONVERT & TRIM ----------------
def convert_and_trim(duration):
    print("Converting and trimming...")
    os.makedirs("audios", exist_ok=True)

    for file in os.listdir("videos"):
        if file.endswith(".mp4"):

            video_path = os.path.join("videos", file)
            audio_path = os.path.join("audios", file.replace(".mp4", ".mp3"))

            try:
                clip = VideoFileClip(video_path)

                clip.audio.write_audiofile(
                    audio_path,
                    codec="mp3",
                    bitrate="192k"
                )

                clip.close()

                sound = AudioSegment.from_mp3(audio_path)
                trimmed = sound[:duration * 1000]

                trimmed.export(
                    audio_path,
                    format="mp3",
                    bitrate="192k"
                )

            except Exception as e:
                print("Skipping:", file, e)


# ---------------- MERGE ----------------
def merge_audios(output_file):
    print("Merging audios...")

    combined = AudioSegment.empty()

    audio_files = sorted(
        [f for f in os.listdir("audios") if f.endswith(".mp3")]
    )

    if not audio_files:
        print("No audio files found.")
        return

    for file in audio_files:
        path = os.path.join("audios", file)
        sound = AudioSegment.from_mp3(path)
        combined += sound

    combined.export(
        output_file,
        format="mp3",
        bitrate="192k"
    )

    print("Mashup created successfully:", output_file)


# ---------------- MAIN ----------------
def main():
    if len(sys.argv) != 5:
        print("Usage: python <rollno>.py <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
        sys.exit(1)

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except ValueError:
        print("NumberOfVideos and AudioDuration must be integers.")
        sys.exit(1)

    output_file = sys.argv[4]

    if num_videos <= 10:
        print("NumberOfVideos must be greater than 10.")
        sys.exit(1)

    if duration <= 20:
        print("AudioDuration must be greater than 20 seconds.")
        sys.exit(1)

    download_videos(singer, num_videos)
    convert_and_trim(duration)
    merge_audios(output_file)


if __name__ == "__main__":
    main()
