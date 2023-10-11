def anagram(st1, st2):
    st1 = st1.replace(" ", " ").lower()
    st2 = st2.replace(" ", " ").lower()
    return sorted(st1)==sorted(st2)
string1=input("Enter first string:")
string2=input("Enter second string:")
result = anagram(string1, string2)
print (result)