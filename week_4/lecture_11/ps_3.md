# problem set 3


## RNN Deeper Dive


### RNN Components

The main challenge with an n-gram model is that history needs to be variable, not fixed. Which parts of the RNN allows for this?
(Choose all that apply.)

Answer = The input layer which takes in new information and the previous state

Answer = Having a hidden state


Which aspect of the RNN differentiates it from a traditional feedforward neural network?


Answer = The hidden state is fed in as input for the next step


Is the following sentence true or false: The hidden state at step t only contains information about words close to t.


Answer = False


### RNN Outputs

Let  𝑝𝑡=softmax(𝑊𝑜∗𝑠𝑡) . What function does  𝑊𝑜  serve?

Answer = sm


What function does  𝑠𝑡  serve?

Answer = st


What function does  𝑠𝑜𝑓𝑡𝑚𝑎𝑥  serve?


Answer = wo
