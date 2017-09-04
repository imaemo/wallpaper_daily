#! coding=utf-8

import ctypes
import urllib
import os
from datetime import datetime


def download_img():
    url = 'https://source.unsplash.com/1920x1080/?nature,water'
    img_dir = os.path.abspath(os.path.expanduser('~/Pictures/wallpaper'))
    if not os.path.isdir(img_dir):
        print '%s not exists, please crate it' % img_dir
    now = datetime.now()
    timestamp = now.strftime('%Y_%m_%d_%H_%M_%S')
    img_path = os.path.join(img_dir, timestamp + '.jpg')
    urllib.urlretrieve(url, img_path)
    return img_path


def set_wallpaper(path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 3)


img_path = download_img()
set_wallpaper(img_path)
