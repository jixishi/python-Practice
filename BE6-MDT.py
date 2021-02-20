# coding=utf-8
import ctypes
import json
import time
import jsonpath
import requests
import progressbar
import requests.packages.urllib3

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:24.0) Gecko/20100101 Firefox/24.0'
}
headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.69 '
                  'Safari/537.36 TheWorld 6 '
}
url1 = "https://api.github.com/repos/way-zer/ScriptAgent4MindustryExt/releases/latest"
url2 = "https://api.github.com/repos/Anuken/Mindustry/releases/latest"
assets1 = requests.get(url1, headers=headers1).json()['assets']
tag1 = requests.get(url1, headers=headers1).json()['tag_name']
name1 = jsonpath.jsonpath(assets1, "$..name")
zn = [i for i, x in enumerate(name1) if x.rfind('zip') != -1]
zipname = name1[zn]
jn = [i for i, x in enumerate(name1) if x.rfind('jar') != -1]
jarname = name1[jn]
down1 = jsonpath.jsonpath(assets1, "$..browser_download_url")
zd = [i for i, x in enumerate(down1) if x.rfind('zip') != -1]
zipdown = down1[zd]
jd = [i for i, x in enumerate(down1) if x.rfind('jar') != -1]
jardown = down1[jd]
updata1 = requests.get(url1, headers=headers1).json()['body']
ctypes.WinDLL("user32.dll").MessageBoxW(0, updata1, "插件更新提醒".decode("utf8"), 0)
time.sleep(3)
tag2 = requests.get(url2, headers=headers1).json()['tag_name']
assets2 = requests.get(url2, headers=headers2).json()['assets']
name2 = jsonpath.jsonpath(assets2, "$..name")
md = [i for i, x in enumerate(name2) if x.find('M') != -1]
mdtname = name2[md]
sd = [i for i, x in enumerate(name2) if x.find('server') != -1]
sername = name2[sd]
down2 = jsonpath.jsonpath(assets2, "$..browser_download_url")
md = [i for i, x in enumerate(down2) if x.find('M') != -1]
mdtdown = down2[md]
sd = [i for i, x in enumerate(down2) if x.find('server') != -1]
serdown = down2[sd]
updata2 = requests.get(url2, headers=headers2).json()['body']
ctypes.WinDLL("user32.dll").MessageBoxW(0, updata2, "核心更新提醒".decode("utf8"), 0)

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
