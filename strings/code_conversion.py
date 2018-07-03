

# message = 'AAAAAAA'




# def leetspeak_function(msg):
#     leetspeak = ''
#     char_replaced = ['4361057']
#     for char in msg:
#         letter = char
#         input_char = ['AEGIOST']
#         if char in input_char:
#             index = input_char.index(char)
#             letter = char_replaced[index]
#         # for i in range(len(input_char)):           
#         #     changed = input_char[i]
#         #     if changed == char:
#         #         letter = char_replaced[i]
#         #     break 
        
#         leetspeak += letter
#     return leetspeak

# print leetspeak_function(message)



sentence_input = 'to be or not to be'


def create_word_list(sentence):
    words = []
    padded_sentence = sentence + ' '
    curr_word = ''
    for char in padded_sentence:
        if char == ' ':
            words.append(curr_word)
            curr_word = ''
        else:
            curr_word += char
    return words


def histogram(words): 
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1
    return word_count

words = create_word_list(sentence_input)
print histogram(words)



# def leet(paragraph):
#     subs = {'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}

#     new_paragraph = ''

#     for letter in paragraph:
#         upper = letter.upper()
#         if upper in subs:
#             letter = subs[upper]

#         new_paragraph += letter

#     return new_paragraph

# sentence = 'HELLO WORLD'
# print sentence         