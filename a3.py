'''
# 1
Given two integer variables, a and x (where a is 10 and x is 2), write a single
expression that adds 1 to a, and then multiplies the resulting value by x.
Print out the result of your evaluated expression, with the words
"Question 1 Result:" preceding your result print out.
'''
# WRITE YOUR SOLUTION HERE
a=10
x=2
print ("Question 1 Result:",(a+1)*x)



'''
# 2
Given three integer variables, x, lb, and ub (where x is 2, lb is 1, and ub is
2), write a single boolean expression that evaluates to True if x is strictly
between lb and ub, and False otherwise.
Print out the result of your evaluated expression, with the words
"Question 2 Result:" preceding your result print out.
'''
# WRITE YOUR SOLUTION HERE
x=2
lb=1
ub=2
print("Question 2 Result:",x>lb &x<ub)


'''
# 3
Given three integer parameters a, b, and c (where a is 4, b is 3, and c is 5),
write a single boolean expression that returns True if a2+b2 is equal to c2
(this is called a "Pythagorean Triple"), and False otherwise. For example, given
the a=4, b=3, c=5, the expression evaluate as True. Print out the result of your
evaluated expression, with the words
"Question 3 Result:" preceding your result print out.
'''
# WRITE YOUR SOLUTION HERE
a= 4
b= 3
c= 5
print("Question 3 Result:",a**2+b**2==c**2)






'''
# 4
Suppose that, in order to graduate a (fictional) MA program, students need to
complete at least four Computer Science courses, at least four Social Science
electives, and exactly two workshop classes. Note that students are allowed to
substitute computing classes with courses from the Statistics Department.
Finally, their GPA must be above 3.0 to graduate from the program under normal
conditions. If their GPA is 3.0 or lower, they do have the option, though, to
write a thesis to complete their requirements and graduate.

Write an expression (and any variables that you find useful) to evaluate whether
students with the following characteristics are eligible to graduate from the
program. If they are eligible to graduate, your expression should evaluate as
True, otherwise it should evaluate as False. Print out the results of your
evaluated expressions for each student, with the words "Question 4, Student
NUMBER_HERE Graduation Eligibility:" preceding your result print out.

Student 1: 4 Social Science Electives, 3 Computer Science courses, 1 Statistics
course, 2 workshops, 3.7 GPA, no thesis on file.
Student 2: 5 Social Science Electives, 4 Statistics courses, 2 workshops,
3.0 GPA, wrote a thesis.
'''
#WRITE YOUR SOLUTION HERE
GPA=3.7
thesis="no"
number=1
cs_course=3
ss_course=4
workshop=2
stat=1

print("Question 4, Student",number,"Graduation Eligibility:", (cs_course+stat>=4 and ss_course>=4 and workshop==2 and (GPA>3.0 or thesis=="yes")))

GPA=3.0
thesis="yes"
number=2
cs_course=0
ss_course=5
workshop=2
stat=4

print("Question 4, Student",number,"Graduation Eligibility:", (cs_course+stat>=4 and ss_course>=4 and workshop==2 and (GPA>3.0 or thesis=="yes")))
