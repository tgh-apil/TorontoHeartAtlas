with open(filename, 'r+') as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith('<!--@SPF-JS-HEADER@-->'):   # find a pattern so that we can add next to that line
            lines[i] = lines[i]+a
        elif line.startswith('<p>hello</p>'):
            lines[i] = lines[i]+b
    f.truncate()
    f.seek(0)                                           # rewrite into the file
    for line in lines:
        f.write(line)