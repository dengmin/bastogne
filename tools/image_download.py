""""多线程下载电影图片
部分douban图片无法正常显示，可以利用此程序将图片下载到本地
"""
import os
from base64 import urlsafe_b64encode
from queue import Queue
import threading
from threading import Thread
from urllib.request import urlopen
from urllib.error import HTTPError
from pymongo import MongoClient

db = MongoClient().bastogne
queue = Queue()
movies = db.movie.find().limit(7000).skip(6000)

for movie in movies:
    queue.put(movie['image'])


class DownloadThread(Thread):
    def __init__(self, save_path):
        super().__init__()
        self.save_path = save_path
        if os.path.exists(self.save_path) is not True:
            #递归建立目录
            os.makedirs(self.save_path)

    def run(self):
        while queue.empty() is False:
            url = queue.get()
            with open(self.save_path + urlsafe_b64encode(url.encode()).decode() + '.jpg', 'wb') as f:
                try:
                    res = urlopen(url)
                    f.write(res.read())
                    # print(self.getName())
                    print(threading.active_count())
                    # print(url, 'ok')
                except HTTPError as e:
                    print(url, e)
                    continue


def main():
    #路径格式：e:/Temp/bastogne/image/
    save_path = input('请输入保存路径:')
    thread_num = int(input('请输入开启的下载线程数目:'))
    for i in range(thread_num):
        download = DownloadThread(save_path)
        download.start()
    queue.join()

    print('下载完毕')


if __name__ == '__main__':
    main()