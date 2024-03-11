def check_guess(guess,answer):
    global score   
    if guess == answer:
        print('Correct!')
        score = score + 1
    else:
        print('Sorry, that is not correct, if you would like to try again, please start the program again!')
score = 0
print('Guess the animal!')
guess1 = input('Which bear lives at the North pole?')
check_guess(guess1, 'polar bear')
guess2 = input('Which is the fastest land animal?')
check_guess(guess2,'cheetah')
guess3 = input('Which is the largest animal on Earth?')
check_guess(guess3,'blue whale')
guess4 = input('Which animal can change its color to match its surroundings?')
check_guess(guess4,'chameleon')
guess5 = input('What is the only mammal capable of true flight?')
check_guess(guess5,'bat')
print('That is all for today. Thank you for playing the Animal Trivia Quiz! Your final score is '+str(score) +'/5')