s = input("Masukan kata : ")
s = s.lower()

reverse= s[::-1]


if( s == reverse ):
    print("Palindrome")
else:
    print("Not Palindrome")