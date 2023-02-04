# Magic 8 Ball program

import random

question = input('Question: ')

num = random.randint(0,8)

if num == 0:
    answer = 'Yes - definitely.'
elif num == 1:
    answer = 'It is decidedly so.'
elif num == 2:
    answer = 'Without a doubt.'
elif num == 3:
    answer = 'Reply hazy, try again.'
elif num == 4:
    answer = 'Ask again later.'
elif num == 5:
    answer = 'Better not tell you now.'
elif num == 6:
    answer = 'My sources say no.'
elif num == 7:
    answer = 'Outlook not so good.'
elif num == 8:
    answer = 'Very doubtful.'
else:
    asnwer = error

print('Question:     ' + question)
print('Magic 8 Ball: ' + answer)
