# function to scramble code up and back by 13 characters

def scramble(text):
    output = ""
    for char in text:
        if ord(char) >= 65 and ord(char) <= 90:
            output += chr(((ord(char) - 64 + 13) % 26) + 64)
        elif ord(char) >= 97 and ord(char) <= 122:
            output += chr(((ord(char) - 96 + 13) % 26) + 96)
        else:
            output += char
    return output
