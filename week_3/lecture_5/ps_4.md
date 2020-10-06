# Problem set four


##  Closed Form Solution


### Necessary and Sufficient Condition for a Solution

In the above video lecture, we verified the following result:

Computing the gradient of

𝑅𝑛(𝜃)=1𝑛∑𝑡=1𝑛(𝑦(𝑡)−𝜃⋅𝑥(𝑡))22, 
 
we get

 	 ∇𝑅𝑛(𝜃)=𝐴𝜃−𝑏(=0)where 𝐴=1𝑛∑𝑡=1𝑛𝑥(𝑡)(𝑥(𝑡))𝑇,𝑏=1𝑛∑𝑡=1𝑛𝑦(𝑡)𝑥(𝑡). 	 	 
Now, what is the necessary and sufficient condition that  𝐴𝜃−𝑏=0  has a unique solution?



Answer = 𝐴  is invertible. correct


Solution:

For any square matrix  𝐴 ,  𝐴𝜃−𝑏=0  has a unique solution  𝜃=𝐴−1𝑏  if and only if  𝐴  is invertible. 

