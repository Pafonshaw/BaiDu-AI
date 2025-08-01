"""
逆向自百度AI(https://chat.baidu.com/)接口
含AI聊天和上传图片
注意: 该接口仅用于学习和研究, 请遵守百度AI的使用条款和政策。
该脚本仅用于学习交流, 请遵守法律, 禁止用于违法活动.
使用该脚本造成的一切后果与本人无关, 此脚本仅做技术分享
开源协议: MIT License
By @Pafonshaw
v2.0
2025/08/01
"""
"""
MIT License

Copyright (c) 2025 Pafonshaw

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import random
import json
import sys
import hmac
import os
import secrets
import bs4
import requests
from base64 import b64encode
from urllib.parse import quote
from time import time, gmtime, strftime
from hashlib import md5 as md5_hash, sha256 as sha256_hash


# 全局配置cookie
cookies = {
}
if cookies == {}:
    print("请先配置cookies")
    sys.exit(1)

drawfunc = [
    {
        "id": "drawSameStyle_shaonvtouxiang",
        "text": "少女头像",
        "input": "帮我画："
    },
    {
        "id": "drawSameStyle_zhigansheying",
        "text": "质感摄影",
        "input": "帮我画：图片风格为人像摄影"
    },
    {
        "id": "drawSameStyle_tuyachahua",
        "text": "涂鸦插画",
        "input": "帮我画：图片风格为扁平插画风"
    },
    {
        "id": "drawSameStyle_gaoqingrenxiang",
        "text": "高清人像",
        "input": "帮我画：图片风格为人像摄影"
    },
    {
        "id": "drawSameStyle_yuzhouxinghe",
        "text": "宇宙星河",
        "input": "帮我画：图片风格为写实风格"
    },
    {
        "id": "drawSameStyle_jijiazhanshi",
        "text": "机甲战士",
        "input": "帮我画：图片风格为动漫风格"
    },
    {
        "id": "drawSameStyle_2dhuihua",
        "text": "2D绘画",
        "input": "帮我画：图片风格为2D绘画，nabis风格"
    },
    {
        "id": "drawSameStyle_menghuanchahua",
        "text": "梦幻插画",
        "input": "帮我画："
    },
    {
        "id": "drawSameStyle_xieshimaozhan",
        "text": "写实毛毡",
        "input": "帮我画：图片风格为3D渲染"
    },
    {
        "id": "drawSameStyle_katongrenwu",
        "text": "卡通人物",
        "input": "帮我画：图片风格为3d皮克斯风格"
    },
    {
        "id": "drawSameStyle_shoubanmoxing",
        "text": "手办模型",
        "input": "帮我画：图片风格为POP MART 风"
    },
    {
        "id": "drawSameStyle_gexingrenxiang",
        "text": "个性人像",
        "input": "帮我画：图片风格为厚涂风格"
    },
    {
        "id": "drawSameStyle_shuimorenxiang",
        "text": "水墨人像",
        "input": "帮我画：图片风格为新工笔"
    },
    {
        "id": "drawSameStyle_gongbihuaniao",
        "text": "工笔花鸟",
        "input": "帮我画：图片风格为新工笔画"
    },
    {
        "id": "drawSameStyle_gufengtouxiang",
        "text": "古风头像",
        "input": "帮我画：图片风格为柔和的抽象画"
    },
    {
        "id": "drawSameStyle_guofengshanshui",
        "text": "国风山水",
        "input": "帮我画：图片风格为抽象绘画风格"
    },
    {
        "id": "drawSameStyle_yishuchahua",
        "text": "艺术插画",
        "input": "帮我画：图片风格为艺术插画"
    },
    {
        "id": "drawSameStyle_youhuafengge",
        "text": "油画风格",
        "input": "帮我画：图片风格为油画"
    },
    {
        "id": "drawSameStyle_gangfengtouxiang",
        "text": "港风头像",
        "input": "帮我画：图片风格为复古风格"
    },
    {
        "id": "drawSameStyle_sumiaoshougao",
        "text": "素描手稿",
        "input": "帮我画：图片风格为米开朗基罗"
    },
    {
        "id": "drawSameStyle_sailulufeng",
        "text": "赛璐璐风",
        "input": "帮我画：图片风格为赛璐璐"
    },
    {
        "id": "drawSameStyle_monaihuazuo",
        "text": "莫奈画作",
        "input": "帮我画：图片风格为莫奈风格"
    },
    {
        "id": "drawSameStyle_dongmantouxiang",
        "text": "动漫头像",
        "input": "帮我画：Redshift风格、动漫艺术、工笔、童话风、光影倒影的方式，现实而浪漫，Dansaekhwa风格"
    },
    {
        "id": "drawSameStyle_jingmeitouxiang",
        "text": "精美头像",
        "input": "帮我画：图片风格为Artgerm"
    },
    {
        "id": "drawSameStyle_qihuanjianzhu",
        "text": "奇幻建筑",
        "input": "帮我画：图片风格为路易斯·康福特·蒂凡尼风格"
    },
    {
        "id": "drawSameStyle_fangaofengge",
        "text": "梵高风格",
        "input": "帮我画：图片风格为梵高风"
    },
    {
        "id": "drawSameStyle_qingxinchahua",
        "text": "清新插画",
        "input": "帮我画：图片风格为浅水彩"
    },
    {
        "id": "drawSameStyle_qvweixiaoxiang",
        "text": "趣味肖像",
        "input": "帮我画：图片风格为梵高风"
    }
]

def get_token_lid():
    url = "https://chat.baidu.com/search?isShowHello=1"
    headers = {
        "Host": "chat.baidu.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Referer": "https://cn.bing.com/",
    }
    res = requests.get(url, headers=headers, cookies=cookies)
    soup = bs4.BeautifulSoup(res.text, "lxml")
    data = soup.find("script", attrs={"type":"application/json","name":"aiTabFrameBaseData"})
    data = json.loads(data.string)
    if not data.get("userInfo", {}).get("isUserLogin"):
        sys.exit("ck已过期")
    token = data["token"]
    lid = data["lid"]
    return token, lid

def md5(s):
    return md5_hash(s.encode()).hexdigest()
def get_tk(token, query, lid):
    p1 = token
    p2 = md5(query)
    p3 = str(int(time() * 1000))
    p4 = lid
    tk = b64encode(f"{p1}|{p2}|{p3}|{p4}".encode("utf-8")).decode("utf-8") + "-" + p4 + "-3"
    return tk

def generate_nanoid():
    """百度AI生成NanoID(随机数pro)"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    random_bytes = secrets.token_bytes(6)
    return ''.join(
        alphabet[byte % 63] 
        for byte in random_bytes
    )
