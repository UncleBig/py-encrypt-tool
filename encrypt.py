# -*- coding: utf-8 -*-

"""
@author: chaosxu
@time: 2020/12/22 04:40 下午
@desc: description
"""

"""
执行前提：
    Python安装
    pip install pycryptodome
    
TODO 从文件list中读取需加密文件，然后清理解密文件
项目使用流程：
    加密文件——>删除源文件——>打包发布
    服务启动解密文件-->load相关信息--->删除解密文件
"""

import os, struct
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from binascii import b2a_hex, a2b_hex
from Crypto.Random import get_random_bytes

encrypt_key = b'U0O8yZqJXmImbc6K'
cipher = AES.new(encrypt_key, AES.MODE_ECB)


# 字符串加密
def encrypt_text(text):
    if not isinstance(text, bytes):
        text = text.encode(encoding="utf-8")
    encrypted_text = b2a_hex(cipher.encrypt(pad(text, AES.block_size)))
    return encrypted_text.decode('utf8')


# 字符串解密
def decrypt_text(encrypted_text):
    if not isinstance(encrypted_text, bytes):
        encrypted_text = encrypted_text.encode('utf8')
    text = unpad(cipher.decrypt(a2b_hex(encrypted_text)), AES.block_size)
    return text.decode('utf8')


# 文件加密
def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            pos = 0
            while pos < filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                if pos == filesize:
                    chunk = pad(chunk, AES.block_size)
                outfile.write(encryptor.encrypt(chunk))


# 文件解密
def decrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.dec'
    with open(in_filename, 'rb') as infile:
        filesize = struct.unpack('<Q', infile.read(8))[0]
        iv = infile.read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            encrypted_filesize = os.path.getsize(in_filename)
            pos = 8 + 16  # the filesize and IV.
            while pos < encrypted_filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                chunk = encryptor.decrypt(chunk)
                if pos == encrypted_filesize:
                    chunk = unpad(chunk, AES.block_size)
                outfile.write(chunk)


if __name__ == '__main__':
    encry_text = encrypt_text('jarvis lab')
    decry_text = decrypt_text(encry_text)
    print(encry_text)
    print(decry_text)
    #encrypt_file(encrypt_key, "./test.txt")
    #decrypt_file(encrypt_key, "./test.txt.enc", "test_decrypt.txt")
    encrypt_file(encrypt_key, "./test.csv")
    decrypt_file(encrypt_key, "./test.csv.enc", "test_decrypt.csv")
