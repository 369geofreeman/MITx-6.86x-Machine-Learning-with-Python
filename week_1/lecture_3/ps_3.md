# Problem set 3


## Hinge Loss and Objective Function


### Hinge Loss Exercise 1

Compute the output of Hinge Loss function (as described in the video) for the following values:

Answer:

Lossℎ(0)=	1 
Lossℎ(0.2)=	0.8
Lossℎ(-10)=	11

Lossℎ(𝑧)={0 if 𝑧>=11−𝑧 otherwise


### Hinge Loss Exercise 2

In a  2  dimensional space, there are points  𝐴,𝐵,𝐶,𝐷  as depicted below. Let  𝐴=(𝑥𝑎,𝑦𝑎),𝐵=(𝑥𝑏,𝑦𝑏),𝐶=(𝑥𝑐,𝑦𝑐),𝐷=(𝑥𝑑,𝑦𝑑) .


What is the hinge loss of point  𝐴 ,  Lossℎ(𝑦(𝑎)(𝜃⋅𝑥(𝑎)+𝜃0)) ?

Answer = 2


What is the hinge loss of point  𝐵 ,  Lossℎ(𝑦(𝑏)(𝜃⋅𝑥(𝑏)+𝜃0)) ?

Ansswer = 0


What is the hinge loss of point  𝐶 ,  Lossℎ(𝑦(𝑐)(𝜃⋅𝑥(𝑐)+𝜃0)) ?

Answer = Between 0-1


What is the hinge loss of point  𝐷 ,  Lossℎ(𝑦(𝑑)(𝜃⋅𝑥(𝑑)+𝜃0)) ?

Answer = 1



Solution:

𝐴  is on the positive margin boundary but with the label  −1 , so

𝑦(𝑎)(𝜃⋅𝑥(𝑎)+𝜃0)=−1. 
 
Thus its hinge loss is  2.   𝐵  is on the positive margin boundary and with the label  +1 , so

=𝑦(𝑏)(𝜃⋅𝑥(𝑏)+𝜃0)=1. 
 
Thus its hinge loss is  0 .  𝐶  lies between the decision boundary and the margin boundary. Thus

1>𝑦(𝑐)(𝜃⋅𝑥(𝑐)+𝜃0)>0. 
 
Thus  𝐶 's hinge loss is between  0  and  1 . Similarly, because  𝐷  is on the decision boundary,

𝑦(𝑑)(𝜃⋅𝑥(𝑑)+𝜃0)=0. 
 
Thus its hinge loss is  1 .Loss functions tell you in general how bad the prediction is. The Hinge Loss tells us how undesirable a training example is, with regard to the margin and the correctness of its classification.



### Regularization

Remember that for points  (𝑥,𝑦)  on the boundary margin, the distance from the decision boundary to  (𝑥,𝑦)  is  1∣∣𝜃∣∣ . Thus

𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)=1. 
 
And

𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)∣∣𝜃∣∣=1∣∣𝜃∣∣. 
 
Now our goal is to maximize the margin, that is to maximize  1∣∣𝜃∣∣ . Which of the following is NOT equivalent to maximizing  1∣∣𝜃∣∣ ?

Answer = maximizing  √∣∣𝜃∣∣


Maximizing  1∣∣𝜃∣∣  is equivalent to maximizing  1∣∣𝜃∣∣2 . It is also equivalent to minimizing  ∣∣𝜃∣∣ .




### Objective


Remember that our objective is given as

𝐽(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2. 
 
Our goal is to minimize this objective  𝐽 . Now, which of the following is true if we have a large  𝜆 ?

Answer = We put more importance on maximizing the margin than minimizing errors


Solution:

Remember that the first term

1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥+𝜃0)) 
 
corresponds to the sum of hinge losses on each training example, and the second term

𝜆2∣∣𝜃∣∣2 
 
corresponds to maximizing the margin. If we increase  𝜆 , we put more weight on maximizing the margin than minimizing the sum of losses.
