# Problem set 4

## Stochastic Gradient Descent

### SGD and Hinge Loss


As we saw in the lecture above,

𝐽(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2=1𝑛∑𝑖=1𝑛[Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2] 
 
With stochastic gradient descent, we choose  𝑖∈{1,...,𝑛}  at random and update  𝜃  such that

𝜃←𝜃−𝜂∇𝜃[Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2] 
 
What is  ∇𝜃[Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))]  if  Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))>0 ?


Answer = -y⁽ⁱ⁾x⁽ⁱ⁾


#### Comparison with Perceptron

Observing the update step of SGD,

𝜃←𝜃−𝜂∇𝜃[Lossℎ(𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0))+𝜆2∣∣𝜃∣∣2] 
 
Which of the following is true?


Answer = Differently from perceptron,  𝜃  is updated even when there is no mistake


We can see from

𝜃←{(1−𝜆𝜂)𝜃 if Loss=0(1−𝜆𝜂)𝜃+𝜂𝑦(𝑖)𝑥(𝑖) if Loss>0 
 
that  𝜃  is updated even when the sum of losses is  0 . This is different from perceptron.
