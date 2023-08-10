import sys
import re
import base64
import socket

CHARSET = "!#$%&()*+-0123456789;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ^_`abcdefghijklmnopqrstuvwxyz{|}"
CHARSET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+\-;<=>?@^_`{|}~"
TARGET  = bytes([v for v in range(33, 118)]).decode()

print('CHARST', CHARSET, len(CHARSET))
print('TARGET', TARGET, len(TARGET))

HOST = "challenge01.root-me.org"
PORT = 52017

def decode_is_base32(input_string):
    base32_pattern = r"^[A-Z2-7]+=*$"
    return re.match(base32_pattern, input_string) is not None

def decode_is_base64(input_string):
    base64_pattern = r"^[A-Za-z0-9+/]+=*$"
    return re.match(base64_pattern, input_string) is not None

def decode_is_hex(input_string):
    hex_pattern = r"^[0-9a-fA-F]+$"
    return re.match(hex_pattern, input_string) is not None

def decode_is_morse(line: str) -> bool:
    return set(line) == set("./-")

def decode_hex(line: str) -> str:
    return bytes.fromhex(line).decode()

def decode_base32(line: str) -> str:
    return base64.b32decode(line).decode()

def decode_base64(line: str) -> str:
    return base64.b64decode(line).decode()

def decode_morse(line: str) -> str:
    d = {
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

    return ''.join([d[v] for v in line.split('/')]).lower()

def shift(line: str, delta: int) -> str:
    r = ''

    charset = TARGET

    for c in line:
        i = CHARSET.index(c)
        i += delta
        i %= len(charset)
        r += charset[i]

    return r 

def decode_special(line: str) -> str:

    print([line])
    return input("REPLY:")

def parse_line(line: str):
    if not line.startswith('[>]'):
        return None

    return line.split("'")

def handle_line(line: str):
    decoded = None

    if decode_is_hex(line):
        print('hex', [line])
        decoded = decode_hex(line)
    elif decode_is_base32(line):
        print('base32', [line])
        decoded = decode_base32(line)
    elif decode_is_base64(line):
        print('base64', [line])
        decoded = decode_base64(line)
    elif decode_is_morse(line):
        print('morse', [line])
        decoded = decode_morse(line)
    else:
        print('i hate you', [line])
        decoded = base64.b85decode(line).decode()

    print('decoded', [decoded])

    return decoded

def handle_message(sock: socket.socket):
    buf = sock.recv(512)
 
    with open('output', 'a+') as file:
        file.write(buf.decode())
        file.write('\n')

    lines = buf.decode().splitlines()
    for line in lines:
        parsed = parse_line(line)
        if parsed is None:
            continue

        decoded = handle_line(parsed[1])
        if decoded is None:
            continue

        sock.sendall((decoded + '\n').encode())

def handle_end(sock: socket.socket):
    buf = sock.recv(512)
    print(buf.decode())

def handle(sock: socket.socket):
    for _ in range(100):
        handle_message(sock)

    handle_end(sock)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))

        handle(sock)

main()