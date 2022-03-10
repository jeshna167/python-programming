import random
name = input("what is your name?")
print('hello,', name)
words=['hello','hi', 'lion','girrafe', 'birds','donkey', 'monkey', 'lolipop','missisippi', 'missouri', 'greenland', 'india', 'russia','fish','goat','gate', 'war', 'omicron', 'corona', 'television', 'computer', 'youtube', 'network', 'blind carbon copy', 'office','puppy', 'kitten', 'mitten', 'keyboard', 'emoji','campk12', 'misic','trouble', 'pencil', 'water', 'sister', 'naughty', 'cheetah', 'river', 'waterfall', 'gate', 'rainbow', 'summer', 'winter', 'wool', 'cotton', 'silk', 'machines', 'cycle', 'band', 'chair', 'pizza', 'cheese', 'milk', 'burger', 'microsoft', 'power', 'name', 'jam', 'bread', 'chips', 'tissue', 'nose', 'ears','eyes','books', 'sparrow', 'swing', 'slide', 'see-saw', 'plants', 'windows', 'doors', 'photos', 'paint', 'google', 'googol', 'chrome', 'couch', 'piano', 'fairy', 'fairy tales', 'english', 'desserts', 'grassland', 'pairies', 'stepes', 'thar dessert', 'congo', 'republic', 'deserts','indian ocean', 'pacific ocean', 'arctic ocean', 'antartic ocean', 'atlantic ocean', 'canada' ]
word=random.choice(words)
#print(word)
print("Guess the letters of the word")
guesses=""#going to contain all the letters that user has guessed
turns=10
while (turns>0) :
    fail=0
    for a in word:
        if a in guesses:
            print(a)
        else :
           print('_')
           fail=fail+1
           #print(fail)
    if fail==0:
        print("you have won, congratulations!!")
        print("the correct word is ", word)
        break
    guess=input('guess a character any: ')
    guesses=guesses+guess
    if guess not in word:
        turns=turns-1
        print("wrong")
        print("number of turns left= ",turns)
        if turns==0:
            print('better luck next time')
            print('the correct word =', word)