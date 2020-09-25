# Homework 3

## Decision Boundaries


In this problem, we will investigate the decision boundary of different classifiers.


### 3) a

Consider the function defined over three binary variables:  𝑓(𝑥1,𝑥2,𝑥3)=(¬𝑥1∧¬𝑥2∧¬𝑥3) .

We aim to find a  𝜃  such that, for any  𝑥=[𝑥1,𝑥2,𝑥3] , where  𝑥𝑖∈{0,1} :

𝜃⋅𝑥+𝜃0>0 when 𝑓(𝑥1,𝑥2,𝑥3)=1, and  
 
𝜃⋅𝑥+𝜃0<0 when 𝑓(𝑥1,𝑥2,𝑥3)=0. 
 
If  𝜃0=0  (no offset), would it be possible to learn such a  𝜃 ?

Answer = No

Would it be possible to learn the pair  𝜃  and  𝜃0 ?

Answer = Yes


### 3) b-1

You are given the following labeled data points:

Positive examples:  [−1,1]  and  [1,−1] ,

Negative examples:  [1,1]  and  [2,2] .

For each of the following parameterized families of classifiers, identify which parameterized family has a family member that can correctly classify the above data and find the corresponding parameters of a family member that can correctly classify the above data.

Note: If there is no family member inside the parameterized family that can correctly classify the above data, just enter  0  for all the parameters.

Inside (positive) or outside (negative) of an origin-centered circle with radius  𝑟 . Enter a scalar for  𝑟 . If there is no such  𝑟 , just enter 0.

Answer = 0


### 3) b-2

Inside (positive) or outside (negative) of an  [𝑥,𝑦] -centered circle with radius  𝑟 .

Answer = [𝑥,𝑦] : = [-0.7,-1.1]
Answer r: = 2.3


### 3) b-3

Strictly above (positive) or below (negative) a line through the origin with normal  𝜃 . Here we define "above" as  𝜃⋅𝑥>0 , and define "below" similarly. Note: Please enter a list for  𝜃  as  [𝜃1,𝜃2] . If there is no solution, enter  [0,0]

Answer = [0,0]

### 3) b-4

Strictly above (positive) or below (negative) a line with normal  𝜃  and offset  𝜃0 . Here we define "above" as  𝜃⋅𝑥+𝜃0>0 , and define "below" similarly. Note: If there is no solution, enter  𝜃=[0,0]  and  𝜃0=0 .

Answer = 


### 3) b-5

Which of the below are families of linear classifiers?

(Choose all that apply.)

Answer = Strictly above or below a line through the origin with normal  𝜃 .
Answer = Strictly above or below a line with normal  𝜃  and offset  𝜃0 .

