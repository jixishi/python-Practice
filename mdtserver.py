# coding:utf8

import urllib.request

import json

import jsonpath

url = "https://mdt.wayzer.top/api/servers/list"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"}
request = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(request)
html = response.read()
un = json.loads(html)
ln = "\n"
n = ".名字："
p = ".地址："
t = ".地图："
b = ".模式："
s = ".玩家数："
m = ".延迟："
w = ".波数:"
name_list = jsonpath.jsonpath(un, "$..name")
ip_list = jsonpath.jsonpath(un, "$..address")
map_list = jsonpath.jsonpath(un, "$..mapName")
mode_list = jsonpath.jsonpath(un, "$..mode")
play_list = jsonpath.jsonpath(un, "$..players")
timeMs_list = jsonpath.jsonpath(un, "$..timeMs")
wave_list = jsonpath.jsonpath(un, "$..wave")
f = open("./servers.txt", "a", encoding='utf-8')
for i in range(28):
    x = i + 1
    ext = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (
        x, n, name_list[i], ln, x, p, ip_list[i], ln, x, t, map_list[i], ln, x, b, mode_list[i],
        ln, x, m, timeMs_list[i], ln, x, w, wave_list[i], ln, x, s, play_list[i], ln,
        ln)
    f.write(ext)
f.close()
