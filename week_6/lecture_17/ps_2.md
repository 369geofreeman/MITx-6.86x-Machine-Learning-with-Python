# RL Terminology


A Markov decision process (MDP) is defined by

a set of states  𝑠∈𝑆 ;

a set of actions  𝑎∈𝐴 ;

Action dependent transition probabilities  𝑇(𝑠,𝑎,𝑠′)=𝑃(𝑠′|𝑠,𝑎) , so that for each state  𝑠  and action  𝑎 ,  ∑𝑠′∈𝑆𝑇(𝑠,𝑎,𝑠′)=1 .

Reward functions  𝑅(𝑠,𝑎,𝑠′),  representing the reward for starting in state  𝑠 , taking action  𝑎  and ending up in state  𝑠′  after one step. (The reward function may also depend only on  𝑠 , or only  𝑠  and  𝑎 .)

MDPs satisfy the Markov property in that the transition probabilities and rewards depend only on the current state and action, and remain unchanged regardless of the history (i.e. past states and actions) that leads to the current state.

Note: If you have taken 6.431x Probability–The Science of Uncertainty and Data, you may review the Markov Property and Markov Chains introduced in Unit 10 Markov Processes. Markov decision processes are extensions of Markov Chains by the set of actions (and the action-dependence of the transition probabilities), and the reward functions.


## Markov Property

Let  𝑋𝑖,𝑖=1,2,…  be a discrete Markov chain with states  {𝑠𝑗,𝑗∈ℕ} . Which of the following statements are correct?


Answer = For  𝑛≥3 ,  𝑃[𝑋𝑛=𝑥𝑛∣𝑋𝑛−1=𝑥𝑛−1,𝑋1=𝑥1]=𝑃[𝑋𝑛=𝑥𝑛∣𝑋𝑛−1=𝑥𝑛−1].

Answer = For  𝑛≥3  and  𝑛−𝑗>1 ,  𝑃[𝑋𝑛=𝑥𝑛∣𝑋𝑛−𝑗=𝑥𝑛−𝑗,𝑋1=𝑥1]=𝑃[𝑋𝑛=𝑥𝑛∣𝑋𝑛−𝑗=𝑥𝑛−𝑗].



An AI agent navigates in the 3x3 grid depicted above, where the middle square is not accessible by the agent (and hence is greyed out).

The MDP is defined as follows:

Every state  𝑠  is defined by the current position of the agent in the grid (and is independent of its previous actions and positions).

The actions  𝑎  are the 4 directions “up", “down",“left", “right".

The transition probabilities from state  𝑠  via action  𝑎  to state  𝑠′  is given by  𝑇(𝑠,𝑎,𝑠′)=𝑃(𝑠′|𝑠,𝑎) .

The agent receives a reward of  +1  for arriving at the top right cell, and a reward of  −1  for arriving in the cell immediately below it. It does not receive any non-zero reward at the other cells as illustrated in the following figure.


## Markovian Setting

Let  𝑠  be any given state in this MDP. The agent takes actions  𝑎1,𝑎2…𝑎𝑛  starting from state  𝑠0  and as a result visits states  𝑠1,𝑠2…𝑠𝑛=𝑠  in that order.

Given that  𝑠𝑛=𝑠,  that is, the agent ends up at the current state  𝑠  after  𝑛  steps, what do the rewards after the  𝑛th  step depend on? (Choose all that apply.)


Answer = Rewards collected after the  𝑛th  step do not depend on the previous states  𝑠1,𝑠2…𝑠𝑛−1  correct

Answer = Rewards collected after the  𝑛th  step can depend on the current state  𝑠  correct

Answer = Rewards collected after the  𝑛th  step do not depend on the previous actions  𝑎1,𝑎2…𝑎𝑛  


## Number of States


Enter the total number of unique states in the MDP described above and depicted by the  3×3  grid above. (Enter  −1  if the number of states is not finite.)


Answer = 8


## Transition Probabilities

Refer to the MDP described and depicted in the  3×3  grid on the top of this page.

Assume that the transition probabilities for all the states are given as a table  𝑀 , whose  (𝑖,𝑗,𝑘) -th entry is  𝑀[𝑖][𝑗][𝑘]=𝑇(𝑠𝑖,𝑎𝑗,𝑠𝑘)=𝑃(𝑠𝑘|𝑠𝑖,𝑎𝑗),  which represents the transition probability of ending up at state  𝑠𝑘  when action  𝑎𝑗  is taken from the state  𝑠𝑖 . Note: Note that here,  𝑠𝑖  and  𝑠𝑘  can be any pair of states, not necessarily reachable by an action in one step.

Enter the number of entries in the table  𝑀 :


Answer = 256


