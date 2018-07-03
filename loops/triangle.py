height = int(raw_input('Height?'))
i = 1
spaces = (height * 2) - 2
j = spaces/2   

while i <= height:
while j >= 0:
    print (j * ' ') + (i * '*') + (j * ' ')
    j -= 1
    i += 2