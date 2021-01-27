import requests
import time

def get_star(url):
    html = requests.get(url).json()['data']
    global mid
    global follower
    mid  = html['mid']
    follower = html['follower']
    following = html['following']
    print("uid：{}，粉丝数：{}，关注数：{}".format(mid,follower,following))
    print("-"*20)

def get_userdata(url):
    jsondata = requests.get(url).json()['data']
    global name
    name = jsondata['name']
    sex = jsondata['sex']
    level = jsondata['level']
    birthday = jsondata['birthday']
    coins = jsondata['coins']
    print("名字是：{}  性别是：{}  等级是：{}  生日是：{}  硬币数目：{}".format(name,sex,level,birthday,coins))



def main():
    time.sleep(0.5)
    number = 1
    f = open("bzfs.txt" , "a")
    for i in range(1, 66):
        time.sleep(0.5)
        url = "https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp".format(i)
        get_userdata(url)
        url2 = "https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp".format(i)
        get_star(url2)
        if(follower >= 100000):
            f.write("uid：{},粉丝数：{}\n".format(mid,follower))
            print("第{}个up粉丝数为{}".format(number,follower))
            number += 1
    f.close()
    print("总共有：{}个up有10w以上的粉丝".follower(number))

if __name__ == '__main__':
    main()