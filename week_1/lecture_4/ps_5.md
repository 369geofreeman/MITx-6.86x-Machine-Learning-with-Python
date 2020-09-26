# Problem set 5


## The Realizable Case - Quadratic program


### The realizable case 1


In the realizable case, which of the following is true?

Answer = There are infinitely many  (𝜃,𝜃0)  that satisfy  𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)>=1  for  𝑖=1,...𝑛 .


### The realizable case 2


Remember the objective function

𝐽(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2 
 
In the realizable case, we can always find  (𝜃,𝜃0)  such that the sum of the hinge losses is 0. In this case, what does the objective function  𝐽  reduce to?


Answer = 12∣∣𝜃∣∣2



### Support Vectors


Support vectors refer to points that are exactly on the margin boundary. Which of the following is true? Choose all those apply.

Answer =  If we remove all points that are support vectors, we will get a different  𝜃,𝜃0
Answer = If we remove one point that is not a support vector, we will get the same  𝜃,𝜃0  correct


Solution:

Support vectors determine the exact solution  𝜃,𝜃0  that minimizes  𝐽(𝜃,𝜃0) . Thus removing/changing all of them changes the  𝜃,𝜃0 . On the other hand, any training example that is not a support vector has no influence on  𝜃,𝜃0 . Thus removing/changing them does not affect  𝜃,𝜃0 .
