## 1. What is the difference between = and ==?  
= equates two variables while == tests whether the two variables are equal.

## 2. Can I leave out the colon in an if, while, or for statement? Yes/No  
No.The colon is significant and required. It separates the header of the compound statement from the body.

## 3. Should I use tab characters to indent my code? Yes/No  
No, you should avoid placing tab characters in your .py files. Many editors, however, offer the option of automatically placing a sequence of spaces into your program when you type the Tab key.it's appropriate to use that option when composing Python programs

## 4. Compose a program that takes three integer command-line arguments and writes 'equal' if all three are equal, and 'not equal' otherwise.  

def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(2, 1, 2))
print(sum(3, 2, 2))
print(sum(2, 2, 2))
print(sum(1, 2, 3))


## 5. What is the value of j after each of the following code fragments is executed?  

a.	j = 0  
	for i in range (0, 10) :  
	j += i  

0
1
3
6
10
15
21
28
36
45


b.	j = 1  
	for i in range (0, 10) :  
	j += j  

2
4
8
16
32
64
128
256
512
1024

c.	for j in range (0, 10) :  
	j += j  

0
2
4
6
8
10
12
14
16
18

## 6. What are m and n after the following code is executed?  

n = 123456789  
m = 0  
while n != 0:  
	m = (10 * m) + (n % 10)  
	n //= 10  
	print (m)  
	print (n)  

Value m = 987654321 n = 0



## 7 What does this code do?
f = 0  
g = 1  
for i in range (0, 16):  
	f = f + g  
	g = f - g  
	stdio.writeln(f)

#Output is as below
 1
 1
 2
 3
 5
 8
13
21
34
55
89
144
233
377
610
987

## Bonus: Is there an example for when the following for and while loops are not equivalent?  
for variable in range(start, stop):  
				statement1  
				statement2  
				...  
  
  
variable = start  
while variable < stop:  
		statement1  
		statement2  
		...  
		variable +=1  

continue 
print 'Current variable value:',variable
print "End of Program"
