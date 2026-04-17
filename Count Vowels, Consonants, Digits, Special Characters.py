# count vowels consonents digits and special char

text = input("Enter a string: ")

vowels = "aeiouAEIOU"

v = c = d = s = 0

for ch in text:
    if ch in vowels:
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    else:
        s += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special chars:", s)