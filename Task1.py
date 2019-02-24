import random
words = ['imagination', 'pleasure', 'apple', 'homework']
word = random.choice(words)
lst_word = list(word)
lst_guessed = ['*']*len(word)
guessed_letters = []
mistakes = 0
while '*' in lst_guessed and mistakes != 5:
    inpt = str(input('Guess a letter:\n'))
    if inpt in lst_word and inpt not in guessed_letters:
        guessed_letters.append(inpt)
        print('Hit!\n')
        for i in range(len(word)):
            if lst_word[i] == inpt:
                lst_guessed[i] = inpt
        print('The word: ', *lst_guessed, '\n', sep='')
        if '*' not in lst_guessed:
            print('You won!')
    else:
        mistakes += 1
        print('Missed, mistake ', mistakes, ' out of 5\n')
        print('The word: ', *lst_guessed, '\n', sep='')
        if mistakes == 5:
            print('You lost!')