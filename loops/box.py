width = int(raw_input('what is the width?'))
height = int(raw_input('what is the height?'))

i = 0

while i < height:
    if i == 0 or i == height - 1:
        print ('#' * width)
        i += 1
    else:
        print('#' +(' ' * (width - 2)) + '#')
        i += 1    