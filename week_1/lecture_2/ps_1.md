# Problem Set 1: Review of Basic Concepts


```
[[𝐴]]  either takes value  1  or  0  depending on whether  𝐴  is True or False. For example,  [[1=3]]=0 ,  [[1=1]]=1 , and  [[1≠3]]=1
```


<hr />

## Concept Review Problem: car accident prediction 1

In this problem, we will put ourselves in the shoes of a car insurance company. Our goal is to find out whether customers were involved in an accident on July 4th, 1998.

For  8  customers, we know the following information:

number of accidents the customer made in the past.

number of miles the customer has driven.

the customer's age

Also, for  5  of the customers, we know whether each of them was involved in an accident on July 4th, 1998.

If we want to learn a model in a supervised way, what is  𝑛 , the number of training examples?

Answer n = 5


## Concept Review Problem: car accident prediction 2

The insurance company recorded relevant information for all 8 customers, as illustrated in the table below.


|            | number of past accidents | miles customer drove so far | customer's age |
|:----------:|:------------------------:|:---------------------------:|:--------------:|
| customer 1 |             0            |            2710.9           |       21       |
| customer 2 |             2            |           13209.2           |       40       |
| customer 3 |             1            |           89001.4           |       32       |
| customer 4 |             3            |           12381.1           |       18       |
| customer 5 |             0            |            1893.5           |       24       |
| customer 6 |             2            |           32493.5           |       24       |
| customer 7 |             1            |            5443.5           |       30       |
| customer 8 |             0            |            4493.5           |       28       |


What is the dimension of each feature vector?

Answer d = 3


## Concept Review Problem: car accident prediction 3

How many feature vectors are there in the above table?


Answer = Number of Feature vectors = 8


## Concept Review Problem: Classifier and Training Error 1

Assume we have training data and a classifier like the following: (where  ℎ(𝑥)  denotes the value outputted by the classifier with the data point as input)


|        | ℎ(𝑥) |  𝑦 |
|:------:|:----:|:--:|
| data 1 |   1  |  1 |
| data 2 |  -1  |  1 |
| data 3 |   1  |  1 |
| data 4 |   1  | -1 |
| data 5 |  -1  | -1 |



What is the training error?

Answer = 𝜀𝑛(ℎ) = 4





## Concept Review Problem: Classifier and Training Error 2


Now let's examine the training error  𝜀𝑛(ℎ)  in a general sense.  𝜀𝑛(ℎ)  is a function of: (choose all those apply)


Answer = n, the number of traning data, and h, the classifier










