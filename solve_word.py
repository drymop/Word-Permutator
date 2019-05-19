from collections import Counter
from itertools import permutations
import nltk

try:
    nltk.find('corpora/wordnet')
except LookupError:
    print('Downloading word dictionary...')
    nltk.download('wordnet')
    print('Download finished')
from nltk.corpus import wordnet

def unique_permutations(letters, length):
    previous = tuple()
    for p in permutations(sorted(letters), length):
        if p > previous:
            previous = p
            yield p

def list_intersect(list1, list2):
    return list((Counter(list1) & Counter(list2)).elements())

def find_words(letters, length):
    for perm in unique_permutations(letters, length):
        perm = ''.join(perm)
        words = perm.split()
        if all(wordnet.synsets(w) for w in words):
            yield perm
def main():
    allowed_letters = None
    print('Word length: ', end='')
    word_length = int(input())
    print('Enter list of allowed characters, then enter an empty line to guess:')
    while True:
        user_input = input().strip().lower()
        if user_input:
            new_allowed_letters = [c for c in user_input if c.isalpha()]
            if allowed_letters is None:
                allowed_letters = list(new_allowed_letters)
            else:
                allowed_letters = list_intersect(allowed_letters, new_allowed_letters)
            allowed_letters.sort()
            print('All letters: ' + ''.join(allowed_letters))
        else:
            found = 0
            spaces = 0
            while spaces <= 1:
                for word in find_words(allowed_letters, word_length):
                    found += 1
                    print(word)
                spaces += 1
                word_length += 1
                allowed_letters.append(' ')
                print('See all %d-word combinations? (y/n) ' % (spaces+1), end='')
                if input().strip().lower() != 'y':
                    break
            if not found:
                print('No word found')
            return

if __name__ == '__main__':
    main()

