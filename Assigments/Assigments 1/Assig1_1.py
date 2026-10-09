# Write a program to calculate the percentage of student based on marks of any 5
# subjects.


#Assuming each subject in out of 100 ,marks :
# Total marks = marks of 5subjects (500)

sub1 = float(input("Enter marks of c programming:")) #we can use  float() for give decimal value of marks.  ex : 45.89
sub2 = float(input("Enter marks of Web Technologies:"))
sub3 = float(input("Enter marks of Microprocessor:"))
sub4 = float(input("Enter marks of Data Science:"))
sub5 = float(input("Enter marks of Java:"))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5  #calculating total marks of 5 subjects

percentage = (total_marks / 500) * 100 # calculating percentage of student based on total marks.

print("Total obtained marks:",total_marks)
print("Percentage of student:",percentage,"%")