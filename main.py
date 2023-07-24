# Made on 19.5.2023 inspired by Codezilla from YouTube
# Many features were added by me

import requests

# Setting necessary vars
secret_word = 'hello'.lower()  # non-case sensitive. The word doesn't change in this case
guess = ''
guess_count = 0
number_of_guess = 3
out_of_guesses = False

# Print the definition before starting
print('Definition: ', requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{secret_word}')
      .json()[0]['meanings'][0]['definitions'][0]['definition'],
      'Hint: ', requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{secret_word}')
      .json()[0]['meanings'][0]['definitions'][0]['synonyms'])

# Loop that needs both guess (non-case sensitive) and out of guesses to be false. Every attempt adds 1 to guess count
while guess != secret_word and not out_of_guesses:
    if guess_count < number_of_guess:
        guess = input('Enter guess: ').lower()
        guess_count += 1
    else:
        out_of_guesses = True

# Results. if you're out_of_guesses (didn't guess correct), it'll print the word
if out_of_guesses:
    print('You lost', f'The word is "{secret_word}"' )
else:
    print('You won')
