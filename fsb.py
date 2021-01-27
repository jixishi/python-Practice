import requests
import time
import random


def get_star(url):
    global mid
    global follower
    global name
    global code
    code = requests.get(url).json()['code']
    if (code == 0):
        html = requests.get(url).json()['data']['card']
        mid = html['mid']
        name = html['name']
        follower = html['fans']
        following = html['friend']
        print("uid：{}，粉丝数：{}，关注数：{}".format(mid, follower, following))


def main():
    number = 1
    f = open("10w.txt", "a")
    for i in range(6666666, 355553533):

        time.sleep(3)
        url = "http://api.bilibili.com/x/web-interface/card?mid={}&jsonp=jsonp".format(
            i)
        get_star(url)
        if (code == 0):
            if (follower >= 100000):
                f.write("uid：{},粉丝数：{},名字：{}\n".format(mid, follower, name))
                print("第{}个up粉丝数为{}".format(number, follower))
                number += 1
    f.close()
    print("总共有：{}个up有10w以上的粉丝".follower(number))
    time.sleep(sleeptime)


if __name__ == '__main__':
    main()