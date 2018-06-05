# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 12:09
# @Author  : liugang9
# @Email   : mlcc330@hotmail.com
# @File    : checkip.py
# @Software: PyCharm
# @license: Apache Licence
# @contact: 3323202070@qq.com

"""

"""

import urllib
import re
import sys

def ISIP(s):
    return len([i for i in s.split('.') if (0<=int(i)<=255)]) == 4

def searchFromIP(ip):
    uip = urllib.urlopen('http://m.ip138.com/ip.asp?ip=%s' % ip)
    fip = uip.read()
    try:
        if fip != "":
            rip = re.compile(r"您查询的IP：(\d+.\d+.\d+.\d+).*本站主数据：(\S+  \S+)</p>.*参考数据一：(\S+ \S+)</p>.*网友提交的IP：(\S+ \S+)</p>")
            results = rip.findall(fip)
            # result = str(result).replace('u\'', '\'')
            # print(type(result))
        else:
            rip = re.compile(r"您查询的IP：(\d+.\d+.\d+.\d+).*本站主数据：(\S+  \S+)</p>.*")
            results = rip.findall()
            # result = str(result).replace('u\'','\'')
            # print(type(result))
    except Exception as e:
        print(e)

    for result in results:
        print('%s\t %s' % (ip,result))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('please enter a ip address')
        sys.exit()
    input = sys.argv[1]
    # if not re.findall()
    if ISIP(input):
        ipadress = input
        searchFromIP(ipadress)
    else:
        print('ip is not found.')