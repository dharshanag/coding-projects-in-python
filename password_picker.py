import random
import string
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'fat', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'fluffy','white', 'proud', 'brave']
noun = ['apple','dino', 'ball', 'unicorn', 'dragon', 'panda','duck','giraffe', 'star', 'plant', 'banana', 'teacher', 'math', 'algebra']
print('Welcome to password picker! Here, you will be given secure passwprkds you can use for anything!\n')
while True:
    adjectives = random.choice(adjectives)
    noun = random.choice(noun)
    number = random.randrange(0,100)
    special_char = random.choice(string.punctuation)
    password = adjectives + noun + str(number) + special_char
    print('Your new password is: %s' % password + '\n')
    break
    