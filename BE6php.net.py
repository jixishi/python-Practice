# coding=utf-8
import sys
import thread

import tool

sys.path.append('.\ipy\BE6')
from bottle import route, run, request, static_file, error, hook, response
import mc


def load_plugin():
    print('[BE6CLOUD] BE6php已加载')
    print('[BE6CLOUD] ========================')
    print('[BE6CLOUD] 默认端口8080')
    print('[BE6CLOUD] 如有需要请更改最后一行')
    print('[BE6CLOUD] 更改远程后台配置')
    print('[BE6CLOUD] 后台地址')
    print('[BE6CLOUD] ip:8080')
    print('[BE6CLOUD] 配置40和41行')
    print (sys.path)
    thread.start_new_thread(be6, ())


@route('/help')
def helps():
    return static_file('help.html', root='./BE6')


@route('/sq', method='POST')
def sq():
    qq = request.forms.get('contact_qq')
    email = request.forms.get('contact_email')
    boxed = request.forms.get('contact_id')
    print(qq, email, boxed)
    if qq != "":
        if email != "":
            if boxed != "":
                mc.runcmd('whitelist add ' + boxed)
                import time
                sj = time.strftime('%Y-%m-%d %H:%M:%S')
                work = tool.WorkingPath()
                path = work + 'plugins/BE6php/whitesq.txt'
                f = open(path, "a")
                f.write("申请时间->{}\nQQ：{},邮箱：{},Xbox ID：{},\n>-------------------------<\n".format(sj, qq, email, boxed))
                f.close()


# 修改用户名与密码
# 不要泄露
@route('/cmd', method='POST')
def cmd():
    name = request.forms.get('name')
    passwd = request.forms.get('pass')
    mccmd = request.forms.get('cmd')
    mm = "jxs"
    wd = "be6"
    if name == mm:
        if passwd == wd:
            mc.runcmd(mccmd)


def pfile():
    if not tool.IfDir('./plugins/BE6php'):
        tool.CreateDir('./plugins/BE6php')
        print('[INFO] BE6php正在创建文件夹...')
    else:
        print('[INFO] BE6php恭喜您，你的文件夹一切正常')
    if not tool.IfFile('./plugins/BE6php/whitesq.txt'):
        tool.WriteAllText('./plugins/BE6php/whitesq.txt', '')


@route('/cmd')
def login():
    return static_file('login.html', root='./BE6')


@route('/favicon.ico')
def login():
    return static_file('favicon.ico', root='./BE6')


@route('/')
def index():
    return static_file('index.html', root='./BE6')


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'


@error(404)
def error404():
    return "我找不到目标了，我发生错误了"


def be6():
    run(host='0.0.0.0', port=17849, debug=True)
