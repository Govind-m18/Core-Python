# Check whether an alphabet is a vowel or consonant

# vowel = A,E,I,O,U,a,e,i,o,u 
# If it is not a vowel, it is a consonant

ch = input("Enter a alphabet :")

if ch in "aeiouAeiou":
    print("Alphabet is vowel")

else:
    print("Alphabet is consonant")

