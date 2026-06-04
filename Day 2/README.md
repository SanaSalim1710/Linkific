# python-basics-practice

## 1. ATM PIN Verification

### Description
This is similar to an ATM PIN login system. The user is prompted to enter a 4-digit ATM PIN. If the PIN is entered incorrectly, it informs you of the number of remaining attempts and allows you to try again. After 3 failed attempts, the user can no longer enter a PIN number.

### Example Outputs
Enter your 4 digit PIN number: 1233
Incorrect PIN. You have 2 attempts left.

Enter your 4 digit PIN number: 1234
Access granted.


Enter your 4 digit PIN number: 4321
Incorrect PIN. You have 2 attempts left.

Enter your 4 digit PIN number: 3421
Incorrect PIN. You have 1 attempts left.

Enter your 4 digit PIN number: 2431
Incorrect PIN. You have 0 attempts left.

Your account has been locked for exceeding maximum attempts.

## 2. Multiplication Table Generator

### Description
This program generates multiplication tables for a number entered by the user. It generates the multiplication table from 1 to 10.

### Example Output
Enter a number: 5


Multiplication Table for 5
5 x 1 = 5

5 x 2 = 10

5 x 3 = 15

5 x 4 = 20

5 x 5 = 25

5 x 6 = 30

5 x 7 = 35

5 x 8 = 40

5 x 9 = 45

5 x 10 = 50

## 3. Free Shipping Eligibility Check

### Description
The program determines whether a customer is eligible for free shipping. It first checks if you are a member and have a voucher. Free shipping is denied if you do not meet these conditions. After this, it checks your location to determine if you are eligible. Only customers from West Malaysia and East Malaysia are eligible. The user is informed of if they are eligible and the reason they are not if they are denied.

### Example Output
Free shipping voucher applied to your order
Sorry, you need to be a member and have a voucher for free shipping
Sorry, your location is not eligible for free shipping.

## 4. Attendance 

## Description
This program tracks attendance. The user is prompted to indicate if a student is present or absent. The program then calculates and displays the total number of students present and absent.

### Example Output
Is Adela present? (y/n): y

Is Jade present? (y/n): y

Is Perrie present? (y/n): n

Is Leigh-Anne present? (y/n): y

No. of Students Present:  3

No. of Students Absent:  1

## 5. Class Marks Average

### Description
This program stores marks for multiple classes using nested lists. It displays each student's marks and calculates the average score for each class.

### Example Output
Class A marks:
 Student 1 Marks: 85
 Student 2 Marks: 92
 Student 3 Marks: 78
Average: 85.0%

Class B marks:
 Student 1 Marks: 89
 Student 2 Marks: 95
 Student 3 Marks: 91
Average: 91.7%

Class C marks:
 Student 1 Marks: 70
 Student 2 Marks: 64
 Student 3 Marks: 82
Average: 72.0%

## 6. Restaurant Ordering System

### Description
This program simulates a food ordering system. Users can select items on the menu until they type "complete" to end this process. The program calculates and displays the total bill based on the items selected.

### Example Output
Order item or reply "complete" if you are done: Fries
Order item or reply "complete" if you are done: burger
Sorry, the item is not on the menu
Order item or reply "complete" if you are done: ketchup
Order item or reply "complete" if you are done: complete
Total cost: 21


## 7. BMI Calculator

## Description
This program calculates a person's Body Mass Index (BMI) using their height and weight. Based on the BMI value, the person is classified into a health category based on their weight and a simple report is printed.

### Example Output
Report: ARIANA

Age:    32 years old
Gender: Female
Height: 1.53 m
Weight: 54 kg

BMI:    23
Status: Normal weight



## 8. Even, Odd and Prime Numbers

## Description
Given a list of numbers, they are sorted into 3 seperate lists for even, odd and prime numbers. 

### Example Output
Even Numbers: [18, 22, 8, 62]
Odd Numbers: [15, 7, 17, 5, 25, 13]
Prime Numbers: [7, 17, 5, 13]


## 9. Word Filter

### Description
It presents a menu of 4 filtering options, The options are to filter words above a certain length, below a certain length, starting with a specific letter or containing a specific letter. The user is prompted to choose a filter and the program prints a filtered list.

### Example Output
Filtering Options:
1. Words longer than a specified length
2. Words shorter than a specified length
3. Words starting with a specific letter
4. Words containing a specific letter
Choose a filter (1-4): 1
Minimum length: 6

Filtered Words:
['Antarctica', 'Zimbabwe', 'singapore', 'malaysia']

Filtering Options:
1. Words longer than a specified length
2. Words shorter than a specified length
3. Words starting with a specific letter
4. Words containing a specific letter
Choose a filter (1-4): 2
Maximum length: 5

Filtered Words:
['peru', 'India', 'EU', 'Asia']

Filtering Options:
1. Words longer than a specified length
2. Words shorter than a specified length
3. Words starting with a specific letter
4. Words containing a specific letter
Choose a filter (1-4): 3
Enter starting letter: a

Filtered Words:
['Antarctica', 'Asia']

Filtering Options:
1. Words longer than a specified length
2. Words shorter than a specified length
3. Words starting with a specific letter
4. Words containing a specific letter
Choose a filter (1-4): 4
Enter letter to search for: Z

Filtered Words:
['Zimbabwe']


## 10. Heatwave Temperature Check

### Description
The program analyses a list of temperatures of a certain week. It identifies heatwave days where temperatures exceed 30°C. It uses Python's zip function and list comprehension to combine and filter the data. The program prints the days of the week when a heatwave occurred and the temperature recorded.

### Example Output
Temperatures this week: [24, 28, 33, 31, 27, 35, 29]
Heatwave Temperatures: [('Wednesday', 33), ('Thrusday', 31), ('Saturday', 35)]


## 11. Number Guessing

### Description
The program generates a random number between 1 and 10. The user repeatedly guesses until the correct number is found. The program tracks and reports the number of guesses made.

### Example Output
Guess the number!: 5
Try again
Guess the number!: 4
Correct! It took 2 tries to guess the right number.


## 12. General Knowledge Quiz

### Description
The program presents 5 quiz questions to the user and calculates a final score. Some questions support multiple answers.

### Example Output
Capital of France? nice
Incorrect! The correct answer is Paris

Who is the ancient Greek god of the sun? APolLo
What is the square root of 36? 6
On which continent would you find the city of Mumbai?   asia
What is the capital city of Malaysia? KL
That's the end of the quiz! Your final score is 4/5
Great job!


## 13. Monitoring Inventory Stock

### Description
The program monitors inventory levels for stock and classifies stock levels as "Available", "Low Stock" and "Out of Stock".

### Example Output
Shirt : Out of stock
Dress : Available
Jeans : Low Stock


## 14. Student Profile

### Description
The program manages student information using a dictionary. It demonstrates dictionary manipulation by updating existing keys and adding new keys. It prints a student profile and conditionally hides the Honours field for non-honours students.

### Example Output
Student Profile

Student ID: 12345678
Name: Olivia Rodrigo
Status: Intermission
Courses: ['Film Studies', 'Sociology']
GPA: 3.7
Honours student


## 15. Temperature Converter

### Description
The program allows conversion between Celsius, Kevin and Fahrenheit. It prints results of conversion to all other units from a given input unit.

### Example Output
100°F is 37.78°C
100°F is 310.93°K
25°C is 77.00°F
25°C is 298.15°K
300°K is 26.85°C
300°K is 80.33°F
