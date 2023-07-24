'Python'[1]
print("P is returned")
"Strings are sequences of characters."[5]
print("g is returned")
len("wonderful")
print("a count of 9 is returned")
'Mystery'[:4]
print("the letters (myst) are returned")
'p' in 'Pineapple'
print("True")
'apple' in 'Pineapple'
print("True")
'pear' not in 'Pineapple'
print("True")
(2, 4, 6, 8, 10)[1:4]
print("interger 4, 6, 8 are returned")
[("cheese", "queso"), ("red", "rojo")][1][0][2]

'Python'.upper()
print("full capitalization")
'Mississippi'.count('s')
print("a place counf of 4 is returned")
letters = ['c', 'z', 'b', 's']
letters.sort()
letters
print("letters are returned alphabetically")
(3, 9, 8, 42, 17).index(42)
print("a placement count of 3 is returned")
"\t   \n     Don't pad me!   \n   \n".strip()
print("dont pad me is returned with no spaces")
mystery = 'apples pears bananas cheesedoodles'.split()
mystery
print("list is returned with commas")
mystery.sort()
mystery
print("list is returned alphabetically")
mystery.reverse()
mystery
print("the list is reverse alphabetically")

word = "Pneumonoultramicroscopicsilicovolcanoconiosis"
(word[6] + word[30] + word[33] + word[15]).upper()
print("product placement for NOVA")

"""
  >>>

"""
#

if __name__ == "__main__":
    import doctest
    doctest.testmod()