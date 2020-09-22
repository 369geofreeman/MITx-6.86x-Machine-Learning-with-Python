# Problem set 2


## Margin Boundary


The decision boundary is the set of points  𝑥  which satisfy
𝜃⋅𝑥+𝜃0=0. 
 
The Margin Boundary is the set of points  𝑥  which satisfy
𝜃⋅𝑥+𝜃0=±1. 
 
So, the distance from the decision boundary to the margin boundary is  1∣∣𝜃∣∣ .



### Margin Boundary 1

As explained in the lecture video, margin boundary is the set of points (𝑥,𝑦) at which the distance from the decision boundary to (𝑥,𝑦) is 1∣∣𝜃∣∣. Now, what is the value of 𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0) for a correctly classified point (𝑥(𝑖),𝑦(𝑖)) on the margin boundary?


Answer = 1

From the previous problem, we know that the distance from a line 𝐿:𝜃𝑥+𝜃0=0 to 𝑃=(𝑥0) is given by ∣∣𝜃𝑥0+𝜃0∣∣∣∣𝜃∣∣. Because we know that the distance from the decision boundary to (𝑥,𝑦) is 1∣∣𝜃∣∣,

∣∣𝜃𝑥0+𝜃0∣∣=1
 
. Thus,

∣∣𝜃𝑥0+𝜃0∣∣=𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)=1



### Margin Boundary 2

What happens to the margin boundaries as we increase  ∣∣𝜃∣∣ ?

Answer = The margin boundries move closer to the decision boundries

As we increase  ∣∣𝜃∣∣ ,  1∣∣𝜃∣∣  decreases. For now, acknowledge that  1∣∣𝜃∣∣  is the distance from the decision boundary to the margin boundary (which we will closely examine in the next set of problems.) Thus, the distance from the point  (𝑥(𝑖),𝑦(𝑖))  that satisfy

𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)=1 
 
to the decision boundary will decrease. Thus the margin moves closer to the decision boundary.



