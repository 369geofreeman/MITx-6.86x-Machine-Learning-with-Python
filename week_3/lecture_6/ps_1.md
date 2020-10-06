# Problem set one


## Higher Order Feature Vectors


We can use linear classifiers to make non-linear predictions. The easiest way to do this is to first map all the examples  𝑥∈ℝ𝑑  to different feature vectors  𝜙(𝑥)∈ℝ𝑝  where typically  𝑝  is much larger than  𝑑 . We would then simply use a linear classifier on the new (higher dimensional) feature vectors, pretending that they were the original input vectors. As a result, all the linear classifiers we have learned remain applicable, yet produce non-linear classifiers in the original coordinates.

There are many ways to create such feature vectors. One common way is to use polynomial terms of the original coordinates as the components of the feature vectors. We have seen two examples in the video above. We will recall the 1-dimensional example here and see another 2-dimensional example in the problem below.

Example: Given 3 training examples with  𝑥(𝑡)∈ℝ(𝑡=1,2,3)  that are not linearly separable in 1-dimensional space as shown below,


define the feature map  𝜙(𝑥)=[𝜙1(𝑥),𝜙2(𝑥)]𝑇=[𝑥,𝑥2]𝑇,  which maps each example  𝑥(𝑡)  in 1-dimensional space to a corresponding feature vector  𝜙(𝑥(𝑡))=[𝑥(𝑡),(𝑥(𝑡))2]𝑇  in 2-dimensional space.

Then, instead of using  (𝑥(𝑡),𝑦(𝑡)),  we use  (𝜙(𝑥(𝑡)),𝑦(𝑡))  as the training examples (where  𝑦(𝑡)  are the labels):


The new training set is linearly separable in the 2-dimensional  (𝜙1,𝜙2) -space, and we can train a “linear classifier" that is linear in the  𝜙 -coordinates.


## Another 2-Dimensional Example

Given the training examples with  𝑥=[𝑥(𝑡)1,𝑥(𝑡)2]∈ℝ2  above, where a boundary between the positively-labeled examples and the negatively-labeled examples is an ellipse , which of the following feature vector(s)  𝜙(𝑥)  will guarantee that the training set  {(𝜙(𝑥(𝑡)),𝑦(𝑡)),𝑡=1,…,𝑛}  (where  𝑦(𝑡)  are the labels) are linearly separable?
(Choose all that apply.)

Answer = 𝜙(𝑥)=[𝑥1,𝑥2,𝑥1𝑥2,𝑥21,𝑥22]𝑇 

Solution:

Since a possible boundary is an elipse, and we recall from geometry that the equation of any ellipse can be given as

 	 𝜃1𝑥1+𝜃2𝑥2+𝜃3𝑥1𝑥2+𝜃4𝑥21+𝜃5𝑥22+𝜃0=𝜃⋅[𝑥1,𝑥2,𝑥1𝑥2,𝑥21,𝑥22]𝑇+𝜃0=0, 	 	 
for some  𝜃=[𝜃1,𝜃2,𝜃3,𝜃4,𝜃5],  we see that defining the feature map to be  𝜙(𝑥)=[𝑥1,𝑥2,𝑥1𝑥2,𝑥21,𝑥22]𝑇  (the last choice) will allow us to write a linear decision boundary in the  𝜙 -coordinates:

 	  	 𝜃⋅𝜙(𝑥)+𝜃0 	 = 	 0⟺ 	 𝜃⋅[𝑥1,𝑥2,𝑥1𝑥2,𝑥21,𝑥22]𝑇+𝜃0 	 = 	 0. 	 	 
Let us examine the first three choices in order:

The first choice  𝜙(𝑥)=[𝑥1,𝑥2]𝑇  maps  𝑥  to  𝑥  itself in  ℝ2 , so the training set remains the same and not linearly-separable.

The second choice  𝜙(𝑥)=[𝑥1,𝑥2,𝑥21+𝑥22]𝑇  gives decision boundaries of the form:

 	 𝜃⋅[𝑥1,𝑥2,𝑥21+𝑥22]𝑇+𝜃0=𝜃1𝑥21+𝜃2𝑥22+𝜃3(𝑥21+𝑥22)+𝜃0=0, 	 	 
which are circles in the  (𝑥1,𝑥2)−  plane. Hence, if the decision boundary in the  (𝑥1,𝑥2)−  plane is an eclipse that is not circular, this choice of  𝜙  will not give a linear decision boundary in the  𝜙 -coordinates.

The argument for the third choice is analogous to the second choice above.

The  𝑥1𝑥2  term is needed in the fifth solution, since the decision boundary is a rotated eclipse.

