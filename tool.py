# coding=utf-8
import ctypes
import json
import os

import progressbar
import requests
import urllib.parse
import urllib.request
import requests.packages.urllib3
import win32api
import win32con


def IfDir(path):  # 判断目录是否存在
    os.path.isdir(path)


def CreateDir(path):  # 创建目录
    os.makedirs(path)


def IfFile(path):  # 判断文件是否存在
    os.path.isfile(path)


def WriteAllText(path, text):  # 覆盖写入文件或者创建文件
    file = open(path, mode="w", encoding="utf-8")
    file.write(text)
    file.close()


def WriteCapText(path, text):  # 追加写入文件
    file = open(path, mode="a", encoding="utf-8")
    file.write(text)
    file.close()


# 自定格式读写入文件
def WriteText(path, mode, text):
    if mode == "w":
        file = open(path, mode=mode, encoding="utf-8")
        file.write(text)
        file.close()
    elif mode == "a":
        file = open(path, mode=mode, encoding="utf-8")
        file.write(text)
        file.close()
    elif mode == "r":
        file = open(path, mode=mode, encoding="utf-8")
        while True:
            output = file.read(1024 * 1024)
            if not output:
                break
            yield output


def WorkingPath():
    os.getcwd()


def FileLine(path):  # 获取文件每行内容并以列表返回
    ls = []
    for line in open(path, 'r', encoding='utf-8'):
        ls.append(line.strip('\n'))
    return ls


# 把文件内容隔指定行数,然后分列表返回
# lt1,lt2,lt3,~,ltn = CreateList(path, n)
# lt’i‘ 从第 i 行开始隔 n 行取下一个值所构成的列表
def CreateList(path, amount):
    lt = []
    for line in open(path, 'r', encoding='utf-8'):
        lt.append(line.strip('\n'))
    for i in range(amount):
        globals()["list" + str(i)] = lt[i::amount]
    return tuple(globals()["list" + str(i)] for i in range(amount))


# 弹出对话框参数 （标题，内容，模式）ctypes.WinDLL("user32.dll").MessageBoxW
def WinTitleA(title, con, mode):
    if mode == "o":  # 提醒OK消息框
        win32api.MessageBox(0, con, title, win32con.MB_OK)
    elif mode == "yn":  # 是否信息框
        win32api.MessageBox(0, con, title, win32con.MB_YESNO)
    elif mode == "s":  # 说明信息框
        win32api.MessageBox(0, con, title, win32con.MB_HELP)
    elif mode == "!":  # 警告信息框
        win32api.MessageBox(0, con, title, win32con.MB_ICONWARNING)
    elif mode == "q":  # 疑问信息框
        win32api.MessageBox(0, con, title, win32con.MB_ICONQUESTION)
    elif mode == "t":  # 提示信息框
        win32api.MessageBox(0, con, title, win32con.MB_ICONASTERISK)
    elif mode == "y":  # 确认信息框
        win32api.MessageBox(0, con, title, win32con.MB_OKCANCEL)
    elif mode == "r":  # 重试信息框
        win32api.MessageBox(0, con, title, win32con.MB_RETRYCANCEL)
    elif mode == "ynb":  # 是否取消信息框
        win32api.MessageBox(0, con, title, win32con.MB_YESNOCANCEL)


# 弹出对话框参数 （标题，内容，模式）
def WinTitleUI(title, con, mode):
    if mode == "o":  # 提醒OK消息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_OK)
    elif mode == "yn":  # 是否信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_YESNO)
    elif mode == "s":  # 说明信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_HELP)
    elif mode == "!":  # 警告信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_ICONWARNING)
    elif mode == "q":  # 疑问信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_ICONQUESTION)
    elif mode == "t":  # 提示信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_ICONASTERISK)
    elif mode == "y":  # 确认信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_OKCANCEL)
    elif mode == "r":  # 重试信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_RETRYCANCEL)
    elif mode == "ynb":  # 是否取消信息框
        ctypes.WinDLL("user32.dll").MessageBoxW(0, con, title, win32con.MB_YESNOCANCEL)


def TLYoudao(text):
    url_youdao = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=' \
                 'http://www.youdao.com/'
    datatext = {'type': 'AUTO', 'doctype': 'json', 'xmlVersion': '1.8', 'keyfrom': 'fanyi.web', 'ue': 'UTF-8',
                'action': 'FY_BY_CLICKBUTTON', 'typoResult': 'true', 'i': text}
    data = urllib.parse.urlencode(datatext).encode('utf-8')
    response = urllib.request.urlopen(url_youdao, data)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    result = data['translateResult'][0][0]['tgt']
    return result


def DownLoad(save, url):
    response = requests.request("GET", url, stream=True, data=None, headers=None)
    requests.packages.urllib3.disable_warnings()
    save_path = save
    total_length = int(response.headers.get("Content-Length"))
    with open(save_path, 'wb') as f:
        widgets = ['Progress: ', progressbar.Percentage(), ' ',
                   progressbar.Bar(marker='#', left='[', right=']'),
                   ' ', progressbar.ETA(), ' ', progressbar.FileTransferSpeed()]
        pbar = progressbar.ProgressBar(widgets=widgets, maxval=total_length).start()
        for chunk in response.iter_content(chunk_size=1):
            if chunk:
                f.write(chunk)
                f.flush()
            pbar.update(len(chunk) + 1)
        pbar.finish()
