# Problem set 2


## Introduction to Non-linear Classification

### Counting Dimensions of Feature Vectorsi



Let  𝑥∈𝐑150,  i.e.  𝑥=[𝑥1,𝑥2,...,𝑥150]𝑇  where  𝑥𝑖  is the  𝑖 -th component of  𝑥 . Let  𝜙(𝑥)  be an order  3  polynomial feature vector. This means, for example,  𝜙(𝑥)  can be

 	 𝜙(𝑥)=[𝑥1,...,𝑥𝑖,...,𝑥150deg 1,𝑥21,𝑥1𝑥2,...,𝑥𝑖𝑥𝑗,...𝑥1502deg 2,𝑥13,𝑥12𝑥2,...,𝑥𝑖𝑥𝑗𝑥𝑘,...,𝑥1503deg 3]where 1≤𝑖≤𝑗≤𝑘≤150. 	 	 
Note that the components of  𝜙(𝑥)  forms a basis of the space of all polynomials with zero constant term and of degree at most  3 .

What is the dimension of the space that  𝜙(𝑥)  lives in? That is,  𝜙(𝑥)∈ℝ𝑑  for what  𝑑 ?

Hint: The number of ways to select a multiset of  𝑘  non-unique items from  𝑛  total is  (𝑛+𝑘−1𝑘) . For example, if a ball can be any of 3 colors, then the number of color configurations of 2 balls is  (3+2−12)=(42)=6 .


Answer:  d = 


### Regression using Higher Order Polynomial feature

Assume we have  𝑛  data points in the training set  {(𝑥(𝑡),𝑦(𝑡))}𝑡=1,...,𝑛  where  (𝑥(𝑡),𝑦(𝑡))  is the  𝑡 -th training example:


We want to find a non-linear regression function  𝑓  that predicts  𝑦  from  𝑥 , given by

𝑓(𝑥;𝜃,𝜃0)=𝜃⋅𝜙(𝑥)+𝜃0 
 
where  𝜙(𝑥)  is a polynomial feature vector of some order. What (loosely) is the minimum order of  𝜙(𝑥) ?

Answer = 


### Effect of Regularization on Higher Order Regression


Let us go back to explore the effect of regularizaion on Higher Order regression.

The three figures below show the fitting result of a 9th order polynomial regression with different regularization parameter  𝜆  on the same training data.

      

Which figure above corresponds to the smallest regularization parameter  𝜆 ?

Answer = A


Which figure corresponds to the largest regularization parameter  𝜆 ?

Answer = B
