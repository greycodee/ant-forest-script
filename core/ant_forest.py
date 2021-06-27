import os
import time

import aircv as ac
import core.adb_cmd as amd

ksq = ac.imread('/Users/zheng/coding/study/ant-forest-script/img/ksq.jpeg')
znl = ac.imread('/Users/zheng/coding/study/ant-forest-script/img/znl.jpeg')


def auto_charge():
    # 截屏
    amd.screen_cap()
    amd.screen_pull()
    sc = ac.imread('./ant_page.png')
    print('开始查找可收取到能量球')
    ac_nlq = ac.find_all_template(sc, ksq, 0.8)
    for n in ac_nlq:
        point = n['result']
        print(point)
        x = point[0]
        y = point[1]
        print(x)
        print(y)
        amd.screen_click(x, y-50)
        print('睡眠 2 秒')
        time.sleep(1)

    ac_znl = ac.find_template(sc, znl)
    if ac_znl == 'None':
        print('未找到【找能量】按钮')
        amd.screen_delete()
        os.system('rm ./ant_page.png')
        return
    point = ac_znl['result']
    x = point[0]
    y = point[1]
    amd.screen_click(x, y)
    print('开始删除截图文件')
    amd.screen_delete()
    os.system('rm ./ant_page.png')
