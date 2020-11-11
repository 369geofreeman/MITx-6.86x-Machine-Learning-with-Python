# The K-Means Algorithm: The Big Picture


## The K-Means Algorithm: Step-by-Step


In the above lecture, given a set of feature vectors

𝑆𝑛={𝑥(𝑖)|𝑖=1,...,𝑛} 
 
and the number of clusters  𝐾 , we saw that we can use the K-Means algorithm to find reasonably good cluster assignments  𝐶1,...,𝐶𝐾  and the representatives of each of the  𝐾  clusters  𝑧1,...,𝑧𝐾 . The algorithm was given as follows:

Randomly select  𝑧1,...,𝑧𝐾 

Iterate

Given  𝑧1,...,𝑧𝐾 , assign each data point  𝑥(𝑖)  to the closest  𝑧𝑗 , so that

Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝐾‖‖𝑥(𝑖)−𝑧𝑗‖‖2 
 
Given  𝐶1,...,𝐶𝐾  find the best representatives  𝑧1,...,𝑧𝐾 , i.e. find  𝑧1,...,𝑧𝐾  such that

𝑧𝑗=argmin𝑧∑𝑖∈𝐶𝑗‖𝑥(𝑖)−𝑧‖2. 
 
The following figure depicts an example of one of the steps of K-means algorithm:


Which is it?

Answer = Step 2.1



## The following figure depicts an example of one of the steps of K-means algorithm:

Which step is it?


Answer = Step 2.2



