# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 08:57:45 2017

@author: Se

Run Test：
run AsciiImage.py 
"""

from PIL import Image
import argparse

# 命令行输入参数
parser = argparse.ArgumentParser()

parser.add_argument('--file', type = str, default = './mt.jpg', help = 'Input Image.')  # 输入文件
parser.add_argument('--output', type = str, default = './output.txt', help = 'Output TXT.')  # 输出文件
parser.add_argument('--width', type = int, default = 88, help = 'Width.')  # 输出字符画宽
parser.add_argument('--height', type = int, default = 33, help = 'Height.')  # 输出字符画高

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 示例：$ python ascii.py p.png -o out.txt --width 90 --height 45

ascii_char = list("@@WW##$$XXoo**""==::''..--  ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
