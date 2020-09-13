# Homework


# Gradients and Optimization


## Multivariable Calculus Review: Simple Gradient

```
Let:

	𝑓: ℝ𝑑 → ℝ

	    ⎛𝜃1⎞
	𝜃 = ⎜𝜃2⎜ ↦ 𝑓(𝜃)
	    ⎜ ⋮⎜
            ⎝𝜃𝑑⎠ 	 

denote a differentiable function. The gradient of  𝑓  is the vector-valued function


	 ∇𝜃𝑓: ℝ𝑑 →  ℝ𝑑
	
	    ⎛𝜃1⎞      ⎛∂𝑓/∂𝜃1⎞⎟
	𝜃 = ⎜𝜃2⎜ ↦    ⎜∂𝑓/∂𝜃2⎜⎟ 
	    ⎜ ⋮⎜      ⎜  ⋮   ⎜⎟
            ⎝𝜃𝑑⎠      ⎝∂𝑓/∂𝜃𝑑⎠⎟𝜃 

Consider

	𝑓(𝜃)=𝜃21+𝜃22.

```

Compute the gradient  ∇𝑓 .
(Enter your answer as a vector, e.g., type [2,x] for the vector  (2𝑥) . Note the square brackets, and commas as separators. Enter theta_i for  𝜃𝑖 . )

∇𝜃𝑓(𝜃) = 


<hr />

## Geometric Picture of the Function


As above, consider  𝑓(𝜃)=𝜃21+𝜃22 . Let us visualize  𝑓(𝜃)  as a surface on the  (𝜃1,𝜃2) -plane. We will use the usual horizonal plane as the  (𝜃1,𝜃2) -plane, and the vertical axis as the  𝑓(𝜃) -axis.

Consider the level curves  𝜃21+𝜃22=𝐾  where  𝐾>0  is some fixed real number.

What is the shapes of such a curve?

Answer = 


Consider how the level curves  𝜃21+𝜃22=+𝐾  change as  𝐾  increases from  0  to  ∞ . Does the graph (surface) of  𝑓(𝜃)  have a global maximum, or global minimum, or neither?

Answer = 


At each point  𝜃=(𝜃1,𝜃2)  in the  (𝜃1,𝜃2) -plane,  𝑓(𝜃)  decreases in the direction of...

Answer =  −∇𝜃𝑓(𝜃)

<hr />

Gradient ascent/descent methods are typical tools for maximizing/minimizing functions. Consider the function  𝐿(𝑥,𝜃)  where  𝜃=[𝜃1,𝜃2,…,𝜃𝑛]𝑇  and  𝑥=[𝑥1,𝑥2,…,𝑥𝑛]𝑇 . Our goal is to select  𝜃  such to maximize/minimize the value of  𝐿  while keeping  𝑥  fixed.

<hr />


## Compute the Gradient

```
The gradient  ∇𝜃𝐿(𝑥,𝜃)  is a vector with  𝑛  components:


		    ⎛∂ / ∂𝜃1 𝐿(𝑥,𝜃) ⎞
	 ∇𝜃𝐿(𝑥,𝜃) = ⎟       ⋮       ⎟.
		    ⎝∂ / ∂𝜃𝑛 𝐿(𝑥,𝜃) ⎠


(Note that we are treating  𝑥  as a constant and also differentiating w.r.t. to  𝜃 .)

Let

	𝐿(𝑥,𝜃)=log(1+exp(−𝜃⋅𝑥)).

(Notice that here the  log  function is the natural algorithm.)
```

Evaluate the gradient  ∇𝜃𝐿(𝑥,𝜃) . Which of the following is its  𝑗th  component?

Answer = 

<hr />

## Gradient Ascent or Descent

The direction of the derivative of a function gives us the direction of the largest change in the function as the independent variables vary.

In gradient ascent/descent methods, we make an educated guess about the next values of  𝜃 , with consecutive updates that will hopefully eventually converge to the global minimum of  𝐿(𝑥,𝜃)  (if it exists).

```
If

	𝜃′=𝜃+𝜖⋅∇𝜃𝐿(𝑥,𝜃)
```
where  𝜖  is a small positive real number, Which of the following is true?

Answer = 𝐿(𝑥,𝜃′)>𝐿(𝑥,𝜃)













