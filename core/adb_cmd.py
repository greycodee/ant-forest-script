import os


# 截屏
def screen_cap():
    os.system('adb shell screencap -p /sdcard/ant_page.png')
    print('【adb命令】截屏')


# 点击屏幕
def screen_click(x, y):
    cmd = 'adb shell input tap ' + str(x) + ' ' + str(y)
    os.system(cmd)
    print('【adb命令】点击屏幕')


# 传输截图到本地
def screen_pull():
    os.system('adb pull /sdcard/ant_page.png ./ant_page.png')
    print('【adb命令】传输截图到本地')


# 删除手机截图
def screen_delete():
    os.system('adb shell rm /sdcard/ant_page.png')
    print('【adb命令】删除手机截图')
