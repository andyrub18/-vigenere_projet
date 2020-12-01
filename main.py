from Vigenere import encrypt_text,decrypt_text,crack_key,crack
#
maximum_key_length=10
text= 'Morisseauaeeeeeeeeeeeee'
key='abcd'
cypher=encrypt_text(text,key)
print(cypher)
print(decrypt_text(cypher,key))
print(crack_key(cypher,4))
print(crack(cypher,10))