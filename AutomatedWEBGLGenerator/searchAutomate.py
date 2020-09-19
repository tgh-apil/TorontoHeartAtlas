a = """<style type="text/css">
table.tblin, td.tblin, th, td.alt
{
     border-color:#cc9;
     border-collapse:collapse;
     border-style:solid;
     border-width:1px;
     border-spacing:4px;
}
"""

b = """<p> it worked </p> 
"""

filename = raw_input('enter a filename you want to open: ')
print("'" + filename + "'")

with open("'" + filename + "'", 'r+') as f:
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