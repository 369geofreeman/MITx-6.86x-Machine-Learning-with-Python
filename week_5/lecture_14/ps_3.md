# Computational Complexity of K-Means and K-Medoids


## Computational Complexity of K-Means

Remember that the K-Means algorithm is given by

Randomly select  𝑧1,...,𝑧𝐾 

Iterate

Given  𝑧1,...𝑧𝐾 , assign each  𝑥(𝑖)  to the closest  𝑧𝑗 , so that

Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝑘‖‖𝑥(𝑖)−𝑧𝑗‖‖2 
 
Given  𝐶1,...,𝐶𝐾  find the best representatives  𝑧1,...,𝑧𝐾 , i.e. find  𝑧1,...,𝑧𝐾  such that

𝑧𝑗=∑𝑖∈𝐶𝑗𝑥(𝑖)|𝐶𝑗| 
 
Assuming that there are  𝑛  data points  {𝑥1,...,𝑥𝑛} ,  𝐾  clusters and representatives,and each  𝑥𝑖∈{𝑥1,...,𝑥𝑛}  is a vector of dimension  𝑑 , what is the computational complexity for one complete iteration of the k-means algorithm? That is, find the time (or the number of steps) it takes to complete steps 2.1 and 2.2.



Answer = O(nkd)



## Computational Complexity of K-Medoids

Remember that the K-Medoids algorithm is given by

Randomly select  𝑧1,...,𝑧𝐾 

Iterate

Given  𝑧1,...𝑧𝐾 , assign each  𝑥(𝑖)  to the closest  𝑧𝑗 , so that

Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝑘dist(𝑥(𝑖),𝑧𝑗) 
 
Given  𝐶𝑗∈{𝐶1,...,𝐶𝐾}  find the best representative  𝑧𝑗∈{𝑥1,...,𝑥𝑛}  such that

∑𝑥(𝑖)∈𝐶𝑗dist(𝑥(𝑖),𝑧𝑗) 
 
is minimal.

What is the complexity of step 2.1?


Answer = O(ndk)

Now what is the complexity of step 2.2?

Answer = O(n2dk)



