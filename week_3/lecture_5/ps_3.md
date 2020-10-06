# Problem set 3

## Gradient Based Approach


### True or False

Let  𝑅𝑛(𝜃)  be the least squares criterion defined by

 	 𝑅𝑛(𝜃)=1𝑛∑𝑡=1𝑛Loss(𝑦(𝑡)−𝜃⋅𝑥(𝑡)). 	 
	 
Which of the following is true? Choose all those apply.

Answer = The least squares criterion  𝑅𝑛(𝜃)  is a sum of functions, one per data point.

Answer = ∇𝜃𝑅𝑛(𝜃)  is a sum of functions, one per data point.

For every point, the loss is a function of  𝜃 , so the least squares criterion  𝑅𝑛(𝜃)  is a sum of functions, one per data point, and this is what makes stochastic gradient descent possible. We want to do stochastic gradient descent because it is faster than gradient descent. Finally, because  𝑅𝑛(𝜃)  is sum of functions, one per data point,  ∇𝜃𝑅𝑛(𝜃)  is also a sum of functions one per data point.
