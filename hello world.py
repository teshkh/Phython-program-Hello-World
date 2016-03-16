#Hitesh Khurana
#This program prints "hello world" on a single line.
#program version 3.0
#Phython version 3.5.1
#3/16/2016

print("hello world");

#See below for version 2.0

hello = 'this is a variable'
print("hello world ", hello)

#See below for version 3.0
#Printing a string backwards
#Len populates the length of a string in this case
#Prints the first charater hello[0] was using to test

a = len(hello)
print("this is the begining character of our variable: ", hello[0]);
for i in range(a):
    print(hello[17-i], end=" ")

#End allows for everything to be printed on one line
#'I' is being incremented everytime the loop completes
#Range (a) tells the phython that i is going to be
#Less than the amount of characters in the string length
#17 is the count of the hello variable, starting the count 0.
    

