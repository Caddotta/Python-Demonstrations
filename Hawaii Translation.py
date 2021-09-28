vowels_dictionary = {'a':'ah','e':'eh','i':'ee','o':'oh','u':'oo'}
pairs_dictionary = {
'ai':'eye','ae':'eye','ao':'ow','au':'ow',
'ei':'ay','eu':'eh-oo',
'iu':'ew',
'oi':'oyo','ou': 'ow',
'iw':'ee-v','ew':'eh-v',
'ui':'ooey',}
hawaiian_letters=['p','k','h','l','m','n','w','a','e','i','o','u',' ','\'']
def pronounce(word):
    word=word.lower()
    i=0
    result=[]
    while i < len(word):
        j=word[i]               
        if i < len(word)-1:     
            pair=j+word[i+1]    
            k=pairs_dictionary.get(pair)
            if k is None:       
                k=vowels_dictionary.get(j)
            else:
                i+=1
        else:
            k=vowels_dictionary.get(j)
        if (k is not None) and (i < len(word)-1):
            k=k+'-'
        result.append(k or j)
        i+=1
    return ''.join(result)
def letter_check(hawaiin_letters,word):
    for q in word:
        q=q.lower()
        if hawaiian_letters.count(q)==0:
            print(q, 'is a non-Hawaiian letter!')
            return False
        return True
def main():
    hawaiian_letters=['p','k','h','l','m','n','w','a','e','i','o','u',' ','\'']
    while True:
        word=input('Enter your Hawaiian word: ')
        if(letter_check(hawaiian_letters,word)):
            final_word=pronounce(word)
            final_word=final_word.upper()
            print(word+' is pronounced',final_word)
        confirm=input('Would you like to enter a new word? (Y/YES or N/NO): ')
        confirm=confirm.upper()
        if confirm[0]=='Y':
            main()
        elif confirm[0]=='N':
            print('You have ended the program')
            return False
main()
