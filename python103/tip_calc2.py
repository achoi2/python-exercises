total = float(raw_input('Total bill amount:'))
tip = float(raw_input('Total tip amount:'))

total_amount = total + tip

print 'Your total amount is %f' % total_amount

level = tip / total

if level >= .20:
    print 'good'
elif level >= .15:
    print 'fair'
else:
    print 'bad'

print level

split = float(raw_input('How many ways?'))

amount_per_person = total_amount / split

print  'Your total amount is %f' % amount_per_person