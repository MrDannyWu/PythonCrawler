# -*- mode: python ; coding: utf-8 -*-
import base64

import hashlib

import datetime

import wmi

from os import getcwd


def create_register_file():
    lianjie_fuhao = "woshilianjiefuhao"

    # 获得主板序列号
    bios_num = wmi.WMI().Win32_BaseBoard()[0].SerialNumber.strip()
    print(bios_num)

    # 获取当前时间字符串

    cur_time = datetime.datetime.now().strftime('%Y-%m-%d')

    # 填充最原始的字符串（流程图的第二步）

    t_str = '{}>>{cur_time}>>{cur_time}>>{cur_time}'.format(bios_num, cur_time=cur_time)

    # 先按照utg-8的编码类型编码为二进制

    content = t_str.encode('utf-8')

    # 生成base64字符串（第3步的前半部分）

    content = base64.b64encode(content)

    # 计算base64字串的MD5值（第3步的后半部分）

    b64_str = content.decode('utf-8')

    md5 = hashlib.md5()

    md5.update(content)

    md5_str = md5.hexdigest()

    # 将base64字串通过连接符号和MD5字串进行拼接（连接符号随便定义都行，目的是

    # 为了防止被人太顺利的破解我们加密方法）

    content = '{}{}{}'.format(b64_str, lianjie_fuhao, md5_str)

    # 再次进行base64编码

    content = content.encode('utf-8')

    content = base64.b64encode(content)

    # 写入到程序目录下

    baocun_lujing = "{}\\授权文件.txt".format(getcwd())

    with open(baocun_lujing, 'wb') as f:
        f.write(content)


if __name__ == "__main__":
    # 创建待授权文件

    create_register_file()

    print("待授权文件已创建")
