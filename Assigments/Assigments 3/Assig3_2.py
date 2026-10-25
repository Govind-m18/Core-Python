# Write a program to input any alphabet and check whether it is vowel or consonant.

alphabet = input("Enter a alphabet :")

# if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
#     print("Vowel")

# else:
#     print("Consonant")


if len(alphabet) == 1 and alphabet.isalpha:

    if alphabet.lower()in "aeiou":
        print(f"{alphabet} is vowel")

    else:
        print(f"{alphabet} is consonant")

else:
    print("Invalid input ! plese enter single alphabet")


