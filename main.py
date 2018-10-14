# -*- coding: utf-8 -*-
# @Time    : 2018/10/3 下午9:39
# @Author  : __apple

from scrapy.cmdline import execute

# execute(["scrapy", "startproject", "douban"])

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "movie"])