# 1. Value Iteration for Markov Decision Process


Consider the following problem through the lens of a Markov Decision Process (MDP), and answer questions 1 - 3 accordingly.
Damilola is a soccer player for the ML United under-15s who is debating whether to sign for the NLP Albion youth team or the Computer Vision Wanderers youth team. After three years, signing for NLP Albion has two possibilities: He will still be in the youth team, earning 10,000 (60% chance), or he will make the senior team and earn 70,000 (40% chance). Lastly, he is assured of making the Computer Vision Wanderers senior team after three years, with a salary of 37,000.


## Q1

Given that Damilola only cares about having the highest expected salary after three years,  𝑉∗  ( ML United under-15s )  is achieved through the action of signing for Computer Vision Wanderers.


Answer = True


## Q2


Given that Damilola only cares about having the highest expected salary after three years,  𝑉∗  ( ML United under-15s )  is achieved through the action of signing for Computer Vision Wanderers.

Amswer = True


## Q3

There are 3 unique states defined in total in this setting.

Answer = False


## Convergence of the Value Iteration Algorithm

1 point possible (graded)
For an Markov Decision Process (MDP) with a single state and a single action, we know the following hold:

 	 𝑉𝑖+1 	 =𝑅+𝛾𝑉𝑖
 	 𝑉∗ 	 =𝑅+𝛾𝑉∗
Working with these equations, we can conclude that after each iteration, the difference between the estimate and the optimal value of V decreases by a factor of ? (Enter your answer in terms of  𝛾 ; use gamma to represent  𝛾 .)


Answer = 


Consider the following Markov Decision Process (MDP):


MDP with 4 states (rewards for each action are indicated on the arrow)
There are 4 states A, B, C, and D. We can move up or down from states B and C, but only up for A and only down for D. Note that the discount factor  𝛾=0.75 , and that this MDP is deterministic i.e. if you choose action UP, you are guaranteed to move UP, and likewise for action DOWN.


What are the optimal policies for each state?

Answer = up up up down


Partially correct (3/4 points)Review
b
3 points possible (graded)
If we initialize the value function with 0, enter the value of state B after:

one value iteration,  𝑉∗𝐵1
 unanswered
two value iterations,  𝑉∗𝐵2
 unanswered
infinite value iterations,






