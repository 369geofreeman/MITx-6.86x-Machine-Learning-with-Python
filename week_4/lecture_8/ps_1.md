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


### Neural networks

Motivation to Neural Networks

So far, the ways we have performed non-linear classification involve either first mapping  𝑥  explicitly into some feature vectors  𝜙(𝑥),  whose coordinates involve non-linear functions of  𝑥,  or in order to increase computational efficiency, rewriting the decision rule in terms of a chosen kernel, i.e. the dot product of feature vectors, and then using the training data to learn a transformed classification parameter.

However, in both cases, the feature vectors are chosen . They are not learned in order to improve performance of the classification problem at hand.

Neural networks, on the other hand, are models in which the feature representation is learned jointly with the classifier to improve classification performance.

