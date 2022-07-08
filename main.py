#   SOURCES:
#   https://stackoverflow.com/questions/42492246/how-to-normalize-the-volume-of-an-audio-file-in-python
#   https://www.codespeedy.com/download-youtube-video-as-mp3-using-python/

import os
from pydub import AudioSegment
from pytube import YouTube

downloadPath = "downloads"
normalizedPath = "normalized"


def setAudioLevel(audioFile, dBTarget):
    extension = audioFile.split(".")[1]
    audioObject = AudioSegment.from_file(downloadPath + "/" + audioFile, extension)
    delta = dBTarget - audioObject.dBFS
    audioObject.apply_gain(delta)
    audioObject.export(normalizedPath + "/" + audioFile.split(".")[0] + ".mp4", format="mp4")
    print(f"Downloaded and set {audioFile}")


def downloadAudioFile(link):
    video = YouTube(link)
    list = video.streams.filter(only_audio=True, file_extension="mp4")
    list[0].download(downloadPath)
    return list[0].title + ".mp4"


def readURLs():
    urlFile = "urls.txt"
    f = open(urlFile, "r")
    lines = f.readlines()
    list = []
    for line in lines:
        list.append(line)
    return list


def exec_Python_youtube_normalized():
    file = "urls.txt"
    if not os.path.isfile(file):
        f = open(file, "w")
        f.close()

    dir = downloadPath
    if not os.path.isdir(dir):
        os.mkdir(dir)

    dir = normalizedPath
    if not os.path.isdir(dir):
        os.mkdir(dir)

    list = readURLs()
    for item in list:
        file = downloadAudioFile(item)
        setAudioLevel(file, -20)


if __name__ == '__main__':
    exec_Python_youtube_normalized()
