# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:34:27 2018

@author: Se
"""

from wxpy import *

"""
:param cache_path:
    * 设置当前会话的缓存路径，并开启缓存功能；为 `None` (默认) 则不开启缓存功能。
    * 开启缓存后可在短时间内避免重复扫码，缓存失效时会重新要求登陆。
    * 设为 `True` 时，使用默认的缓存路径 'wxpy.pkl'。
:param console_qr:
    * 在终端中显示登陆二维码，需要安装 pillow 模块 (`pip3 install pillow`)。
    * 可为整数(int)，表示二维码单元格的宽度，通常为 2 (当被设为 `True` 时，也将在内部当作 2)。
    * 也可为负数，表示以反色显示二维码，适用于浅底深字的命令行界面。
    * 例如: 在大部分 Linux 系统中可设为 `True` 或 2，而在 macOS Terminal 的默认白底配色中，应设为 -2。
:param qr_path: 保存二维码的路径
:param qr_callback: 获得二维码后的回调，可以用来定义二维码的处理方式，接收参数: uuid, status, qrcode
:param login_callback: 登陆成功后的回调，若不指定，将进行清屏操作，并删除二维码文件
:param logout_callback: 登出时的回调
"""
bot = Bot(cache_path=True )

my_friend = ensure_one(bot.search('刘生'))
# 发送文本
my_friend.send('好友查找成功!')

#tuling = Tuling(api_key='486270d731f64b758f2640355f880a2a')
#
## 使用图灵机器人自动与指定好友聊天
#@bot.register(my_friend)
#def reply_my_friend(msg):
#    tuling.do_reply(msg)

xiaoi = XiaoI('tpmOGmlUaIM4', 'aMuhE2YTCWKxblrMEXQG')

# 使用小 i 机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    xiaoi.do_reply(msg)

bot.join()

#embed()






