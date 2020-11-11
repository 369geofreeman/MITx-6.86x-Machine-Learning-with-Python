# Limitations of the K Means Algorithm

## Limitations of the K-Means Algorithm I


Remember that the K-Means Algorithm is given as below:

Randomly select  𝑧1,...,𝑧𝐾 

Iterate

Given  𝑧1,...,𝑧𝐾 , assign each data point  𝑥(𝑖)  to the closest  𝑧𝑗 , so that

Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝑘‖‖𝑥(𝑖)−𝑧𝑗‖‖2 
 
Given  𝐶1,...,𝐶𝐾  find the best representatives  𝑧1,...,𝑧𝐾 , i.e. find  𝑧1,...,𝑧𝐾  such that

𝑧𝑗=argmin𝑧∑𝑖∈𝐶𝑗‖𝑥(𝑖)−𝑧‖2=∑𝑖∈𝐶𝑗𝑥(𝑖)|𝐶𝑗| 
 
where  |𝐶𝑗|  is the number of points in  𝐶𝑗 .

Which of the following are false about K-Means Algorithm? Please choose all those apply.



Answer = It is always guaranteed that the  𝐾  representatives  𝑧1,...,𝑧𝐾∈{𝑥1,...,𝑥𝑛}


## Limitations of the K-Means Algorithm II


Suppose we have a 1D dataset drawn from 2 different Gaussian distribution  (𝜇1,𝜎21) ,  (𝜇2,𝜎22)  where  𝜇1≠𝜇2 . The dataset contains  𝑛  data points from each of the two distributions for some large number  𝑛 .

Define optimal clustering to be the assignment of each point to the more likely Gaussian distribution given the knowledge of the generating distribution.

Consider the case where  𝜎21=𝜎22 , would you expect a 2-means algorithm to approximate the optimal clustering?

Answer = Yes

Now if  𝜎21>>𝜎22 , would you expect a 2-means algorithm to approximate the optimal clustering?

Answer = No


