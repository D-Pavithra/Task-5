def rem_vowels(string):
    vowels=("AaEeIiOoUu")
    result=""
    for ch in string:
        if ch not in vowels:
            result +=ch
    return result
a = "Hello Guvi world"
b = rem_vowels(a)
print(b)