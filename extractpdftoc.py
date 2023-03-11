lines = []
prefix = 'BookmarkTitle: '
with open('ag_meta.txt', 'r') as inpf:
    for line in inpf:
        if line.startswith(prefix):
            lines.append(line[len(prefix):])
with open('ag_toc.txt', 'w') as outpf:
    outpf.write(''.join(lines))
