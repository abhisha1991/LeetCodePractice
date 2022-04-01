# asked in Gemini first round
# design an encryption/decryption function that takes in a message (upper/lower case letters)
# it also takes in a common key, and then encrypts/decrypts that message with the following logic
'''
message = "Abc"

key = "123", output of encryption: "Bdf"
key = "12", output of encryption: "Bdd"
key = "1", output of encryption: "Bcd"

Basically, you have to take a character, take a corresponding key number and shift the ascii value of that character by the key number
So if key = "123", A gets shifted by 1, b gets shifted by 2, c gets shifted by 3
and if key = "12", A gets shifted by 1, b gets shifted 2, c gets shifted by 1 (notice that we "wrap around" the key if we're out of key characters)

Decryption is the opposite of encryption, given key 123 and output Bdf ==> we get bac "Abc"
'''

def validateKey(key):
    if type(key) == int:
        if key < 0:
            raise ValueError("negative key")
        key = str(key)
        if len(key) == 0:
            raise ValueError("empty key")
    return key

def decrypt(message, key):
    key = validateKey(key)    

    if message == "":
        return ""
    i = 0
    output = ""
    for m in range(len(message)):
        k = key[i]
        i +=1
        # wrap around key
        if i == len(key):
            i = 0

        ascii = ord(message[m])
        ascii -= int(k)
        output += chr(ascii)
    return output

def encrypt(message, key):
    key = validateKey(key)

    if message == "":
        return ""
    i = 0
    output = ""
    for m in range(len(message)):
        k = key[i]
        i +=1
        # wrap around key
        if i == len(key):
            i = 0

        ascii = ord(message[m])
        ascii += int(k)
        output += chr(ascii)
    return output

# example 
enc = encrypt("Open", "123")
print(enc)
dec = decrypt(enc, "123")
print(dec)
assert("Open" == dec)

# example 
enc = encrypt("Open", 12)
print(enc)
dec = decrypt(enc, 12)
print(dec)
assert("Open" == dec)

# example 
enc = encrypt("test", "1")
print(enc)
dec = decrypt(enc, "1")
print(dec)
assert("test" == dec)

# example 
enc = encrypt("Abhinav", 12)
print(enc)
dec = decrypt(enc, 12)
print(dec)
assert("Abhinav" == dec)

# example
enc = encrypt("Abhinav Sharma", 129)
print(enc)
dec = decrypt(enc, 129)
print(dec)
assert("Abhinav Sharma" == dec)