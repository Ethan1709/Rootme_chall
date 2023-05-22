with open("ch19.txt", "r") as file:
    text = file.read()

output = []
for line in text.splitlines():
    s = ''
    for c in reversed(line):
        if c in ' \t':
            s += c
        else:
            break
    output.append(''.join(reversed(s)))
with open("output.txt", "w") as file:
    file.write("\n".join(output))
