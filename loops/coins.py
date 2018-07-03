msg = raw_input('Do you want a coin? ')
coins = 0

while msg != 'no': 
    if msg == 'yes': 
        coins += 1
    print 'You have %i coins' % coins
    msg = raw_input('Do you want a coin?')
print 'Bye!'


