# Policy and Value Functions



## Definition of Optimal Policy

Given an MDP, and a utility function  𝑈[𝑠0,𝑠1,…,𝑠𝑛], , our goal is to find an optimal policy function that maximizes the expectation of the utility. Here, a policy is a function  𝜋:𝑆→𝐴  that assigns an action  𝜋(𝑠)  to any state  𝑠 . We denote the optimal policy by  𝜋∗ .

Which of the following option is correct about the optimal policy function?



Answer = The  optimal policy assigns an action at every state that maximizes the expected utility.


## Optimal policy - Numerical Example


Recall that in this setup, the agent receives a reward (or penalty) of  −10  for every action that it takes, on top of the  +1  and  −1  when it reached the corresponding cells. Since the agent always starts at the state  𝑠0 , and the outcome of each action is deterministic, the discounted reward depends only on the action sequences and can be written as:

 	 𝑈[𝑎1,𝑎2,…] 	 = 	 𝑅(𝑠0,𝑎1)+𝛾𝑅(𝑠1,𝑎2)+𝛾2𝑅(𝑠2,𝑎3)+⋯ 	 	 
where the sum is until the agent stops.

For the cases  𝛾=0  and  𝛾=0.5 , what is the maximum discounted reward that the agent can accumulate by starting at the bottom right corner and taking actions until it reached the top right corner?

(Remember the negative reward  −10  is applied to any action taken, including one that leads the agent to the  −1  or  +1  cells.)

For  𝛾=0 :


Answer = 


Answer = 



## Value Function

As above, we are working with the  3×3  grid example with  +1  reward at the top right corner and  −1  at the cell below it. The agent also gets a reward of  −10  for every action that it takes. The action outcomes are deterministic. The agent continues to act until it reaches the  +1  cell, when it stops.

The following figures show states  𝑠1,𝑠2,𝑠3,  in which the letter “A" marks the current location of the agent.

		
A value function  𝑉(𝑠)  of a given state  𝑠  is the expected reward (i.e the expectation of the utility function) if the agent acts optimally starting at state  𝑠 . In the given MDP, since the action outcome is deterministic, the expected reward simply equals the utility function.

Which of the following should hold true for a good value function  𝑉(𝑠)  under the reward structure in the given MDP?

Note: You may want to watch the video on the next page before submitting this question.


Answer = 𝑉(𝑠3)<𝑉(𝑠1)<𝑉(𝑠2)




