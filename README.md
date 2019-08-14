There's this game on FB where your friends draw something and you have to guess the word. However, most of the drawings will be terrible, and for your sanity, sometimes a brute-force approach is preferred.

<img src="https://github.com/lmtuan/Word-Permutator/blob/master/example.jpg" width="288" height="417">

There is an exploit to reduce the alphabet: By quitting the game, then return, a different set of characters will be generated. Repeat this several time, and we can find the exact characters needed for the word, by comparing the character sets.\
All that's left is to permute the alphabet, and find out which permutation is a word (or in some cases, 2 words). NLTK corpus works decently for this purpose.

How to run: `python3 solve_word.py` \
Then keep resetting the game and writing down the alphabets. Repeat enough time and only the correct characters remain. Press enter to brute force the answer.\
Requirement: nltk
