import socket
import base64


host = 'challenge01.root-me.org'
port = 52023

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    sentences = buff.decode().split('!')
    last_sentence = sentences[-1]
    sentence_split = last_sentence.split(' ')
    print(sentence_split[3])
    res = base64.b64decode(sentence_split[3])
    new = str(res, encoding='utf-8') + '\n'
    print(new)
    s.sendall(new.encode())
    print(s.recv(512).decode())