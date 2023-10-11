def palindrome(string):
    b = string.replace(" ", " ").lower()
    return b ==b[::-1]
a = input("Enter a string:")
if palindrome(a):
    print("True")
else:
    print("False")