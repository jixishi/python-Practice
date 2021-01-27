# coding=utf-8
import sys
import thread
import json
import mc
import tool
import be6config
sys.path.append('.\ipy\BE6')

from flask import Flask, request, send_from_directory

be6 = Flask(__name__)


def load_plugin():
    print('[BE6CLOUD] BE6php已加载')
    print('[BE6CLOUD] ========================')
    print('[BE6CLOUD] 默认端口8080')
    print('[BE6CLOUD] 如有需要请更改配置文件')
    print('[BE6CLOUD] 更改远程后台配置')
    print('[BE6CLOUD] 后台地址')
    print('[BE6CLOUD] ip:8080')
    print('[BE6CLOUD] 配置26和27行')
    print (sys.path)
    thread.start_new_thread(be6, ())


def pfile():
    if not tool.IfDir('./plugins/BE6php'):
        tool.CreateDir('./plugins/BE6php')
        print('[INFO] BE6php正在创建文件夹...')
    else:
        print('[INFO] BE6php恭喜您，你的文件夹一切正常')
    if not tool.IfFile('./plugins/BE6php/whitesq.txt'):
        tool.WriteAllText('./plugins/BE6php/whitesq.txt', '')


@be6.route('/', methods=['GET'])
def index():
    return send_from_directory('./BE6', 'index.html')


@be6.route('/cmd', methods=['GET'])
def cmdget():
    return send_from_directory('./BE6', 'login.html')


@be6.route('/help', methods=['GET'])
def cs():
    return send_from_directory('./BE6', 'help.html')


# 只接受POST方法访问
@be6.route("/sq", methods=["POST"])
def sqpost():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断传入的json数据是否为空
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    qq = get_Data.get('contact_qq')
    email = get_Data.get('contact_email')
    xbox = get_Data.get('contact_id')
    # 对参数进行操作
    return_dict['result'] = sq(qq, email, xbox)

    return json.dumps(return_dict, ensure_ascii=False)


@be6.route("/cmd", methods=["POST"])
def cmdpost():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '执行成功', 'result': False}
    # 判断传入的json数据是否为空
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的参数
    get_Data = request.get_data()
    # 传入的参数为bytes类型，需要转化成json
    get_Data = json.loads(get_Data)
    name = get_Data.get('name')
    passwd = get_Data.get('pass')
    mccmd = get_Data.get('cmd')
    # 对参数进行操作
    return_dict['result'] = cmd(name, passwd, mccmd)

    return json.dumps(return_dict, ensure_ascii=False)


# 功能函数
def sq(qq, email, xbox):
    global sj
    if qq != "" and email != "" and xbox != "":
        mc.runcmd('whitelist add ' + xbox)
    import time
    sj = time.strftime('%Y-%m-%d %H:%M:%S')
    work = tool.WorkingPath()
    path = work + 'plugins/BE6php/whitesq.txt'
    f = open(path, "a")
    f.write("申请时间->{}\nQQ：{},邮箱：{},Xbox ID：{},\n>-------------------------<\n".format(sj, qq, email, xbox))
    f.close()
    result_str = "申请时间->%s QQ：%s,邮箱：%s,Xbox ID：%s" % (sj, qq, email, xbox)
    return result_str


def cmd(name, passwd, mccmd):
    if name == be6config.mm and passwd == be6config.wd:
        mc.runcmd(mccmd)
    import time
    times = time.strftime('%Y-%m-%d %H:%M:%S')
    result = "执行时间-> %s 命令-> %s" % (times, mccmd)
    return result


def be6():
    be6.run(host='0.0.0.0', port=be6config.port, debug=True)
