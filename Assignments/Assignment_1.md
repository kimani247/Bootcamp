## 1. Compose a program that writes the Hello, World message 10 times. 		 
print ("Hello World \n" *10) 
## 2. Describe what happens if you omit the following in helloworld.py: 
•	the first '  
A syntax error message (Hello is not defined) is displayed which is considered as a python grammar mistake.

•	the second '  
An EOL error message(String literal Unterminated) is displayed which means end of line has no closing tag.

•	the print() statement  
A syntax error message is displayed that there is missing parentheses in call to 'print'

## 3. Which one of the following is the correct way to execute useargument.py using the terminal: • 
Executing python3 useargument.py or python useargument.py will work.

python useargument.py python

python3 useargument.py

python useargument.py

useargument.py python

python useargument	

## 4. Modify helloworld.py to compose a program that takes three names and writes a proper sentence with the names in the reverse of the order they are given, so that, for example, python helloworld.py Alice Bob Carol writes the string 'Hi Carol, Bob, and Alice'

first_name=str(input('Please input the first name:'))
second_name=str(input('Please input the second name:'))
third_name=str(input('Please input the third name:'))
fourth_name=str(input('Please input the fourth name:'))
fifth_name=str(input('Please input the fifth name:'))
sixth_name=str(input('Please input the sixth name:'))
#print out all the names as prompted
names =[first_name,second_name,third_name,fourth_name,fifth_name,sixth_name]
names.reverse()
print("Hi",names)


