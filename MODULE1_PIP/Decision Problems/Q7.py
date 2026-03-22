# Check whether a character is vowel or consonant
ch = input()
if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")