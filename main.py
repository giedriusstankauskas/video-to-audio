from pytube import YouTube
import os
import ssl

# code line to avoid [SSL: CERTIFICATE_VERIFY_FAILED] error on mac
ssl._create_default_https_context = ssl._create_unverified_context

songs_dir = f"{os.getcwd()}/songs"


def main():
    video_url = input('Enter YouTube video URL: ')  # enter YouTube video url you want to convert

    name = input("Enter filename: ")  # enter name you want to save your mp3 as
    video = YouTube(video_url).streams
    out_file = video.filter(only_audio=True).first().download(output_path=songs_dir, filename=name)  # download

    # rename mp4 to mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(f"Done. '{name}' was added to '{songs_dir}'")  # success message printed after converting


if __name__ == '__main__':
    main()
