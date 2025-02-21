#########################################################################
#########################################################################
#                       Introduction to R [6]
#########################################################################
#########################################################################
# R fundamentals
#########################################################################
# Your first R session
  # To get help, find out which directory is current 
help.start()      # html help and documentation (use it)
help(sort)        # specific help 
?exp              # same help
getwd()           # get working directory
help(round)-
#########################################################################
# Arithmetic with R
# -----------------------------------------------------------------------
2+2                   # addition [1] 4
5*5 + 2.1             # multiplication and addition [1] 27.1
a = 6
a
a = 64
a
5.6/4 - 3             # division and subtraction [1] -1.6
sqrt(8)               # square root
8^(-2)                # power 
abs(-2)	              # absolute value
ceiling(2.5687)	      # ceiling
floor(2.5687)	        # floor
floor(-2.5678)
round(2.5687,digits=2)# rounding a number
10/3
10%/%3                # quotient
10%%3                 # remainder
10/3
exp(5)                # exponential
log(exp(pi))          # natural log
log10(10^2)           # log 10 base  
log2(10)
log(10)/log(2)
sin(pi/2)             # sine 
cos(pi/2)             # cosine 
tan(pi/2)             # tan 
pi
1:20                   # sequences [1] 1 2 3 4 5
seq(1,20)
help(seq)
seq(1,2,length.out=10)
seq(1, 10, by=2)      # sequences [1] 1 3 5 7 9
rep(2,3)              # repeat 2 three times [1] 2 2 2
help(rep)
rep(1:3, times=3)    # repeat 1 to 3, two times [1] 1 2 3 1 2 3
rep(1:3, each=5)     # repeat each elements, two times each [1] 1 1 2 2 3 3
help(rep)
#Assignment to make some objects:
x <- 1 + 2    # put 1 + 2 in object x
x = 1 + 2     # same as above with fewer keystrokes
1 + 2 -> x    # same
x             # view object x
(y = 2 + 5)   # put 2 + 5 in object y and view the result

#########################################################################
# Data Structure
# Variable Type Data Handling
#########################################################################
# Discrete data as Vector of integers
# -----------------------------------------------------------------------
cnt_dummy = 2:-2  
cnt_dummy
class(cnt_dummy)
(sibl = c(1,0,1,0,2,1,1,0,0,1,2,1,0,1,1)) # Join elements to create a vector 
sibl                                    # display the data
class(sibl)
sibl=as.integer(sibl)                   # vector of integers
class(sibl)
length(sibl)                            # number of elements
# -----------------------------------------------------------------------
# Continuous data as Vector of numeric
# -----------------------------------------------------------------------
cnt_dummy = seq(from=1,to=3, by=0.2)      # sequence specify step size
cnt_dummy = seq(1, 4, length.out=5)       # sequence specify length of the vector
cnt_dummy
dim(cnt_dummy)                            # no dimensions NULL
length(cnt_dummy)

cntDummy1 = array(2,3)                    # create a blank vector of length 3
cntDummy1
dim(cntDummy1)                            # Dimensions 3

a = array(c(1,3,4,5,1))
a
class(a)
dim(a)
# -----------------------------------------------------------------------
# Vectors Operations
# -----------------------------------------------------------------------
# Create a vector with mixed variables: turns to vector of numerics
v = c(2, 4, 6, -7.2, 9, 12, 16, 1.1, 6)

# Data extractions
v[4]                                  # Extract fourth element of vector v
v[-4]                                 # Extract all but the fourth element of vector v
v[2:4]                                # Elements two to four of vector v
v[-(2:4)]                             # All elements but two to four of vector v
v[c(2,5)]                             # Elements one and five of vector v
v >= 6                                # checking if 6 is in vector v
v[v >= 6]                             # (Filtering)Elements which are equal to 6 of vector v
sum(v[v==6])                             # How many 6s are there
v1 = v==6
sum(v1)
v[v < 8]                              # (Filtering)All elements less than 8 of vector v
v < 8
sum(v<8)
v2 = c(2,3,5,7)
v2[1]
v1=c("second"=4,"third"=6,"fourth"=-7,"first"=2)  # assigning names to index

v1['first']
v1[4]
v1[1]
# Unitary Vector Operations
print(v)        
v
v[7]=164          # edit second element of vector
v
(v=c(v,3,3,5,7))  # adding element to vector
(v=v[-1])         # deleting first element from vector

