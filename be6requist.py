# coding=utf-8

from fake_useragent import UserAgent  # 下载：pip install

ua = UserAgent()  # 实例化，需要联网但是网站不太稳定-可能耗时会长一些

headers = {
    'User-Agent': ua.random  # 伪装
}
import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").json()


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def getHtml(path):
    # ....
    retry_count = 5
    proxy = get_proxy().get("proxy")
    while retry_count > 0:
        try:
            html = requests.get(path, headers=headers, proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 删除代理池中代理
    delete_proxy(proxy)
