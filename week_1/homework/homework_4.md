# Homework part 4

## Linear Support Vector Machines

In this problem, we will investigate minimizing the training objective for a Support Vector Machine (with margin loss).

The training objective for the Support Vector Machine (with margin loss) can be seen as optimizing a balance between the average hinge loss over the examples and a regularization term that tries to keep the parameters small (increase the margin). This balance is set by the regularization parameter  𝜆>0 . Here we only consider the case without the offset parameter  𝜃0  (setting it to zero) so that the training objective is given by

 	 [1𝑛∑𝑖=1𝑛𝐿𝑜𝑠𝑠ℎ(𝑦(𝑖)𝜃⋅𝑥(𝑖))]+𝜆2‖𝜃‖2=1𝑛∑𝑖=1𝑛[𝐿𝑜𝑠𝑠ℎ(𝑦(𝑖)𝜃⋅𝑥(𝑖))+𝜆2‖𝜃‖2] 	 	(4.3)
where the hinge loss is given by

Lossℎ(𝑦(𝜃⋅𝑥))=max{0,1−𝑦(𝜃⋅𝑥)} 
 
 	 𝜃̂ =Argmin𝜃[Lossℎ(𝑦𝜃⋅𝑥)+𝜆2‖𝜃‖2] 	 	(4.4)
Note: For all of the exercises on this page, assume that  𝑛=1  where n is the number of training examples and  𝑥=𝑥(1)  and  𝑦=𝑦(1) .


## Minimizing Loss - Case 1

In this question, suppose that  Lossℎ(𝑦(𝜃̂ ⋅𝑥))>0 . Under this hypothesis, solve for optimisation problem and express  𝜃̂   in terms of  𝑥 ,  𝑦  and  𝜆

Answer = 


## Minimizing Loss - Numerical Example (1)

Consider minimizing the above objective fuction for the following numerical example:

𝜆=0.5,𝑦=1,𝑥=[10] 
 
Note that this is a classification problem where points lie on a two dimensional space. Hence  𝜃̂   would be a two dimensional vector.

Let  𝜃̂ =[𝜃1^,𝜃2^] , where  𝜃1^,𝜃2^  are the first and second components of  𝜃̂   respectively.

Solve for  𝜃1^,𝜃2^ .

Hint: For the above example, show that  Lossℎ(𝑦(𝜃̂ ⋅𝑥))≤0

Answer = 𝜃1^=


Answer 𝜃2^= = 

## Minimizing Loss - Numerical Example (2)

Now, let  𝜃̂ =𝜃̂ (𝜆)  be the solution as a function of  𝜆 .

For what value of  ‖𝑥‖2 , the training example  (𝑥,𝑦)  will be misclassified by  𝜃̂ (𝜆) ?

Answer = ‖𝑥‖2=
