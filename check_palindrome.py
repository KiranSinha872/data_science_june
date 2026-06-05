#check palindrome

s = input()
n = len(s)

i = 0
j = n - 1

while (i < j):
    if (s[i] == s[j]):
        i += 1
        j -= 1
    else:
        print("Not Palindrome")
        break
else:
    print("Palindrome")



    