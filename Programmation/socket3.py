import socket
import codecs


host = 'challenge01.root-me.org'
port = 52021

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    print(buff.decode())
    sentences = buff.decode().split('!')
    last_sentence = sentences[-1]
    sentence_split = last_sentence.split(' ')
    word = sentence_split[3]

    new = codecs.decode(word, 'rot_13')
    new2 = new[1:-2] + '\n'

    s.sendall(new2.encode())
    print(s.recv(512).decode())
