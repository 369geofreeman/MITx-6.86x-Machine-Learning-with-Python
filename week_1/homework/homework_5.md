# HomeWork 5

## Passive-aggressive algorithm


In this problem, we will try to understand the loss in Passive-Aggressive (PA) Perceptron algorithm.

The passive-aggressive (PA) algorithm (without offset) responds to a labeled training example  (𝑥,𝑦)  by finding  𝜃  that minimizes

 	 𝜆2‖‖𝜃−𝜃(𝑘)‖‖2+Lossℎ(𝑦𝜃⋅𝑥) 	 	(4.5)
where  𝜃(𝑘)  is the current setting of the parameters prior to encountering  (𝑥,𝑦)  and

Lossℎ(𝑦𝜃⋅𝑥)=max{0,1−𝑦𝜃⋅𝑥} 
 
is the hinge loss. We could replace the loss function with something else (e.g., the zero-one loss). The form of the update is similar to the perceptron algorithm, i.e.,

 	 𝜃(𝑘+1)=𝜃(𝑘)+𝜂𝑦𝑥 	 	(4.6)
but the real-valued step-size parameter  𝜂  is no longer equal to one; it now depends on both  𝜃(𝑘)  and the training example  (𝑥,𝑦) .


### Update equation

Consider minimizing the above defined loss function with the hinge loss component.
What happens to the step size at large values of  𝜆 ? Please choose one from the options below:

Answer = If  𝜆  is large, the step-size of the algorithm ( 𝜂 ) would be small


### Calculating the Step size

Suppose  Lossℎ(𝑦𝜃(𝑘+1)⋅𝑥)>0  after the update. Express the value of  𝜂  in terms of  𝜆  in this case. (Hint: you can simplify the loss function in this case).

Answer = 


### Loss functions and decision boundaries

Consider minimizing the above defined loss function and the setting of our decision boundary plotted below. We ran our PA algorithm on the next data point in our sequence - a positively-labeled vector (indicated with a  + ). We plotted the results of our algorithm after the update, by trying out a few different variations of loss function and  𝜆  as follows:

hinge loss and a large  𝜆 

hinge loss and a small  𝜆 

0-1 loss and a large  𝜆 

0-1 loss and a small  𝜆 

Each of the options below provides a matching between the 4 variations above with a decision boundary plotted in a-d below. Please choose the options that match them correctly. Note that the dotted lines correspond to the previous decision boundary, and the solid blue lines correspond to the new decision boundary; also, note that these are just sketches which ignore any changes to the magnitude of  𝜃 .

Answer:
* a = 
* b = 
* c = 
* d = 
