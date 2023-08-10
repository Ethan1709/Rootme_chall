import socket
import base64
import binascii
import re

def is_base32_encoded(input_string):
    base32_pattern = r"^[A-Z2-7]+=*$"
    return re.match(base32_pattern, input_string) is not None

def is_base64_encoded(input_string):
    base64_pattern = r"^[A-Za-z0-9+/]+=*$"
    return re.match(base64_pattern, input_string) is not None

def is_hex_encoded(input_string):
    hex_pattern = r"^[0-9a-fA-F]+$"
    return re.match(hex_pattern, input_string) is not None

def decode_morse(code):
    morse_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '/': ' ',
        '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8',
        '----.': '9', '-----': '0'
    }

    decoded = []
    words = code.split('/')
    for word in words:
        letters = word.split('/')
        for letter in letters:
            if letter in morse_dict:
                decoded.append(morse_dict[letter])
            else:
                decoded.append('?')

    return ''.join(decoded)


host = 'challenge01.root-me.org'
port = 52017

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    buff = s.recv(512)
    print(buff.decode())
    for i in range(0, 100):
        if i == 0:
            line = buff.decode().split('>')
            code_to_decode = line[1].split(' ')
            code_to_decode = code_to_decode[5][1:-3]
        else:
            code_to_decode = new_code.split(' ')
            code_to_decode = code_to_decode[5][1:-4]
                
        if is_hex_encoded(code_to_decode):
            if len(code_to_decode) % 2 != 0:
                code_to_decode = '0' + code_to_decode
            code_to_decode = bytes.fromhex(code_to_decode).decode('utf-8') + '\n'
            print(code_to_decode)
            s.sendall(code_to_decode.encode())
            new_code = s.recv(512).decode()
            print(new_code)
        elif is_base32_encoded(code_to_decode):
            code_to_decode = base64.b32decode(code_to_decode)
            code_to_decode = str(code_to_decode, encoding='utf-8') + '\n'
            print(code_to_decode)
            s.sendall(code_to_decode.encode())
            new_code = s.recv(512).decode()
            print(new_code)
        elif is_base64_encoded(code_to_decode):
            code_to_decode = base64.b64decode(code_to_decode)
            code_to_decode = str(code_to_decode, encoding='utf-8') + '\n'
            print(code_to_decode)
            s.sendall(code_to_decode.encode())
            new_code = s.recv(512).decode()
            print(new_code)
        else:
            code_to_decode = decode_morse(code_to_decode) + '\n'
            code_to_decode = code_to_decode.lower()
            print(code_to_decode)
            s.sendall(code_to_decode.encode())
            new_code = s.recv(512).decode()
            print(new_code)