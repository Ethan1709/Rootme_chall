with open("ch19.txt", "r") as file:
    text = file.read()

output = []
for line in text.splitlines():
    # outline = ''
    # for c in line:
    #     if c in ' \t':
    #         outline += c
    # output.append(outline)

    # output.append(' ' * line.count(' '))

    s = ''
    for c in reversed(line):
        if c in ' \t':
            s += c
        else:
            break
    output.append(''.join(reversed(s)))
with open("output.txt", "w") as file:
    file.write("\n".join(output))
