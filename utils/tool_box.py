# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File:           tool_box.py
   Description:
   Author:        
   Create Date:    2021/01/18
-------------------------------------------------
   Modify:
                   2021/01/18:
-------------------------------------------------
"""
import os
import zipfile
from Crypto.Cipher import AES
import base64


def aes_encrypt(key, data):
    """
    AES的ECB模式加密方法
    :param key: 密钥
    :param data: 被加密字符串（明文）
    :return: 密文
    """

    # Bytes
    BLOCK_SIZE = 16

    # 字符串补位
    pad = lambda s:s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

    key = key.encode('utf8')
    data = pad(data)
    cipher = AES.new(key, AES.MODE_ECB)
    # 加密后得到的是bytes类型的数据，使用Base64进行编码,返回byte字符串
    result = cipher.encrypt(data.encode())
    encode_str = base64.b64encode(result)
    enc_text = encode_str.decode('utf8')
    return enc_text


def aes_decrypt(key, data):
    """
    AES解密
    :param key: 密钥
    :param data: 加密后的数据（密文
    :return: 明文
    """

    # 去补位
    unpad = lambda s: s[:-ord(s[len(s) - 1:])]

    key = key.encode('utf8')
    data = base64.b64decode(data)
    cipher = AES.new(key, AES.MODE_ECB)

    text_decrypted = unpad(cipher.decrypt(data))
    text_decrypted = text_decrypted.decode('utf8')
    return text_decrypted

def compress_zip(o_attach_filename):
    """
    将附件压缩，并返回压缩后文件的路径
    :param o_attach_filename: 原来的文件
    :return: 压缩后的文件名
    """
    n_attach_filename = os.path.splitext(o_attach_filename)[0] + '.zip'
    f = zipfile.ZipFile(n_attach_filename, 'w', zipfile.ZIP_DEFLATED)
    f.write(o_attach_filename, os.path.basename(o_attach_filename))
    f.close()
    return n_attach_filename

def check_and_adjust_file_name(file_name):
    if file_name is None:
        import tempfile
        return tempfile.NamedTemporaryFile().name

    file_name = file_name.replace(' ', '_')
    file_name = file_name.replace('\\', '_')
    file_name = file_name.replace('/', '_')
    file_name = file_name.replace(':', '_')
    file_name = file_name.replace('*', '_')
    file_name = file_name.replace('?', '_')
    file_name = file_name.replace('”', '_')
    file_name = file_name.replace('<', '_')
    file_name = file_name.replace('>', '_')
    file_name = file_name.replace('|', '_')
    return file_name


def count_time(func):
    """
    函数运行计时器
    :param func:
    :return:
    """
    import time

    def int_time(*args, **kwargs):
        start_time = time.time()  # 程序开始时间
        func(*args, **kwargs)
        over_time = time.time()   # 程序结束时间
        total_time = over_time - start_time
        print('程序共计%s秒' % total_time)
        return total_time

    return int_time

@count_time
def test_dec(a):
    import time
    time.sleep(3)
    print(a)


if __name__ == '__main__':
    a = test_dec(1)
    print(a)
    # get_all_task()
    # from config.config import KEY

