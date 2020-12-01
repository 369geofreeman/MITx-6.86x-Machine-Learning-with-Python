## Value Iteration


Recall from lecture the value iteration update rule :

𝑉∗𝑘+1(𝑠)=max𝑎[∑𝑠′𝑇(𝑠,𝑎,𝑠′)(𝑅(𝑠,𝑎,𝑠′)+𝛾𝑉∗𝑘(𝑠′))], 
 
where  𝑉∗𝑘(𝑠)  is the expected reward from state  𝑠  after acting optimally for  𝑘  steps.

Recall the example discussed in the lecture.


An agent is trying to navigate a one-dimensional grid consisting of  5  cells. At each step, the agent has only one action to choose from, i.e. it moves to the cell on the immediate right.

Note: The reward function is defined to be  𝑅(𝑠,𝑎,𝑠′)=𝑅(𝑠) ,  𝑅(𝑠=5)=1  and  𝑅(𝑠)=0  otherwise. Note that we get the reward when we are leaving from the current state. When it reaches the rightmost cell, it stays for one more time step and then receives a reward of  +1  and comes to a halt.

Let  𝑉∗(𝑖)  denote the value function of state  𝑖 , the  𝑖𝑡ℎ  cell starting from left.

Let  𝑉∗𝑘(𝑖)  denote the value function estimate at state  𝑖  at the  𝑘𝑡ℎ  step of the value iteration algorithm. Let  𝑉∗0(𝑖)  denote the initialization of this estimate.

Use the discount factor  𝛾=0.5 .

We will write the functions  𝑉∗𝑘  as arrays below, i.e. as  [𝑉∗𝑘(1)𝑉∗𝑘(2)𝑉∗𝑘(3)𝑉∗𝑘(4)𝑉∗𝑘(5)] .

Initialize by setting  𝑉∗0(𝑖)=0  for all  𝑖 :

 	 𝑉∗0 	 = 	 [00000]. 	 	 
Then, using the value iteration update rule, we get

 	 𝑉∗1 	 = 	 [00001], 	 	 
 	 𝑉∗2 	 = 	 [0000.51] 	 	 
Note: Note that as soon as the agent takes the first action to reach cell  5 , it stays for one more step and halts and does not take any more action, so we set  𝑉∗𝑘+1(5)=𝑉∗𝑘(5)  for all  𝑘≥1 .


## Value Function Update


Run the  3𝑟𝑑  iteration of the value iteration algorithm to get  𝑉∗3  and answer the following questions:

Enter the value of  𝑉∗3  as an array  [𝑉∗3(1)𝑉∗3(2)𝑉∗3(3)𝑉∗3(4)𝑉∗3(5)] .

(For example, type [0,2,0,3,4] for the array  [02034] .)


Answer = 


## Complexity of Value Iteration


Let the number of states and actions be  |𝑆|  and  |𝐴| , respectively. Choose from the following the complexity of an iteration of the value iteration algorithm.


Answer = (|𝑆|2⋅|𝐴|)

## Another Example of Value Iteration (Software Implementation)


Consider the same one-dimensional grid with reward values as in the first few problems in this vertical. However, consider the following change to the transition probabilities: At any given grid location the agent can choose to either stay at the location or move to an adjacent grid location. If the agent chooses to stay at the location, such an action is successful with probability  1/2  and

if the agent is at the leftmost or rightmost grid location it ends up at its neighboring grid location with probability  1/2 ,

if the agent is at any of the inner grid locations it has a probability  1/4  each of ending up at either of the neighboring locations.

If the agent chooses to move (either left or right) at any of the inner grid locations, such an action is successful with probability  1/3  and with probability  2/3  it fails to move, and

if the agent chooses to move left at the leftmost grid location, then the action ends up exactly the same as choosing to stay, i.e., staying at the leftmost grid location with probability  1/2 , and ends up at its neighboring grid location with probability  1/2 ,

if the agent chooses to move right at the rightmost grid location, then the action ends up exactly the same as choosing to stay, i.e., staying at the rightmost grid location with probability  1/2 , and ends up at its neighboring grid location with probability  1/2 .

Let  𝛾=0.5 .

Run the value iteration algorithm for 100 iterations. Use any computational software of your choice.

Enter the value of  𝑉∗100  as an array  [𝑉∗100(1)𝑉∗100(2)𝑉∗100(3)𝑉∗100(4)𝑉∗100(5)] .

(For example, type [0,2,0,3,4] for the array  [02034] . Type at least 4 decimal digits.)


Answwer = 

Are the values different if we iterate 200 times? Consider only the first three decimal digits to answer this question.

Answer = No

How about if we only performed 10 iterations? Are the values different when compared to 100 iterations? Consider only the first three decimal digits to answer this question.

Answer = Yes