sort(v)           # sort the vector v, by-default ascending order
sort(v,decreasing = TRUE)
mean(v)           # average
sd(v)             # standard deviation
var(v)
# Binary Vector Operations
x=c(1,2,3,4,5) 
y=c(2,4,6,8)
x+y             # addition component wise  
x-y             # subtraction  
x*y             # elementwise multiplication
x%*%y           # vector multiplication
x/y             # elementwise division
y%/%x
    
# [Unequal width vector operations]
z=c(10,20)
z
x+z            # repeated addition component wise until the 
               # smaller array size after multiple repetitions exhausts
               # the width of the larger array
#########################################################################
# Variable Type data as Matrix of numerics
# -----------------------------------------------------------------------
v=v[c(-9,-8,-7)]
(mymat=matrix(v, nrow = 3, ncol = 3)) # create a matrix from v
mymat=matrix(v,nrow=5)              # by default, matrix distributes the elements of a vector columnwise
v=c(v,3,4,5)
mymat
(mymat=matrix(v,nrow=3,byrow=TRUE))   # create a matrix from v row-wise
help(matrix)
# -----------------------------------------------------------------------
# Matrices operations
# -----------------------------------------------------------------------
nrow(mymat)                           # number of rows
ncol(mymat)                           # number of columns
dim(mymat)                            # number of rows and columns
mymat[2,3]                            # select one element from mymat
mymat
mymat[2, ]                            # select a row from mymat
mymat[ ,1]                            # select a column from mymat

colnames(mymat)=c("C1","C2","C3")     # naming columns
rownames(mymat)=c("R1","R2","R3","R4","R5")     # naming rows

mymat
mymat["R2","C3"]                      # select an element from mymat

# Matrices: size alteration
newmat=matrix(c(-4,6,2,9,4,1),nrow=2,ncol=3)      # create a rectangular matrix from  
newmat                                            # display matrix "newmat"
(newmat=rbind(newmat,c(9,2,3)))                   # concatenate a row to matrix
(newmat=cbind(newmat,c(2,3,7)))                   # concatenate a column to matrix
newmat=newmat[,-1]                               # deleting first column
newmat
mymat = mymat[c(-4,-5),]
# Matrices: Binary operations
mymat+newmat                  # mymat[i,j] + newmat[i,j]
mymat-newmat                  # mymat[i,j] - newmat[i,j]
mymat*newmat                  # mymat[i,j] * newmat[i,j]
mymat/newmat                  # mymat[i,j] / newmat[i,j]
mymat%*%newmat                # sum over k (mymat[i,k] * newmat[k,j])

# Matrices: Unitary operation
t(newmat)                     # transpose of matrix "newmat"
diag(newmat)                  # extracting diagonals of matrix
solve(newmat)                 # inverse of square matrix
eigen(newmat+t(newmat))       # eigen values, eigen vectors of square matrix
dim(newmat)
#########################################################################
# Data Structure
# Attribute/Categorical Type Data Handling
#########################################################################
# Nominal data as vector of characters
# -----------------------------------------------------------------------
clrs= c('blue','black','blue','grey',
        'blue','grey','blue','grey',
        'grey','black','blue','black',
        'grey','black','black','pink')     # Declaration
print(clrs)                         # display vector
length(clrs)                        # size of data
g = c(2,2,4,6,87,9,0)
g == 2
clrs == 'blue'                      # search in data
length(clrs[clrs == 'blue'])        # how many blues
sum(clrs=='blue')
clrs[c(2,7)]='green'                # modification in vector
clrs
clrs=c(clrs,'grey')                 # adding new data
clrs                                # check the vector
sort(clrs)
# -----------------------------------------------------------------------
# Nominal data as factor
# -----------------------------------------------------------------------
clrsf = factor(c('blue','black','blue','grey',
                 'blue','grey','blue','grey',
                 'grey','black','blue','black',
                 'grey','black','black'))         # Declaration
clrsf[c(2,7)]='green'                             # Invalis modification in factor
levels(clrsf)                                     # check levels
levels(clrsf)=c(levels(clrsf),"green")           # add new level
clrsf[c(2,7)]='green'                             # modification in factor
print(clrsf)
clrsf=c(clrsf,"grey")                             # adding new data
print(clrsf)
# run ln174
clrsf=factor(c(as.character(clrsf),'grey'))       # adding new data
clrsf
clrsf=clrsf[-16]                                  # deleting an element 
sort(clrsf)                                       # sort by level(:dictionary)
# -----------------------------------------------------------------------
# Ordinal data as factor
# -----------------------------------------------------------------------
meduf = factor(c('UG','HS','UG','PG','HS','HS','UG','PG',
                 'UG','UG','PG','HS','PG','UG','PG'),
               levels = c('HS','UG','PG'))        # Declaration
