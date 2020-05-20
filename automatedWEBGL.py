name = input('what would you like to name the Web GL File? ')


f = open(name,'w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()