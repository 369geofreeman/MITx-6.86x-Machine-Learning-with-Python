# The K-Means Algorithm: The Specifics


## Finding the Representative z

In this problem, we will find the “best" representative 𝑧𝑗 for the cluster {𝑥(𝑖)}𝑖∈ℂ𝑗.

First, compute the following gradient:

∇𝑧𝑗⎛⎝⎜⎜∑𝑖∈ℂ𝑗‖𝑥(𝑖)−𝑧𝑗‖2⎞⎠⎟⎟.


Answer =  ∑𝑖∈ℂ𝑗−2(𝑥(𝑖)−𝑧𝑗)



Find  𝑧𝑗  that minimizes the sum  ∑𝑖∈ℂ𝑗‖𝑥(𝑖)−𝑧𝑗‖2 .


Answer = ∑𝑖∈𝐶𝑗𝑥(𝑖)|𝐶𝑗|



Regarding the update of  𝑧𝑗 , which of the following statements is true?
(Select all that apply.)

Answer = The value of  𝑧𝑗  is only affected by points  {𝑥𝑖:𝑖∈𝐶𝑗}

Answer = The obtained  𝑧𝑗  is the centroid (center of mass assuming each  𝑥(𝑖)  has equal mass) of the  𝑗 th cluster



## Impact of Initialization


Remember that the K-Means algorithm is given by

Randomly select  𝑧1,...,𝑧𝐾 

Iterate

Given  𝑧1,...,𝑧𝐾 , assign each data point  𝑥(𝑖)  to the closest  𝑧𝑗 , so that
Step 2.1 decreases or does not change the cost of clustering output 
Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝑘‖‖𝑥(𝑖)−𝑧𝑗‖‖2. 
 
Given  𝐶1,...,𝐶𝐾  find the best representatives  𝑧1,...,𝑧𝐾 , i.e. find  𝑧1,...,𝑧𝐾  such that

𝑧𝑗=argmin𝑧∑𝑖∈𝐶𝑗‖𝑥(𝑖)−𝑧‖2. 
 
Which of the following is true about the initialization and output of the K-Means algorithm? Select all those apply.


Answer = Step 2.1 decreases or does not change the cost of clustering output 

Answer = Step 2.2 decreases or does not change the cost of clustering output

Answer = The clustering output that the K-Means algorithm converges to depends on the initialization


## What if K is 1?


Now, assume that we are given with  𝐾=1  as the number of clusters. Now, does initialization matter at all?

Answer = No, because cluster assignment does not change in step 2.1


## K-Means Drawbacks



Which of the following are drawbacks of the K-means algorithm with Euclidean distance (as presented so far in this lecture)? Select all those apply.

Answer = Manual choice of  𝐾

Answer = Not robust to outliers


Answer = Does not scale well with increasing number of dimensions