def filetoken():
    """生成文件token, 其实就是随机字符串"""
    return str(int(time()*1000)) + generate_nanoid()

def generateAuthorizationHeaders(method: str, ak: str, sk: str, upload_token: str, uri: str, params: dict, timeout: int = 1800):
    """百度云鉴权认证(要长脑子了)"""
    x_bce_date = gmtime()
    x_bce_date: str = strftime('%Y-%m-%dT%H:%M:%SZ',x_bce_date)
    headers = {
        # 网站实际还验证了content-length, 经测试删去后仍然正常, 懒得区分PUT POST GET, 就删了
        "Host": "aisearch.bj.bcebos.com",
        "x-bce-security-token": upload_token,
        "x-bce-date": x_bce_date,
        "content-type": "image/jpeg"
    }
    signedHeaders = 'content-type;host;x-bce-date;x-bce-security-token'
    authStringPrefix = f"bce-auth-v1/{ak}/{x_bce_date}/{timeout}"
    CanonicalURI = quote(uri)
    CanonicalQueryString = []
    for k,v in params.items():
        CanonicalQueryString.append(f"{quote(k)}={quote(v)}")
    CanonicalQueryString.sort()
    CanonicalQueryString = "&".join(CanonicalQueryString)
    CanonicalHeaders = []
    for k,v in headers.items():
        CanonicalHeaders.append(f"{str(quote(k.lower(), safe=''))}:{str(quote(v.strip(), safe=''))}")
    CanonicalHeaders.sort()
    CanonicalHeaders = "\n".join(CanonicalHeaders)
    CanonicalRequest = method.upper() + "\n" + CanonicalURI + "\n" + CanonicalQueryString +"\n" + CanonicalHeaders
    signingKey = hmac.new(sk.encode('utf-8'),authStringPrefix.encode('utf-8'),sha256_hash)
    Signature = hmac.new((signingKey.hexdigest()).encode('utf-8'),CanonicalRequest.encode('utf-8'),sha256_hash)
    authorization = authStringPrefix + "/" +signedHeaders + "/" +Signature.hexdigest()
    headers.update({
        "Authorization": authorization,
        "Connection": "keep-alive",
        "Origin": "https://chat.baidu.com",
        "Referer": "https://chat.baidu.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "Accept": "*/*",
    })
    return headers

def chunk_file(file_path, chunk_size=1024*1024):
    # 百度AI仅允许上传10MB以下的文件, 文件上传时分块, 每块1MB
    MaxSize = 1024*1024*10
    file_size = os.path.getsize(file_path)
    if file_size > MaxSize:
        sys.exit("文件大小不能超过10MB")
    chunk_list = []
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_list.append(chunk)
    return chunk_list

def upload_img(user_token, lid):

    file_path = input("请输入图片文件路径: ")
    if not os.path.exists(file_path):
        sys.exit("文件不存在")
    file_type = file_path.split(".")[-1]
    if file_type not in ["jpg", "jpeg", "png", "webp", "bmp"]:
        sys.exit("文件格式错误")

    url = "https://chat.baidu.com/aichat/api/file/sts?tk=" + get_tk(user_token, "", lid)
    headers = {
        "Host": "chat.baidu.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "Accept": "*/*",
        "Referer": "https://chat.baidu.com/search?isShowHello=1&extParams=%7B%22out_enter_type%22%3A%22chat_url%22%2C%22enter_type%22%3A%22sidebar_dialog%22%7D",
    }
    res = requests.get(url, headers=headers, cookies=cookies)
    uploaddata = res.json()['data']

    ak: str = uploaddata['ak']
    sk: str = uploaddata['sk']
    upload_token: str = uploaddata['token']
    preFixPath: str = uploaddata['preFixPath']
    # bceUrl: str = uploaddata['bceUrl']
    # bucketName: str = uploaddata['bucketName']

    filetk = filetoken()
    uri = '/v1/' + preFixPath + filetk + '.' + file_type

    uploadUrl = 'https://aisearch.bj.bcebos.com' + uri

    params = {
        "uploads": "",
    }
    headers = generateAuthorizationHeaders("POST", ak, sk, upload_token, uri, params)
    res = requests.post(uploadUrl, headers=headers, params=params)
    resp = res.json()
    if code := resp.get("code"):
        sys.exit(code)
    uploadId = resp["uploadId"]


    params = {
        "partNumberMarker": "0",
        "uploadId": uploadId,
    }
    # 我也不知道这里GET一次干啥
    headers = generateAuthorizationHeaders("GET", ak, sk, upload_token, uri, params)
    res = requests.get(uploadUrl, headers=headers, params=params)

    etag = []
    chunk_list = chunk_file(file_path)
    for i, chunk in enumerate(chunk_list):
        params = {
            "partNumber": str(i+1),
            "uploadId": uploadId,
        }
        headers = generateAuthorizationHeaders("PUT", ak, sk, upload_token, uri, params)
        res = requests.put(uploadUrl, headers=headers, params=params, data=chunk)
        etag.append(eval(res.headers["ETag"]))

    params = {
        "uploadId": uploadId
    }
    payload = {
        "parts": [
            {
                "partNumber": i+1,
                "partSize": len(chunk_list[i]),
                "eTag": etag[i],
            }
            for i in range(len(etag))
        ]
    }
    headers = generateAuthorizationHeaders("POST", ak, sk, upload_token, uri, params)
    res = requests.post(uploadUrl, headers=headers, params=params, json=payload)
    resp = res.json()
    if code := resp.get("code"):
        sys.exit(code)
    
    url = "https://chat.baidu.com/aichat/api/file/upload?tk=" + get_tk(user_token, "", lid)

    headers = {
        "Host": "chat.baidu.com",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://chat.baidu.com",
        "Referer": "https://chat.baidu.com/search?isShowHello=1&extParams=%7B%22out_enter_type%22%3A%22chat_url%22%2C%22enter_type%22%3A%22sidebar_dialog%22%7D",
    }
    data = {
        'path': preFixPath + filetk + '.' + file_type,
        'size': os.path.getsize(file_path),
        'name': generate_nanoid() + '.' + file_type,    # 本地文件名, 伪造一个即可
        'id': b64encode((filetk+'.'+file_type).encode("utf-8")).decode("utf-8"),
        'type': 'image'
    }
    res = requests.post(url, headers=headers, cookies=cookies, json=data)
    resp = res.json()
    if (status:=resp.get("status")) != 0:
        sys.exit(status)
    return resp

print("""
逆向自百度AI(https://chat.baidu.com/)接口
含AI聊天和上传图片
注意: 该接口仅用于学习和研究, 请遵守百度AI的使用条款和政策。
该脚本仅用于学习交流, 请遵守法律, 禁止用于违法活动.
使用该脚本造成的一切后果与本人无关, 此脚本仅做技术分享
开源协议: MIT License
By @Pafonshaw
v2.0
2025/08/01
""")


user_token, lid = get_token_lid()


print('选择模式:\n'
      '1.常规模式(也能提出绘/识图要求)\n'
      '2.绘图模式(指定风格绘图)\n'
      '3.识图模式\n'
      '4.使用帮助')
mode = input('请输入模式: ')
if mode not in ['1', '2', '3', '4']:
    sys.exit("输入错误")
if mode == '1':
    query = input("问题: ") or "你好"
    sa = 'bkb'
elif mode == '2':
    print('选择绘图风格:')
    print('\n'.join([f"{i+1}. {v['text']}" for i, v in enumerate(drawfunc)]))
    num = input('请输入风格编号: ')
    if num not in [str(i+1) for i in range(len(drawfunc))]:
        sys.exit("输入错误")
    num = int(num)
    sa = 'functab_pic_' + drawfunc[num-1]['id']
    print('选择指令模式:\n'
        '1. 使用规范指令\n'
        '2. 自由发挥(如果指令不是以"帮我画："开头,不会触发AI绘图)')
    _mode = input('请输入指令模式: ')
    if _mode not in ['1', '2']:
        sys.exit("输入错误")
    if _mode == '1':
        query = drawfunc[num-1]['input']
        query += input(f'请补全指令: {query}')
    else:
        query = input('请输入绘图指令: ')
elif mode == '3':
    img = upload_img(user_token, lid)
    image_id = img["data"]["id"]
    sa = 'bkb_funcguide_read_2'
    query = input("请输入识图指令: ") or "进行图片识别"
else:
    sys.exit("使用帮助:\n"
        "使用前请先配置cookies\n"
        "常规模式是集成版, 你可以通过 "
        '"帮我对 图片链接 进行 图片识别" 来AI识图, 通过 '
        '"帮我画: 图片描述" 来AI绘图\n'
        "绘画模式可在代码层面传递风格参数\n"
        "若想直接识别本地图片, 需要使用识图模式来上传图片, 此外它还从代码层面传递识图参数")



# sessionId 是每个会话的唯一标识, 置空则开启新会话
sessionId = ""
if os.path.exists("./sessionId.txt"):
    with open("./sessionId.txt", encoding="utf-8") as f:
        sessionId = f.read().strip()
    if sessionId:
        print("发现缓存历史会话, 回车继续使用上次会话(续用上下文), 输入任意内容启用新会话(清除上下文)")
        if input(">>>"):
            sessionId = ""






def get_anti_ext(query):
    # 根据query长度模拟输入时长
    inputT = len(query)*1000 + random.randint(-10*len(query), len(query)*20+300) # 打字速度: 1s/字符+随机抖动
    # 模拟鼠标点击时长
    ck1 = random.randint(79, 246)
    # 模拟控件点击坐标
    ck9 = random.randint(281, 1025) # clientX
    ck10 = random.randint(847, 926) # clientY
    return {
        "inputT": inputT,
        "ck1": ck1,
        "ck9": ck9,
        "ck10": ck10,
    }
anti_ext = get_anti_ext(query)
str_anti_ext = json.dumps(anti_ext)

url = "https://chat.baidu.com/aichat/api/conversation"

headers = {
    "Host": "chat.baidu.com",
    "Connection": "keep-alive",
    "X-Chat-Message": f"query:{quote(query)},anti_ext:{quote(str_anti_ext)},enter_type:chat_url,re_rank:1,modelName:DeepSeek-R1",
    "isDeepseek": "1",
    "source": "pc_csaitab",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
    "accept": "text/event-stream",
    "Content-Type": "application/json",
    "landingPageSwitch": "",
    "Origin": "https://chat.baidu.com",
    "Referer": "https://chat.baidu.com/search?extParams=%7B%22enter_type%22%3A%22chat_url%22%7D&isShowHello=1",
}

data = {
    "message": {
        "inputMethod": "chat_search",
        "isRebuild": False,
        "content": {
            "query": "",
            "agentInfo": {
                "agent_id": [
                    ""
                ],
                "params": "{\"agt_rk\":1,\"agt_sess_cnt\":1}" if mode != '3' else ""
            },
            "qtype": 0,
            "aitab_ct": ""
        },
        "searchInfo": {
            "srcid": "",
            "order": "",
            "tplname": "",
            "dqaKey": "",
            "re_rank": "1",
            "ori_lid": sessionId,
            "sa": sa,
            "enter_type": "chat_url",
            "chatParams": {
                "setype": "csaitab",
                "chat_samples": "WISE_NEW_CSAITAB",
                "chat_token": get_tk(user_token, query, lid),
                "scene": ""
            } if mode != '3' else {
                "setype": "csaitab",
                "chat_token": get_tk(user_token, query, lid),
            },
            "blockCmpt": [],
            "usedModel": {
                "modelName": "DeepSeek-R1",
                "modelFunction": {
                    "internetSearch": "1",
                    "deepSearch": "0"
                }
            },
            "landingPageSwitch": "",
            "landingPage": "aitab",
            "out_enter_type": "" if mode != '3' else "sidebar_dialog",
            "showMindMap": False
        },
        "from": "",
        "source": "pc_csaitab",
        "query": [
            {
                "type": "TEXT",
                "data": {
                    "text": {
                        "query": query,
                        "text_type": ""
                    }
                }
            }
        ] if mode != '3' else [
            {
                "type": "IMAGE",
                "data": {
                "image": {
                    "image_id": image_id
                }
                }
            },
            {
                "type": "TEXT",
                "data": {
                "text": {
                    "query": query,
                    "text_type": ""
                }
                }
            }
        ],
    },
    "setype": "csaitab",
    "rank": 1   # 这(应该)是消息序号, 实测始终写 1 也可
}

if mode != '3':
    data['message']['anti_ext'] = anti_ext
    data['message']['searchInfo'].update({
        "isInnovate": 2,
        "applid": "",
        "a_lid": "",
    })
else:
    data['message']['searchInfo'].update({
        "lid": lid,
        "interaction_type": 2
    })

# 流式
res = requests.post(url, headers=headers, cookies=cookies, json=data, stream=True)
status = 0
for line in res.iter_lines():
    if line:
        res_line = line.decode("utf-8")
        with open('res.txt', 'a+', encoding='utf-8') as f:
            f.write(res_line+'\n'+'='*30+'\n')
        if not status and res_line.startswith("event:"):
            event = res_line[6:].strip()
            if event == "message":
                status = 1
        elif status and res_line.startswith("data:"):
            data = res_line[5:].strip()
            try:
                mdata = json.loads(data)
                component = mdata['data']['message']['content']['generator']['component']
                data = mdata['data']['message']['content']['generator']['data']
                if data.get('status') == 'finished':
                    sessionId = mdata.get('sessionId')
                    break
                if component == 'thinkingSteps':
                    if status != 2:
                        print('\n\n系统提示: AI思考中...\n')
                        status = 2
                    print(''.join(data['reasoningContentArr']), end='')
                elif component == 'markdown-yiyan':
                    if status != 3:
                        print('\n\n系统提示: AI回答中...\n')
                        status = 3
                    print(data['value'], end='')
                elif component == 'image-generate':
                    if status != 4:
                        print('\n\n系统提示: AI返图中...\n')
                        status = 4
                    print('\n'.join(i.get('originUrl', '???') for i in data.get('items', []) if i.get('loading') == 0))
                elif component == 'editor-workspace-viewer':
                    if status != 5:
                        print('\n\n系统提示: AI返回代码中...\n')
                        print(f"标题: {data['value']['title']}")
                        print(f"文件名: {data['value']['fileName']}")
                        print(f"语言: {data['value']['files'][0]['language']}")
                        status = 5
                    print(data['value']['updateFile']['content'], end='')
            except Exception:
                continue

if sessionId:
    with open("./sessionId.txt", "w", encoding="utf-8") as f:
        f.write(sessionId)

# print(res.request.headers)
# print(res.request.body)
