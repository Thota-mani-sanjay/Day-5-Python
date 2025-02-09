# Operators:Operators are used to perform the specific task with the operands.
# There are some types of operators in python.They are:
# 1.Arithmetic Operators
# 2.Assignment Operators
# 3.Comparison Operators
# 4.logical Operators
# 5.Bitwise Operators
# 6.Terrinary Operators


# 1.Arithmetic Operators: +,-,,/,*,//,%
num1=10
num2=10
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print(num1//num2)
print(num1%num2)


# 2.Assignment Operators:=,+=,-=,*=,/=,%=
num1=10
num2=10
num1+=num2
print(num1)
num1-=num2
print(num1)
num1*=num2
print(num1)
num1/=num2
print(num1)
num1%=num2
print(num1)

#3.Comparison Operators:==,<,>,<=,>=,!=
a=10
b=15
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a!=b)


# 4.logical Operators:and,or,not
a=10
b=15
print(a<b) and (a>b)
print(a>b) or (a<b)
print(not(a<b) and (a>b))

# 5.Bitwise Operators:~,<<,>>
a=8<<2
print(a)
b=9>>1
print(b)
c=~10
print(c)