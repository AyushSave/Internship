from pytube import YouTube

url = input("Enter YouTube video URL: ")
folder = input("Enter destination folder: ")

try:
    video = YouTube(url)

    print("Downloading:", video.title)

    stream = video.streams.get_highest_resolution()
    stream.download(output_path=folder)

    print("Download completed!")

except Exception as e:
    print("Invalid link or an error occurred.")
    print(e)
