# Homework Five


## Linear Regression and Regularization

In this question, we will investigate the fitting of linear regression.

### 5. (a)

For each of the datasets below, provide a simple feature mapping  𝜙  such that the transformed data  (𝜙(𝑥(𝑖)),𝑦(𝑖))  would be well modeled by linear regression.

Which feature mapping  𝜙  is appropriate for the above model?

Answer = exp(𝑥)

Which feature mapping  𝜙  is appropriate for the above model?

Answer = 𝜙(𝑥)=𝑥−sign(𝑥)

### 5. (b)


Consider fitting a  ℓ2 -regularized linear regression model to data  (𝑥(1),𝑦(1)),…,(𝑥(𝑛),𝑦(𝑛))  where  𝑥(𝑡),𝑦(𝑡)∈ℝ  are scalar values for each  𝑡=1,…,𝑛 . To fit the parameters of this model, one solves

min𝜃∈ℝ, 𝜃0∈ℝ𝐿(𝜃,𝜃0) 
 
where

𝐿(𝜃,𝜃0)=∑𝑡=1𝑛(𝑦(𝑡)−𝜃𝑥(𝑡)−𝜃0)2  + 𝜆𝜃2 
 
Here  𝜆≥0  is a pre-specified fixed constant, so your solutions below should be expressed as functions of  𝜆  and the data. This model is typically referred to as ridge regression .

Write down an expression for the gradient of the above objective function in terms of  𝜃 .

Important: If needed, please enter  ∑𝑛𝑡=1(…)  as a function sum_t(...), including the parentheses. Enter  𝑥(𝑡)  and  𝑦(𝑡)  as x^{t} and y^{t}, respectively.

Answer ∂𝐿∂𝜃=  -2*sum_t(x^{t})*(y^{t}-theta*x^{t}-theta_0)+2*lambda*theta


Write down an expression for the gradient of the above objective function in terms of  𝜃0 .

∂𝐿∂𝜃0= -2*sum_t(y^{t}-theta*x^{t}-theta_0) 

