# Problem set 3

## Gradient Descent


### Gradient Descent: Geometrically Revisited


Assume  𝜃∈ℝ . Our goal is to find  𝜃  that minimizes

𝐽(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2 
 
through gradient descent. In other words, we will

Start  𝜃  at an arbitrary location:  𝜃←𝜃𝑠𝑡𝑎𝑟𝑡 

Update  𝜃  repeatedly with  𝜃←𝜃−𝜂∂𝐽(𝜃,𝜃0)∂𝜃  until  𝜃  does not change significantly

In the 2 dimensional space below, we start our gradient descent at  𝜃𝑠𝑡𝑎𝑟𝑡 . What is the direction  𝜃  moves to in its first update?


Answer = Towards the origin

What happens if we increase the stepsize  𝜂 ?

Answer = the magnitude of change in each update gets larger


Solution:

Gradient descent makes  𝜃  move to opposite direction of the gradient. Thus it will move towards the origin at  𝜃𝑠𝑡𝑎𝑟𝑡 . Also, increasing the stepsize makes the update happen in greater magnitude.
