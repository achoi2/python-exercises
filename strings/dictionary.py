# ramit = {
#     'name': 'Ramit',
#     'email': 'ramit@gmail.com',
#     'interests': ['movies', 'tennis'],
#     'friends': [{
#         'name': 'Jasmine',
#         'email': 'jasmine@yahoo.com',
#         'interests': ['photography', 'tennis']
#     }, {
#         'name': 'Jan',
#         'email': 'jan@hotmail.com',
#         'interests': ['movies', 'TV']
#     }]
# }
# ramit['email']
# ramit['interests'][0]
# ramit['friends'][0]['email']
# print ramit['friends'][1]['interests'][1]



# msg = raw_input('msg:')

# integer = 0 

# letter_histogram = {}

# for char in msg:
#     letter_histogram[char] = 1
#     for i in range(len(msg)):
#         if char == msg[i]:
#             integer += 1
#             letter_histogram[char] = integer

# print letter_histogram


# sentence = raw_input("Please enter a sentence: ")
# dictionary = {}
# space = " "
# words = sentence.split(" ")

# for word in words:
#     if word not in dictionary:
#         dictionary[word] = 1
#     else:
#         dictionary[word] += 1
        
# print dictionary

# sentence_input = 'this is a sentence is is is.'#raw_input('Riddle me a sentance please: ')
# sentence = sentence_input.lower()
# words = []
# wordlower = ''
# d = {}


 
# for char in range(len(sentence)):
#     if char == 0:
#         wordlower += sentence[char]
#         if sentence[char + 1] == ' ':
#             words.append(wordlower)
#             wordlower = ''
#     elif sentence[char] != ' ': 
#         wordlower += sentence[char]
#         if sentence[char] == '.':
#             break
#         elif sentence[char + 1] == ' ' or sentence[char + 1] == '.':
#             words.append(wordlower)
#             wordlower = ''
#     elif sentence[char] == '.':
#         break
        
# print words

# for item in words: 
#     if item not in d:
#         d[item] = 1
#     elif item in d: 
#         d[item] += 1
# print d


# sentence_input = raw_input("Please enter a sentence: ")
# dictionary = {}
# space = " "
# words = sentence.split(" ")
    
#     for char in sentence_input:


# msg = "sentence"
# dict1 = {}
# wordslower = ''


# for char in range(len(msg)):
#     if char == 0:




# sentence = raw_input("Please enter a sentence: ")
# dictionary = {}
# space = " "
# words = sentence.split(" ")

# for word in words:
#     if word not in dictionary:
#         dictionary[word] = 1
#     else:
#         dictionary[word] += 1
        
# print dictionary
# msg_input = raw_input("Sentence? ")
# dict1 = {}
# word = ''
# list2 = ['!', '.', '?']
# msg = msg_input.lower()

# for char in range(len(msg)):
#     if char == 0:
#         word += msg[char]
#         if msg[char + 1] == ' ':
#             dict1[word]
#             word = ''
#     elif msg[char] != ' ' or char == len(msg):
#         word += msg[char]
#         if msg[char + 1] == ' ' or char = len(msg):
#             dict1[word]
#             word = ''
#     elif msg[char] in list2:
#         break

# print dict1

sentence = 'to be or not to be'

padded_sentence = sentence + ' '

words = []
curr_word = ''


for char in padded_sentence:
    if char == ' ':
        words.append(curr_word)
        curr_word = ''
    else:
        curr_word += char

words.append(curr_word)

# words = ['to', 'be', 'or', 'not', 'to', 'be']

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else: 
        word_count[word] = 1

print word_count