# coding=utf-8
import os


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
            output = file.read(1024*1024)
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
