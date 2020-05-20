name = input('what would you like to name the file? ')


f = open(name,'w')

message = """<html>
<head></head>
<body><p>Hello World!</p></body>
</html>"""

f.write(message)
f.close()