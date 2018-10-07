import os


def search_data(path, videoList):
    newpath = path
    if os.path.isfile(path):
        videoList.append(path)
    elif os.path.isdir(path):
        for s in os.listdir(path):
            newpath = os.path.join(path, s)
            search_data(newpath, videoList)
    return videoList


def getfiles(path):
    templist = list()
    search_data(path, templist)
    videolist = list()
    for i in templist:
        videolist.append(i.replace(path, ""))
    return videolist