# -*- coding:utf-8 -*-

import time

class TestBot(object):
    def __init__(self, name):
        self.name = name
        self.run = True

    def work(self):
        x = 0
        while self.run:
            with open('testbot.txt', 'a') as f:
                f.write('%s write -> %s\n' % (self.name, x))
                # time.sleep(0.5)
                self.run = True if x < 100 else False
            x += 1
