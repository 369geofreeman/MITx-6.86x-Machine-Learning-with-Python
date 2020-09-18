# Problem set 4 : Linear Separation

Given  𝜃  and  𝜃0 , a linear classifier  ℎ:𝑋→{−1,0,+1}  is a function that outputs  +1  if  𝜃⋅𝑥+𝜃0  is positive,  0  if it is zero, and  −1  if it is negative. In other words,  ℎ(𝑥)=sign(𝜃⋅𝑥+𝜃0) .


# Basics 1


As described in the lecture above,  ℎ  is a linear classifier which is defined by the boundary  𝜃⋅𝑥=0  (where theta is a vector perpendicular to the plane.) The  𝑖 th training data is  (𝑥(𝑖),𝑦(𝑖)) , where  𝑥(𝑖)  is a vector and  𝑦(𝑖)  is a scalar quantity. If  𝜃  is a vector of the same dimension as  𝑥(𝑖) , what are  𝑦(𝑖)  and sign( 𝜃⋅𝑥(𝑖) ) respectively?


Answer = Label output of the classifier h


# Basics 2

For the  𝑖 th training data  (𝑥𝑖,𝑦𝑖) , what values can  𝑦(𝑖)  take, conventionally (in the context of linear classifiers)? Choose all those apply.


Answer = -1 and 1


# Basics 3 


For the  𝑖 th training data  (𝑥𝑖,𝑦𝑖) , what values can  𝑠𝑖𝑔𝑛(𝜃⋅𝑥(𝑖))  take? Choose all those apply.

Answer = -1, +1, 0


# When the Product is Positive

When does  𝑦(𝑖)(𝜃⋅𝑥(𝑖))>0  happen? Choose all those apply.

Answer =  𝑦(𝑖) > 0  and  𝜃⋅𝑥(𝑖) > 0  
Answer =  𝑦(𝑖) < 0  and  𝜃⋅𝑥(𝑖) < 0


# Intuitive Meanings of Positive Product

What is the intuitive meaning of  𝑦(𝑖)(𝜃⋅𝑥(𝑖))>0 ?

Answer =  𝑥𝑖label and classified result match


# Intuitive Meanings of Negative Product


What is the intuitive meaning of  𝑦(𝑖)(𝜃⋅𝑥(𝑖))<0 ?


Answer = 𝑥𝑖label and classified result do not match




# Linear Separation 1

Of the following, which is linearly separable? Choose all those apply.


Answer = 1, 3


# Linear Separation 2

A set of Training examples is illustrated in the table below, with the classified result by some linear classifier  ℎ  and the label  𝑦𝑖 . Is it linearly separable?


|           | ℎ(𝑥 𝑖) | 𝑦 𝑖 |
|:---------:|:------:|:---:|
| example 1 |   -1   |  -1 |
| example 2 |    1   |  1  |
| example 3 |    1   |  1  |
| example 4 |   -1   |  -1 |
| example 5 |   -1   |  -1 |



Answer = Yes













