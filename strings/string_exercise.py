msg = raw_input('Write your message:')

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

new_string = ''

for char in msg:
    if char in lowercase:
        i = 0
        keepLooking = True 
        while keepLooking:
            if char == lowercase[i]:
                new_string += uppercase[i]
                keepLooking = False 
            i += 1
    else:
        new_string += char
print new_string



message = 'you shall NOT pass'

upcased = ''

for char in message:
    letter = char
    for i in range(len(lowercase)):
        lowerletter = lowercase[i]
        if lowerletter == char:
            letter = uppercase[i]
            break

    upcased = upcased + letter
print upcased





message = "storm the Castle!"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_string = ""
pre_letter = ' '
for char in message:
    if pre_letter == ' ':
        pre_letter = char
        for i in range(len(lowercase)):
            letter = lowercase[i]
            if letter == char:
                char = uppercase[i]
                pre_letter = char
                break
        new_string = new_string + char
    else:
        pre_letter = char
        new_string = new_string + char
print new_string

    
string = "this string is reversed"
new_string = ''

for i in range(len(string)):
    if i == 0:
        letter = string[-1]
    else:
        letter = string[-i-1]
    new_string += letter   

print new_string

string = "this string is reversed"
new_string = ''

msg = 'Given a pArAgrAph of tExt as a STring, prinT the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):'

input_char = ['AEGIOST']
char_replaced = ['4361057']

leetspeak = ''

for char in msg:
    letter = char
    for i in range(len(input_char)):
        changed = input_char[i]
        if changed == char:
            letter = char_replaced[i]
            break
    
    leetspeak = leetspeak + letter

print leetspeak

for char in msg:
    if char in lowercase:
        i = 0
        keepLooking = True 
        while keepLooking:
            if char == lowercase[i]:
                new_string += uppercase[i]
                keepLooking = False 
            i += 1
    else:
        new_string += char
print new_string

msg = 'my favorite food is tree'

long_vowel = ['o', 'e']
long_vowels_extend = ['ooooo', 'eeeee']

new_string = ''

for char in msg:
    if char in long_vowel:
        i = 0 
        keepLooking = True
        while keepLooking:
            if char == long_vowel[i]:
                new_string += long_vowels_extend[i]
                keepLooking = False
        i += 1
    else:
        new_string += char
print new_string    
            

msg = 'my favorite food is tree'

long_vowel = ['o', 'e']
long_vowels_extend = ['ooooo', 'eeeee']

new_string = ''

for char in msg:
    if char in long_vowel:
        for i in range(len(long_vowel)):
            if char == long_vowel[i]:
                char = long_vowels_extend[i]  
                new_string += char 
    else:
        new_string += char

print new_string    
    
word = "cheese"
long_word = ''
longs = ['e', 'o', 'a']
new_num = 2
pre_letter = ' '
for char in word:
    if  char == pre and char in longs:
        pre_letter = char
        long_word += char + char * new_num
    else:
        pre_letter = char
        long_word += char
print long_word
    
message = "storm the Castle!"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
new_string = ""
pre_letter = ' '
for char in message:
    if pre_letter == ' ':
        pre_letter = char
        for i in range(len(lowercase)):
            letter = lowercase[i]
            if letter == char:
                char = uppercase[i]
                pre_letter = char
                break
        new_string = new_string + char
    else:
        pre_letter = char
        new_string = new_string + char
print new_string

msg = raw_input('please enter a sentence:')

dict1 = {}
space = ' '

for word in msg:
    if word != ' ':
        print word