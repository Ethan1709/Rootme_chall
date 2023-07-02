import socket
import base64
import zlib


host = 'challenge01.root-me.org'
port = 52022

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    print(buff.decode())
    sentences = buff.decode().split('!')
    last_sentence = sentences[-1]
    sentence_split = last_sentence.split(' ')
    word = sentence_split[3]
    res = base64.b64decode(word)
    print(res)
    res_uncompressed = zlib.decompress(res)
    print(res_uncompressed)
    byte_to_string = str(res_uncompressed, encoding='utf-8') + '\n'
    print(byte_to_string)
    s.sendall(byte_to_string.encode())


    buff = s.recv(512)
    print(buff.decode())
    sentences = buff.decode().split('?')
    last_sentence = sentences[0]
    sentence_split = last_sentence.split(' ')
    word = sentence_split[3]
    res = base64.b64decode(word)
    print(res)
    res_uncompressed = zlib.decompress(res)
    print(res_uncompressed)
    byte_to_string = str(res_uncompressed, encoding='utf-8') + '\n'
    print(byte_to_string)
    s.sendall(byte_to_string.encode())


    buff = s.recv(512)
    print(buff.decode())
    sentences = buff.decode().split('?')
    last_sentence = sentences[0]
    sentence_split = last_sentence.split(' ')
    word = sentence_split[3]
    res = base64.b64decode(word)
    print(res)
    res_uncompressed = zlib.decompress(res)
    print(res_uncompressed)
    byte_to_string = str(res_uncompressed, encoding='utf-8') + '\n'
    print(byte_to_string)
    s.sendall(byte_to_string.encode())


    buff = s.recv(512)
    print(buff.decode())
    sentences = buff.decode().split('?')
    last_sentence = sentences[0]
    sentence_split = last_sentence.split(' ')
    word = sentence_split[3]
    res = base64.b64decode(word)
    print(res)
    res_uncompressed = zlib.decompress(res)
    print(res_uncompressed)
    byte_to_string = str(res_uncompressed, encoding='utf-8') + '\n'
    print(byte_to_string)
    s.sendall(byte_to_string.encode())
    print(s.recv(512).decode())
