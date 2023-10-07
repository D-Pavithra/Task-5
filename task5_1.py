string = "Guvi Geeks network private limited"
vowels = "AaEeIiOoUu"
def checking(string, vowels):
    final = [each for each in string if each in vowels]
    print(final)
checking (string, vowels)