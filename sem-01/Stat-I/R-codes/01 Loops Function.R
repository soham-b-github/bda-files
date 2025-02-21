#########################################################################
#########################################################################
#                       R programming [4]
#########################################################################
#########################################################################
# 1. Conditionals and Control Flow
#----------------------------------------
# 1(a) if 
# if (test_expression) {
#   statement
# }
x = -10
if(x >= 0)
{
  print("Positive number")
}

#----------------------------------------
# 1(b) if else
# if (test_expression) {
#   statement1
# } else {
#   statement2
# }
x = -10
if(x > 0)
{
  print("Positve number")
}else
{
  print("Non-positive number")
}

#----------------------------------------
# 1(c) Nested if
# if ( test_expression1) {
#   statement1
# } else if ( test_expression2) {
#   statement2
# } else
#   statement3
x = 4
if (x < 0) {
  print("Negative number")
} else if (x > 0) {
  print("Positive number")
} else print("Zero")

#----------------------------------------
# 1(d) ifelse
# ifelse(test,yes,no)
x = c(12,7,21,9)
ifelse(x %% 2 == 0,"even","odd")
#########################################################################
#########################################################################
# 2. Loops
#----------------------------------------
# 2(a) for
# for (val in sequence)
# {
#   statement
# }
x=c(21,52,34,9,8,11,6)
count <- 0
for (val in x) 
{
  if(val %% 2 == 0)  
    count = count+1
}
print(count)

#----------------------------------------
# 2(b) while
# while (test_expression)
# {
#   statement
# }
i=1
while (i < 6) 
{
  print(i)
  i=i+2
}

#----------------------------------------
# 2(c) break
x=1:8
for (val in x) {
  if (val == 5){
    break
  }
  print(val)
}
  
#----------------------------------------
# 2(d) next
x=2:8
for (val in x) {
  if (val == 5){
    next
  }
  print(val)
}
  
#----------------------------------------
# 2(e) repeat
# repeat {
#   statement
# }
x = 2
repeat {
  print(x)
  x = x+1
  if (x == 5){
    break
  }
}
#########################################################################
#########################################################################
# 3. Functions
#----------------------------------------
# 3(a)i. Syntax
# func_name <- function (argument) {
#   statement
# }
pow <- function(x, y) {
  # function to print x raised to the power y
  result <- x^y
  print(paste(x,"raised to the power", y, "is", result))
}
# 3(a)ii. Call function
pow(8,2)
pow(2,8)
pow(y=2,x=8)

#----------------------------------------
# 3(b)i. Function with default argument
pow <- function(x, y=2) {
  # function to print x raised to the power y
  result <- x^y
  print(paste(x,"raised to the power", y, "is", result))
}
# 3(b)ii. Call function
pow(3)
pow(3,3)
  
#----------------------------------------
# 3(c) Function with/without return value
check <- function(x) {
  if (x > 0) {
    result <- "Positive"
  }
  else if (x < 0) {
    result <- "Negative"
  }
  else {
    result <- "Zero"
  }
  return(result)
#  result  
}
# 3(c)ii call function
check(1)
check(-10)
x=check(0)

#----------------------------------------
# 3(d)i. Multiple return
multi_return <- function(x) {
  my_list <- list("color" = x, "size" = 20, "shape" = "round")
  return(my_list) 
}
# 3(d)ii. call function
a=multi_return("red")
a$color

#----------------------------------------
# 3(e)i. Global and local variables
outer_func = function(){
  a=20
  inner_func = function(){
    a = 30
    print(a)
  }
  inner_func()
  print(a)
}

a=10
# 3(e)ii. call function
outer_func()
print(a)
# 3(e)iii. take global variable
outer_func <- function(){
  inner_func <- function(){
    print(a)
  }
  inner_func()
  print(a)
}
outer_func()

#----------------------------------------
# 3(f)i. Recursive function
recursive.factorial <- function(x) {
  # Recursive function to find factorial
  if (x == 0)    return (1)
  else           return (x * recursive.factorial(x-1))
}
# 3(f)ii. call function 
recursive.factorial(5)

#----------------------------------------
# 3(g)i. infix operator  
5*3-1
`-`(`*`(5,3),1)
`*`(`-`(5,3),1)

# 3(g)ii. User defined infix operator
`%divisible%` <- function(x,y)
{
  if (x%%y ==0) return (TRUE)
  else          return (FALSE)
}
# 3(g)iii. call function
10 %divisible% 2
`%divisible%`(10,3)

#----------------------------------------
# 3(h) Syntax of switch() function
# switch(statement, list)
switch(3,"red","green","blue")
switch(4,"red","green","blue")
switch("color", "color" = "red", "shape" = "square", "length" = 5)
#########################################################################
#########################################################################