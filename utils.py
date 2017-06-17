# -*- coding:utf-8 -*-

import os
import logging

import config


class Logger(object):
    def __init__(self, logger_name, file_handler):
        self._log = logging.getLogger(logger_name)
        self._log.addHandler(file_handler)
        self._log.setLevel(file_handler.level)

    def __getattr__(self, *args, **kwds):
        return getattr(self._log, *args, **kwds)


def get_all_modules(exclude_files=()):
    return [f for f in os.listdir(config.ACCOUNTS_DIR)
            if f.endswith(".py")
            and not f.startswith("__")
            and f not in exclude_files]


def get_config_from_module(module_name):
    module = __import__("accounts.%s" % module_name, fromlist=['accounts'])
    return getattr(module, "CONFIG")
