from Vigenere import encrypt_text,decrypt_text,crack_key,crack
maximum_key_length=10
with open('vigenere.txt', 'r') as file:
    data = file.read()
key='abcd'
cypher=encrypt_text(data,key)
print(cypher)
print(decrypt_text(cypher,key))
print(crack(cypher,10))

