a = str (input("Enter 1st string:"))
b = str (input("Enter 2nd string:"))
def sub():
    s1 = set(a.split())
    s2 = set(b.split())
    s3 = s2.intersection(s1)
    print (s1)
    print (s2)
    print (s3)
sub()