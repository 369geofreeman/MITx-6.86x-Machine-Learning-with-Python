# Homework Four


## Kernels-II

In this question, we will practice some specific kernel methods.

### 4. (a)

In the figure below, a set of points in 2-D is shown on the left. On the right, the same points are shown mapped to a 3-D space via some transform  𝜙(𝑥) , where  𝑥  denotes a point in the 2-D space. Notice that  𝜙(𝑥)1=𝑥1  and  𝜙(𝑥)2=𝑥2 , or in other words, the first and second coordinates are unchanged by the transformation.


Which of the following functions could have been used to compute the value of the 3rd coordinate,  𝜙(𝑥)3  for each point?


Answer = 𝜙(𝑥)3=𝑥21+𝑥22

Think about how a linear decision boundary in the 3 dimensional space ( {𝜙∈ℝ3:𝜃⋅𝜙+𝜃0=0} ) might appear in the original 2 dimensional space.

For example, suppose the decision boundary in the 3 dimensional space is  𝑧=4 .

Provide an equation  𝑓(𝑥1,𝑥2)=0  in the 2 dimensional space such that all the points  (𝑥1,𝑥2)  with  𝑓(𝑥1,𝑥2)>0  correspond to  𝑧>4  in the 3 dimensional space.

Answer 𝑓(𝑥1,𝑥2)=0= 


### 4. (b)

Consider fitting a kernelized SVM to a dataset  (𝑥(𝑖),𝑦(𝑖))  where  𝑥(𝑖)∈ℝ2  and  𝑦(𝑖)∈{1,−1}  for all  𝑖=1,…,𝑛 . To fit the parameters of this model, one computes  𝜃  and  𝜃0  to minimize the following objective:

𝐿(𝜃,𝜃0)=1𝑛∑𝑖=1𝑛Lossℎ(𝑦(𝑖)(𝜃⋅𝜙(𝑥(𝑖))+𝜃0))+𝜆2‖𝜃‖2 
 
where  𝜙  is the feature vector associated with the kernel function. Note that, in a kernel method, the optimization problem for training would be typically expressed solely in terms of the kernel function  𝐾(𝑥,𝑥′)  (dual) rather than using the associated feature vectors  𝜙(𝑥)  (primal). We use the primal only to highlight the classification problem solved.

The plots below show 4 different kernelized SVM models estimated from the same 11 data points. We used a different kernel to obtain each plot but got confused about which plot corresponds to which kernel. Help us out by assigning each plot to one of the following models: linear kernel, quadratic kernel, order 3 kernel, and RBF kernel.

Which kernel is used in the above model?


Answer = quadratic kernel

Which kernel is used in the above model?

Answer = RBF kernel

Which kernel is used in the above model?

Answer = linear kernel

Which kernel is used in the above model?

Answer = order 3 kernel


How would you describe qualitatively how the resulting classifiers vary with the value of  𝜆 ? If the value of  𝜆  is increased, the fitting of model would be

Answer = worse fit on training data (flatter decision boundary)


