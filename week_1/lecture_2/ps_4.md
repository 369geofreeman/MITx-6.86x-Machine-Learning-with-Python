# The Perceptron Algorithm



## Perceptron Concept Questions 1

Remember that the Perceptron Algorithm (without offset) is stated as the following:


Perceptron ({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛},𝑇): 
  initialize  𝜃=0 (vector);
    for  𝑡=1,...,𝑇  do
      for  𝑖=1,...,𝑛  do
        if  𝑦(𝑖)(𝜃⋅𝑥(𝑖))≤0  then
        update  𝜃=𝜃+𝑦(𝑖)𝑥(𝑖) 

What does the Perceptron algorithm take as inputs among the following? Choose all those apply.


Answer = Traning set
Answer = T - the number of times the algorithm iterates through the whole training set


## Perceptron Update 1

Now consider the Perceptron algorithm with Offset. Whenever there is a "mistake" (or equivalently, whenever  𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)≤0  i.e. when the label  𝑦𝑖  and  ℎ(𝑥)  do not match), perceptron updates

𝜃 with 𝜃+𝑦(𝑖)𝑥(𝑖) 
 
and

𝜃0 with 𝜃0+𝑦(𝑖). 
 
More formally, the Perceptron Algorithm with Offset is defined as follows:


Perceptron ({(𝑥(𝑖),𝑦(𝑖)),𝑖=1,...,𝑛},𝑇): 
  initialize  𝜃=0 (vector);  𝜃0=0 (scalar)
    for  𝑡=1,...,𝑇  do
      for  𝑖=1,...,𝑛  do
        if  𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)≤0  then
        update  𝜃=𝜃+𝑦(𝑖)𝑥(𝑖) 
        update  𝜃0=𝜃0+𝑦(𝑖) 

In the next set of problems, we will try to understand why such an update is a reasonable one.

When a mistake is spotted, do the updated values of  𝜃  and  𝜃0  provide a better prediction? In other words, is

𝑦(𝑖)((𝜃+𝑦(𝑖)𝑥(𝑖))⋅𝑥(𝑖)+𝜃0+𝑦(𝑖)) 
 
always greater than or equal to

𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)


Answer = Yes, because  (𝑦(𝑖))2‖𝑥(𝑖)‖2+(𝑦(𝑖))2≥0



## Perceptron Update 2

For a given example  𝑖 , we defined the training error as  1  if  𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)≤0 , and  0  otherwise:

𝜀𝑖(𝜃,𝜃0)=[[𝑦(𝑖)(𝜃⋅𝑥(𝑖)+𝜃0)≤0]] 
 
Say we have a linear classifier given by  𝜃,𝜃0 . After the perceptron update using example  𝑖 , the training error  𝜀𝑖(𝜃,𝜃0)  for that example can (select all those apply):


Answer = Stay the same
Answer - Decrease









