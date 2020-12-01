def encrypt_text(text,key):
    cypher_text=''
    for i in range(len(text)):
        positionClef=i%len(key)
        decalage=ord(key[positionClef])
        NouvellePosition=(decalage+ord(text[i]))%240
        cypher_text+=chr(NouvellePosition)
    return cypher_text

def decrypt_text(cypher_text,key):
    text=''
    for i in range(len(cypher_text)):
        positionClef=i%len(key)
        decalage=ord(key[positionClef])
        NouvellePosition=(ord(cypher_text[i])-decalage)%240
        text+=chr(NouvellePosition)
    return text

def crack_key(cypher_text,len_key):
    key=''
    for i in range(len_key):
        j=0
        dico={} 
        most_repeted_time=0
        most_repeted_letter=''
        index=i+j*len_key
        while (index)<len(cypher_text):
            letter=cypher_text[index]
            dico[letter]= dico.get(letter,0) + 1
            if dico[letter]>most_repeted_time:
                most_repeted_letter=letter
            j+=1
            index=i+j*len_key
        key+=chr( ord(most_repeted_letter)-(ord('e')) % 240 )
    return key

def crack(cypher,max_length):
    for i in range(1,max_length):
        print("for a length of {} the key should be {}".format(i,crack_key(cypher,i)))


            
            

