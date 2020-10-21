# Problem set one

### Motivation

Consider the classification decision rule

𝑦̂ =sign(𝜃⋅𝜙(𝑥)) 
 
where  𝑥∈ℝ𝑑  represent input data and  𝑦∈{1,−1}  is the corresponding predicted labels, and we have omitted the bias/offset term for simplicity.

Given the model above, determine if the following statements are True or False.

The feature map  𝜙  is function from  ℝ𝑑  to  ℝ𝑑 .

Answer = false, because its not neccessary for the feature map to be a function from Rd to Rd ,it depends on the dimension of theta.

If  𝜙(𝑥)∈ℝ𝐷,  then the classification parameter  𝜃  is also a vector in  ℝ𝐷 . (Answer based on the model as written.)


Answer = true, if feature map is a function from Rd to Rd ,then theta must be also in Rd , else the dot product is not possible between them.




