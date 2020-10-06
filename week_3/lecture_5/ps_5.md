# problem set five



## Regularization


### Regularization: extreme case 1

As in the video above, define the loss function

𝐽𝑛,𝜆(𝜃,𝜃0)=1𝑛∑𝑡=1𝑛(𝑦(𝑡)−𝜃⋅𝑥(𝑡)−𝜃0)22+𝜆2‖𝜃‖2 
 
where  𝜆  is the regularization factor.


In the figure above, the blue dots are the training examples. If we increase  𝜆  to  ∞ , where does  𝑓(𝑥)=𝜃⋅𝑥+𝜃0  converge to?

Answer = Line 1

Solution:

If we increase  𝜆  to  ∞ , minimizing  𝐽  is equivalent to minimizing  ||𝜃|| . Thus  𝜃  will have to be a zero vector. Thus  𝑓(𝑥)=𝜃⋅𝑥+𝜃0  becomes  𝑓(𝑥)=𝜃0 , a horizontal line. Thus  𝑓  converges to line 1.


### Regularization: Extreme case 2

As in the problem above,

𝐽𝑛,𝜆(𝜃,𝜃0)=1𝑛∑𝑡=1𝑛(𝑦(𝑡)−𝜃⋅𝑥(𝑡)−𝜃0)22+𝜆2‖𝜃‖2 
 
where  𝜆  is the regularization factor.


In the figure above, the blue dots are the training examples. If we decrease  𝜆  to  0 , where does  𝑓(𝑥)=𝜃⋅𝑥+𝜃0  converge to?

Answer = Line 2


Solution:

If we decrease  𝜆  to zero, minimizing  𝐽  is equivalent to minimizing  1𝑛∑𝑛𝑡=1(𝑦(𝑡)−𝜃⋅𝑥(𝑡)−𝜃0)22 , which is the "fit." Thus  𝑓  converges to line 2.
