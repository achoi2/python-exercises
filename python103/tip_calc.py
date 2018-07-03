total = float(raw_input('Total bill amount:'))
tip = float(raw_input('Total tip amount:'))

level = tip / total 

if level >= .20:
    print 'good'
elif level >= .15:
    print 'fair'
else:
    print 'bad'

print level