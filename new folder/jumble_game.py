import random
'''Create a Word Jumble game whereby the computer selects a random word from a list, jumbles it up,
    and the user has to guess the word.'''

'''Improve "Word Jumble" so that each 
    word is paired with a hint. The player
    should be able to see the hint if he or she is stuck. Add a scoring
    system that rewards players who solve a jumble without asking for the hint'''

'''The Word Jumble Game Pseudocode'''
# create an array of words
# randomly choose a word
# jumble the word
# have the user guess what the word is

# create an array of possible words

possible_words = ['telephone', 'imperial', 'sql',
                  'statistics', 'machine']

# possible hints
hint_telephone = "Make a phone call."
hint_imperial = "University in London."
hint_sql = "Database management."
hint_statistics = "Branch of mathematics."
hint_machine = "Will take over the world."

# pick a random word
index_words = random.randint(0, len(possible_words)-1)
random_word = possible_words[index_words]

# for reference
word_static = random_word

# jumble the word

# create an empty string to store jumbled word
buffer = ""

for i in range(0, len(random_word)):
    # create a random number generator to index characters of selected word
    index_letter = random.randint(0, len(random_word) - 1)

    # store random letter in empty string
    buffer += random_word[index_letter]

    # "remove" letter in random_word by storing first half, and second half of word
    random_word = random_word[:index_letter] + random_word[(index_letter + 1):]

# hint counter
hint_counter = 0

# prompt user until the guess is correct
while True:

    # have user guess random word
    guess = input('The jumbled word is: %s. Take a guess. Enter your guess here:' % buffer)

    if guess.lower() == word_static:
        print("\nCongratulations! You won! Fin.")
        if hint_counter == 0:
            print("\nNo hints used. Here is your prize -> :D ")
        break

    # prompt for hint
    hint_answer = input("\nWrong. Do you want a hint? (Y/N): ")

    if hint_answer.lower() == "y":
        # update hint counter
        hint_counter += 1

        print("\n\nNumber of hints used: %s" % hint_counter, "\n")

        if word_static == "telephone":
            print(hint_telephone)
        elif word_static == "imperial":
            print(hint_imperial)
        elif word_static == "sql":
            print(hint_sql)
        elif word_static == "statistics":
            print(hint_statistics)
        else:
            print("\n\n", hint_machine)
