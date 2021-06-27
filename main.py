# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import time

import aircv as ac
import logging as log
import core.ant_forest as ant
import numpy as np


def compare_image():
    img_one = ac.imread("/Users/zheng/Documents/aircv-img/WechatIMG7.jpeg")
    img_two = ac.imread("/Users/zheng/Documents/aircv-img/WechatIMG9.jpeg")
    # print(ac.find_all_sift(img_two, img_one))
    # print(ac.find_all_sift(img_one, img_two))
    # print(ac.find_sift(img_one,img_two))
    result = ac.find_all_template(img_one, img_two, 0.8)
    for r in result:
        point = r['result']
        print(point)
        x = point[0]
        y = point[1]
        print(x)
        print(y)

        click(x, y - 50)

    print(ac.find_template(img_two, img_one))
    circle_center_pos = ['result']


def click(x, y):
    cmd = 'adb shell input tap ' + str(x) + ' ' + str(y)
    print(cmd)
    os.system(cmd)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # compare_image()
    while 1:
        log.info('开始...')
        ant.auto_charge()
        time.sleep(3)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
