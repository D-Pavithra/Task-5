def charc(string):
    char_freq={}
    for char in string:
        if char.isalpha():
            char_freq[char]=char_freq.get(char, 0)+1
    ch = max (char_freq, key=char_freq.get)
    return ch
string = input("Enter a string:")
result = charc(string)
print(f"the most frequent character is:", result)