"""
Write a program that asks a user score in percentage and display the grade with some remarks as follows:

Temperature	Grade	Remarks
below 60%	C	Work hard otherwise you're going to fail the exam.
61% to 70%	B	Your result is satisfactory.
71% to 80%	B+	Good Job, Keep doing better.
81% to 90%	A	Amazing Your hard work paid off.
above 90%	A+	Excellent work, Congratulations topper!!
"""

user_score = int(input("enter a user score in %"))
if user_score <= 60:
    print("Grade C")
    print("Work hard otherwise you're going to fail the exam.")
elif user_score <= 70:
    print("Grade B")
    print("Your result is satisfactory.") 
elif user_score <= 80:
    print("Grade B+")
    print("Good Job, Keep doing better.") 
elif user_score <= 90:
    print("Grade A")
    print("Amazing Your hard work paid off.") 
else:
    print("Grade A+")
    print("Excellent work, Congratulations topper!!") 

    """
    enter a user score in %98
Grade A+
Excellent work, Congratulations topper!!

Grade C
Work hard otherwise you're going to fail the exam.

enter a user score in %70
Grade B
Your result is satisfactory.

enter a user score in %73
Grade B+
Good Job, Keep doing better.

enter a user score in %87
Grade A
Amazing Your hard work paid off.
    """