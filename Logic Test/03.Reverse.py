def reverse(string):
    reversed_string = ""
    for i in string :
        reversed_string = i+reversed_string
    print("Reversed: ",reversed_string)
string = input("Input string: ")
print("entered string",string)
reverse(string)