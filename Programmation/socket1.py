import socket
import math
import struct


host = 'challenge01.root-me.org'
port = 52002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    sentences = buff.decode().split('!')
    last_sentence = sentences[-1]
    sentence_split = last_sentence.split(' ')
    square_num = int(sentence_split[5])
    multiply_num = int(sentence_split[9])
    result = str((round(math.sqrt(square_num) * multiply_num, 2))) + '\n'
    s.sendall(result.encode())
    response = s.recv(512)
    print(response.decode())