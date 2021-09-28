vowels=['a','e','i','o','u']
word=str(input('Enter a word: '))


def main(word):
    word=word.lower()
    while word != str('done'):
        find_first_vowel(word)
        print(str(pig_conversion(word)))
        print(str(reversal(word)))
        word=str(input('Enter a word: '))
    print('The program has stopped')
    
def find_first_vowel(word):
    word=word.lower()
    i=0
    while i<len(word):
        if word[i] in vowels:
            return i
        i+=1
    return len(word)-1

def pig_conversion(word):
    pig_word=[]
    i=find_first_vowel(word)
    if word[i]==word[0]:
        pig_word=str(word[1:]+word[0]+'way')
    elif word[i] not in vowels:
        pig_word=str(word)
    else:
        pig_word=str(word[i:]+word[0:i]+'ay')
    return pig_word

def reversal(word):
    reverse=''
    for k in range(1, len(word)+1):
        reverse += word[len(word)-k]
    return reverse
    
main(word)
