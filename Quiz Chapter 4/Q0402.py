"""
Write a program to input a word and find out if it is palindrome.

A word is palindrome if it reads the same from both backward and forward. 
EVE HANNAH BOB, ROTATOR, ANNA, etc. are some of palindrome words

The output in the console should look like below:

Enter a word [press cancel to exit]:    Hannah
palindrome

Enter a word [press cancel to exit]:    John
not palindrome
"""
word = input("enter a word")
if word == word[:: -1]:
    print("palindrome")
else:
    print("not palindrome")

# enter a word hannah
# palindrome

# enter a word john
# not palindrome


