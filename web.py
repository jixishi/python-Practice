# coding=utf-8
from bottle import route, run, request, static_file, error, hook, response


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
                import time
                sj = time.strftime('%Y-%m-%d %H:%M:%S')
                f = open("whitesq.txt", "a")
                f.write("申请时间->{}\nQQ：{},邮箱：{},Xbox ID：{},\n>-------------------------<\n".format(sj, qq, email, boxed))
                f.close()


@route('/cmd', method='POST')
def cmd():
    name = request.forms.get('name')
    passwd = request.forms.get('pass')
    mccmd = request.forms.get('cmd')
    if name == "jxs":
        if passwd == "be6":
            print(mccmd)
            print(name, passwd, mccmd)
    return "错误"


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


run(host='0.0.0.0', port=8080, debug=True)
