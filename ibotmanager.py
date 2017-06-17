# -*- coding:utf-8 -*-

import os
import time
import signal
import atexit
import logging
from threading import Thread

import config
from bot.instabot import InstaBot, RUN
from utils import get_all_modules, get_config_from_module, Logger

if not os.path.exists(config.LOG_TO):
    os.makedirs(config.LOG_TO)


fh = logging.FileHandler(os.path.join(config.LOG_TO, config.LOGGER.get('file')))
fh.setLevel(config.LOGGER.get('level'))
fh.setFormatter(config.LOGGER.get('formatter'))

log = Logger("IBotManager", fh)


modules = get_all_modules()

threads = [Thread(target=InstaBot(**get_config_from_module(module_name[:-3])).new_auto_mod,
                  name=module_name[:-3]) for module_name in modules]


for t in threads:
    try:
        log.debug("Try start '%s' bot" % t.name)
        t.start()
        log.debug("Successfully start '%s' bot." % t.name)
    except Exception as ex:
        log.exception("Error during work bot")

[t.join() for t in threads if t.is_alive()]


def stop_all_process():
    signal.alarm(1)

atexit.register(stop_all_process)
time.sleep(5)
