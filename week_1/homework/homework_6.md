# Homework 6


## Perceptron Updates


In this problem, we will try to understand the convergence of perceptron algorithm and its relation to the ordering of the training samples for the following simple example.

Consider a set of  𝑛=𝑑  labeled  𝑑− dimensional feature vectors,  {(𝑥(𝑡),𝑦(𝑡)),𝑡=1,…,𝑑}  defined as follows:

 	 𝑥(𝑡)𝑖 	 = 	 cos(𝜋𝑡)if𝑖=𝑡 	 	(4.7)
 	 𝑥(𝑡)𝑖 	 = 	 0otherwise, 	 	(4.8)
Recall the no-offset perceptron algorithm, and assume that  𝜃⋅𝑥=0  is treated as a mistake, regardless of label. Assume that in all of the following problems, we initialize  𝜃=0  and when we refer to the perceptron algorithm we only consider the no-offset variant of it.

<hr />

## Working out Perceptron Algorithm

Consider the  𝑑=2  case. Let  𝑦(1)=1,𝑦(2)=1 . Assume that the feature vector  𝑥(1)  is presented to the perceptron algorithm before  𝑥(2) .

For this particular assignment of labels, work out the perceptron algorithm until convergence.

Let  𝜃̂   be the resulting  𝜃  value after convergence. Note that for  𝑑=2 ,  𝜃̂   would be a two-dimensional vector. Let's denote the first and second components of  𝜃̂   by  𝜃̂ 1  and  𝜃̂ 2  respectively.

Please enter the total number of updates made to  𝜃  by perceptron algorithm:

Answer = 2

Please enter the numerical value of  𝜃̂ 1 :

Answer = -1

Please enter the numerical value of  𝜃̂ 2 :

Answwer 1


## General Case - Number of updates

Now consider any  𝑑>0 .

For the specific dataset we are considering, please choose the correct answer from the options below:

Answer = Perceptron algorithm will make exactly  𝑑  updates to  𝜃  regardless of the order and labelings of the feature vectors


## Sketching convergence

Consider the case with  𝑑=3 . Also assume that all the feature vectors are positively labelled. Let  𝑃  denote the plane through the three points in a 3-d space whose vector representations are given by the feature vectors  𝑥(1),𝑥(2),𝑥(3) .

Let  𝜃̂   denote the value of  𝜃  after perceptron algorithm converges for this example. Let  𝑣  denote the vector connecting the origin and  𝜃̂  . Which of the following options is true regarding the vector represented by  𝜃̂  .

Answer = 𝑣  is perpendicular to the plane  𝑃  and pointing towards it
