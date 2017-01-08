def disemvowel(word):
    word = list(word.lower())
    for vowel in ['a','e','i','o','u']:
        while True:
            try:
                word.remove(vowel)
                print("Removed {}".format(vowel))
            except ValueError:
                break
    word = "".join(word)
    print(word)
    return word

def disemvowel_v2(word):
    word = list(word)
    for letter in word:
        if letter.lower() in ['a','e','i','o','u']:
            word.remove(letter)
            print("Removed {}".format(letter))
    
    word = "".join(word)
    print(word)
    return word
        
t = 'hello'    
disemvowel(t)
disemvowel_v2(t)

t = t.upper()    
disemvowel(t)
disemvowel_v2(t)