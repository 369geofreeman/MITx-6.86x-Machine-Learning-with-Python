# Problem set 1


## Review and the Lambda parameter


### Distance from a line to a point in terms of components

In a 2 dimensional space, a line  𝐿  is given by  𝐿:𝑎𝑥+𝑏𝑦+𝑐=0 , and a point  𝑃  is given by  𝑃=(𝑥0,𝑦0) . What is  𝑑 , the shortest distance between  𝐿  and  𝑃 ? Express  𝑑  in terms of  𝑎,𝑏,𝑐,𝑥0,𝑦0 .

Answer = abs(a*x_0+b*y_0+c)/sqrt(a^2+b^2)

Use the projection equation. Here  𝜃  is  [𝑎,𝑏] ,  𝜃0  is  𝑐  and the point is  [𝑥0,𝑦0] .


### Varying Lambda in the Geometric Sense

Remember that the objective

𝐽(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2. 
 
In the picture below, what happens to  𝑑 , the distance between the decision boundary and the margin boundary, as we increase  𝜆 ?


Hint: You can answer with your intuition in this question. To see whether  𝑑  converges to  𝜆 , think of a simple setting where we are working in 1 dimension with just two points with labels  𝑥1=−1,𝑥2=2,𝑦1=−1,𝑦2=1  and assume that  𝜆  is large enough where it dominates the loss function and pushes  𝜃  close enough to  0  where all points are margin violators.


Answer = d increases


Solution:

Increasing  𝜆  means we put more weight on maximizing the margin. Thus  𝑑  increases.
It is not true that  𝑑  always converges to  𝜆  as  𝜆  increases. Here is a counter example:
Consider a simple setting where we are working in 1 dimension with just two points with labels  𝑥1=−1,𝑥2=2,𝑦1=−1,𝑦2=1  and assume that  𝜆  is large enough where it dominates the loss function and pushes  𝜃  close enough to  0  where all points are margin violators.

 	 𝐽 	 = 	 12[(1−𝜃+𝜃0)+(1−2𝜃−𝜃0)]+𝜆2𝜃2 	 	 
 	 	 = 	 2−3𝜃2+𝜆2𝜃2. 	 	 
Solve this explicitly by taking  ∂𝐽∂𝜃=0 :

 	 −32+𝜆𝜃 	 = 	 0 	 	 
 	 𝜃 	 = 	 32𝜆 	 	 
 	 𝑑 	 = 	 1𝜃=23𝜆. 	 
