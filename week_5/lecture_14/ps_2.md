# Introduction to the K-Medoids Algorithm

## K-Medoids Algorithm as a Variation of K-Means


As explained in the lecture video, the K-Medoids algorithm is a variation of the K-Means algorithm that addresses some of the K-Means algorithm's limitations. The K-Medoids algorithm is given by

Randomly select  {𝑧1,...,𝑧𝐾}⊆{𝑥1,...,𝑥𝑛} 

Iterate

Given  𝑧1,...,𝑧𝐾 , assign each  𝑥(𝑖)  to the closest  𝑧𝑗 , so that

Cost(𝑧1,...𝑧𝐾)=∑𝑖=1𝑛min𝑗=1,...,𝑘dist(𝑥(𝑖),𝑧𝑗) 
 
Given  𝐶𝑗∈{𝐶1,...,𝐶𝐾}  find the best representative  𝑧𝑗∈{𝑥1,...,𝑥𝑛}  such that

∑𝑥(𝑖)∈𝐶𝑗dist(𝑥(𝑖),𝑧𝑗) 
 
is minimal.

Which part of the K-Medoids algorithm is different from its equivalent counterpart in the K-Means algorithm?

Answer = Part 2.2


## Concept Check: K-Medoids Algorithm


Which of the following is true about the K-Medoids algorithm? Choose all those apply.

Answer = It is always guaranteed that the  𝐾  representatives  𝑧1,...,𝑧𝐾∈{𝑥1,...,𝑥𝑛}

Answer = Line 2.2 of the algorithm(Given  𝐶𝑗∈{𝐶1,...,𝐶𝐾}  find the best representative  𝑧𝑗∈{𝑥1,...,𝑥𝑛}  such that...) finds the cost-minimizing representatives  𝑧1,...𝑧𝐾  for any given distance measure