sort(meduf)                                       # sort by level(: as specified)
meduf1 = factor(c('UG','HS','UG','PG','HS','HS','UG','PG',
                  'UG','UG','PG','HS','PG','UG','PG'))
sort(meduf1)
# -----------------------------------------------------------------------
# Categorical data in matrices of characters
# -----------------------------------------------------------------------

Newborn = matrix(data=clrs, nrow=15, ncol=1, byrow=FALSE, dimnames=NULL)
Newborn = matrix(clrs, 15, 1, FALSE, NULL)

NewBorn = matrix(clrsf,nrow=15,ncol=1)                      # create a single column matrix
NewBorn = cbind(c('female','female','male','female','male',
                  'male','female','female','male','female',
                  'female','male','male','female','male'),
                NewBorn,as.character(meduf))  # adding new column
help(matrix)
NewBorn
class(NewBorn)
colnames(NewBorn) <- c('Sex',"Eye Color","M Education")
NewBorn
NewBorn[10,]                                                # extracting tenth entry
NewBorn[10,"Sex"]='male'                                    # modify tenth entry
NewBorn[10,]                                                # extracting tenth entry

#########################################################################
# Data Structure
# Mixed Data Handling [Structured]
#########################################################################
# Data frames
# -----------------------------------------------------------------------
students=data.frame("Sn"=1:2,"Age"=c(21,22),
                    "Name" = c("Pratyusha","Prabuddha"))  # creating data frame
str(students)                                             # structure of x
students$Name                                             # extracting students' names

wt=c(3.85,3.01,2.54,2.68,3.81,3.35,2.80,2.75,
     3.86,3.76,2.59,2.68,3.62,3.12,2.88)
ht=c(52.51,51.76,49.19,49.98,55.97,54.63,46.43,50.68,
     54.06,54.04,47.01,52.14,51.77,50.23,47.91)

NewBorn = cbind(NewBorn,wt,ht,sibl)               # create mixed data (still in matrix form)
NewBorn=data.frame(NewBorn)                       # create data frame
colnames(NewBorn)[4:6] <- c("Weight","Height","Sibling")    # naming the columns
names(NewBorn)                                    # checking names
print(NewBorn)                                    # check dataframe

NewBorn['Sex']                                  # Extracting particular column
NewBorn[3,]                                     # extracting third row
#NewBorn=as.matrix(NewBorn)                     # create data frame
NewBorn[4,"Weight"]<-2.78                       # modify "wt" of fourth entry (error, why?)
NewBorn[1:4,]

#########################################################################
# Data Structure
# Mixed Data Handling [Unstructured]
#########################################################################
# Lists
# -----------------------------------------------------------------------
# Keeping everything together
mydatalist = list(hospital='National Medical college',
                 data=NewBorn,season='July,2017')   # create mixed data  
length(mydatalist)                                  # shows number of objects
str(mydatalist)                                     # see the structur

mydatalist$hospital                                 # show (a particular component) name of the hospitl
mydatalist$data[5,]                                 # extracting fifth entry of "data" object
mydatalist$data
mydatalist$data[5,'Eye.Color']='blue'               # modify the "eye_color" of fifth entry of "data" object
mydatalist                                          # checking the modification
mydatalist$data=mydatalist$data[order(mydatalist$data[,'Weight']),]
mydatalist

#########################################################################
#########################################################################

#########################################################################
# Some general commands 
# -----------------------------------------------------------------------
# To check data type
# -----------------------------------------------------------------------
class(v)
class(mymat)
class(newmat)
class(clrs)
class(clrsf)
class(NewBorn)
class(mydatalist)
# -----------------------------------------------------------------------
# Class conversion
# -----------------------------------------------------------------------
print(v)
print(as.integer(v))          # from numeric (conitnuous) to integer (discrete)
clrsf=as.character(clrsf)     # from factor to character
# -----------------------------------------------------------------------
# To list your objects, remove objects.
# -----------------------------------------------------------------------
ls()                  # list all objects " 
ls(pattern = "my")    # list every object that contains "my" 
ls(pattern = '^m')    # objects beginning with 'm'
ls(pattern = 't$')    # objects ending with 't'
rm(mydata)            # remove object "mydata"
# -----------------------------------------------------------------------
# To quit
q()               # end the session  
# -----------------------------------------------------------------------
#########################################################################