import time

import logging as log
import core.ant_forest as ant


if __name__ == '__main__':
    while 1:
        log.info('开始...')
        ant.auto_charge()
        time.sleep(3)



