# homework Three


## Kernels

In this question, we will practice kernel methods in classification.


### 3. (a)

Let  𝑥,𝑞∈ℝ2  be two feature vectors, and let  𝐾(𝑥,𝑞)=(𝑥𝑇𝑞+1)2 . This is often known as a polynomial kernel. It's simple to compute: you just take the dot product between two feature vectors, add one, and then square the result. But what kind of feature mapping does this kernel implicitly use?

Assuming we can write  𝐾(𝑥,𝑞)=𝜙(𝑥)𝑇𝜙(𝑞) , derive an expression for  𝜙(𝑥) .

Enter the solution as a vector  𝜙(𝑥)=[𝑓1(𝑥1,𝑥2),⋯,𝑓𝑁(𝑥1,𝑥2)] .

Answer = 𝜙(𝑥)=  [1,sqrt(2)*x_1,sqrt(2)*x_2,x_1^2, sqrt(2)*x_1*x_2, x_2^2]


### 3. (b)

As a simple example that uses this kernel, imagine that our feature vectors were bag of words vectors. In this example, give an intuitive interpretation of what the  2‾√𝑥1𝑥2  term in the expression for  𝜙(𝑥)  you just wrote down mean


Answer = co-appeareance in document
