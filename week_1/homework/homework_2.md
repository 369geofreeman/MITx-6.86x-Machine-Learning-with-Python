# Homework 2 : Perceptron Performance

In class we initialized the perceptron algorithm with  𝜃=0 . In this problem we will also explore other initialization choices.

<hr />

## 2) a.

The following table shows a data set and the number of times each point is misclassified during a run of the perceptron algorithm (with offset  𝜃0 ).  𝜃  and  𝜃0  are initialized to zero.

| 𝑖 | 𝑥 (𝑖)    | 𝑦 (𝑖) | times misclassified |
|---|----------|-------|:-------------------:|
| 1 | [-4, 2]  | +1    |          1          |
| 2 | [-2, 1]  | +1    |          0          |
| 3 | [-1, -1] | -1    |          2          |
| 4 | [2, 2]   | -1    |          1          |
| 5 | [1, -2]  | -1    |          0          |


Write down the state of  𝜃  and  𝜃0  after this run has completed (note, the algorithm may not yet have converged). Enter  𝜃  as a list  [𝜃1,𝜃2]  and  𝜃0  as a single number in the following boxes.

Please enter  𝜃 :

Answer = [-4,2]

Please enter  𝜃0  :

Answer = -3


## 2) b

Provide one example of a different initialization of  𝜃  such that the perceptron algorithm with this initialization would not produce any mistakes during a run through the data.


Answer = 
[𝜃1,𝜃2] = 
𝜃0 : = 



## 2) c

The theorem from question 1. (e) provides an upper bound on the number of steps of the Perceptron algorithm and implies that it indeed converges. In this question, we will show that the result still holds even when  𝜃  is not initialized to  0. 

In other words: Given a set of training examples that are linearly separable through the origin, show that the initialization of  𝜃  does not impact the perceptron algorithm's ability to eventually converge.

To derive the bounds for convergence, we assume the following inequalities holds:

There exists  𝜃∗  such that  𝑦(𝑖)(𝜃∗𝑥(𝑖))‖𝜃∗‖≥𝛾  for all  𝑖=1,⋯,𝑛  and some  𝛾>0 

All the examples are bounded  ‖𝑥(𝑖)‖≤𝑅,𝑖=1,⋯,𝑛 

If  𝜃  is initialized to  0 , we can show by induction that:

𝜃(𝑘)⋅𝜃∗‖𝜃∗‖≥𝑘𝛾 
 
For instance,

𝜃(𝑘+1)⋅𝜃∗‖𝜃∗‖=(𝜃(𝑘)+ 𝑦(𝑖)𝑥(𝑖))⋅𝜃∗‖𝜃∗‖≥(𝑘+1)𝛾 
 
If we initialize  𝜃  to a general (not necessarily 0)  𝜃(0) , then:

𝜃(𝑘)⋅𝜃∗‖𝜃∗‖≥𝑎+𝑘𝛾 
 
Determine the formulation of  𝑎  in terms of  𝜃∗  and  𝜃(0) :

Important: Please enter  𝜃∗  as theta^{star} and  𝜃(0)  as theta^{0}, and use norm(...) for the vector norm  ‖...‖ .

Answer = 𝑎= 


If  𝜃  is initialized to  0 , we can show by induction that:

‖𝜃(𝑘)‖2≤𝑘𝑅2 
 
For instance,

‖𝜃(𝑘+1)‖2≤‖𝜃(𝑘)+𝑦(𝑖)𝑥(𝑖)‖2≤‖𝜃(𝑘)‖2+𝑅2 
 
If we initialize  𝜃  to a general (not necessarily 0)  𝜃(0) , then:

‖𝜃(𝑘)‖2≤𝑘𝑅2+𝑐2 
 
Determine the formulation of  𝑐2  in terms of  𝜃(0) :


Answer = 𝑐2= 

From the above inequality, we can derive the inequality  ‖𝜃(𝑘)‖≤𝑐+𝑘‾‾√𝑅  by applying the following inequality:  𝑥2+𝑦2‾‾‾‾‾‾‾√≤(𝑥+𝑦)2‾‾‾‾‾‾‾‾√  if  𝑥,𝑦>0 .

If  𝜃  is initialized to  0 , we then use the fact that  1≥𝜃(𝑘)‖𝜃(𝑘)‖⋅𝜃∗‖𝜃∗‖  to get the upper bound  𝑘≤𝑅2𝛾2 .

In the case where we initialize  𝜃  to a general  𝜃(0) , use the inequality for  𝜃(𝑘)⋅𝜃∗‖𝜃∗‖  above and the inequality  ‖𝜃(𝑘)‖≤𝑐+𝑘‾‾√𝑅  to derive a bound on the number of iterations  𝑘 .

Hint: Use the larger root of a quadratic equation to obtain the upper bound.

Note: Give your answer in terms of  𝑎,𝑐,𝑅,𝛾  (enter the latter as gamma).


Answer = 𝑘 ≤ 

## 2) d

Since the convergence of the perceptron algorithm doesn't depend on the initialization, the end performance on the training set must be the same. Are the resulting  𝜃 's the same regardless of the initialization?

Answer = No

Does this necessarily imply that the performance on a test set is the same?

Answer = No
