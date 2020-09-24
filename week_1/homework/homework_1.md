# Homework 1 :  Perceptron Mistakes


In this problem, we will investigate the perceptron algorithm with different iteration ordering.

Consider applying the perceptron algorithm through the origin based on a small training set containing three points:

| 𝑥 (1) =[-1,-1],   |  𝑦 (1)=1 |
|-------------------|:--------:|
|   𝑥 (2) =[1,0],   | 𝑦 (2)=-1 |
| 𝑥 (3) =[-1, 1.5], |  𝑦 (3)=1 |
|                   |          |

Given that the algorithm starts with  𝜃(0)=0 , the first point that the algorithm sees is always considered a mistake. The algorithm starts with some data point and then cycles through the data (in order) until it makes no further mistakes.


## 1) a

How many mistakes does the algorithm make until convergence if the algorithm starts with data point  𝑥(1) ? How many mistakes does the algorithm make if it starts with data point  𝑥(2) ?

Also provide the progression of the separating plane as the algorithm cycles in the following list format:  [[𝜃(1)1,𝜃(1)2],…,[𝜃(𝑁)1,𝜃(𝑁)2]] , where the superscript denotes different  𝜃  as the separating plane progresses. For example, if  𝜃  progress from  [0,0]  (initialization) to  [1,2]  to  [3,−2] , you should enter  [[1,2],[3,−2]] 

Please enter the number of mistakes of Perceptron algorithm if the algorithm starts with  𝑥(1) .

Answer = 2

Please enter the progression of the separating hyperplane ( 𝜃 , in the list format described above) of Perceptron algorithm if the algorithm starts with  𝑥(1) .

Answer = [[-1,-1],[-2,0.5]]

Please enter the number of mistakes of Perceptron algorithm if the algorithm starts with  𝑥(2) .

Answer = 1

Please enter the progression of the separating hyperplane ( 𝜃 , in the list format described above) of Perceptron algorithm if the algorithm starts with  𝑥(2) .

Answer = [[-1,0]]

<hr />

## 1) b.

In part (a), what are the factors that affect the number of mistakes made by the algorithm?

Note: Only choose factors that were changed in part (a), not all factors that can affect the number of mistakes

(Choose all that apply.)


Answer = Iteration order


## 1) c.

Now assume that  𝑥(3)=[−1,10] . How many mistakes does the algorithm make until convergence if cycling starts with data point  𝑥(1) ?

Also provide the progression of the separating plane as the algorithm cycles in the following list format:  [[𝜃(1)1,𝜃(1)2],…,[𝜃(𝑁)1,𝜃(𝑁)2]] , where the superscript denotes different  𝜃  as the separating plane progresses. For example, if  𝜃  progress from  [0,0]  (initialization) to  [1,2]  to  [3,−2] , you should enter  [[1,2],[3,−2]] 

Please enter the number of mistakes of Perceptron algorithm if the algorithm starts with  𝑥(1) .


Answer = 6


Please enter the progression of the separating hyperplane ( 𝜃 , in a list format described above) of Perceptron algorithm if the algorithm starts with  𝑥(1) .

Answer = [[-1,-1],[-2,9],[-3,8],[-4,7],[-5,6],[-6,5]]


Please enter the number of mistakes of Perceptron algorithm if the algorithm starts with  𝑥(2) .

Answer = 1


Please enter the progression of the separating hyperplane ( 𝜃 , in the list format described above) of Perceptron algorithm if the algorithm starts with  𝑥(2) .

Answer = [[-1,0]]


## 1) d.

For a fixed iteration order, what are the factors that affect the number of mistakes made by the algorithm between part (a) and part (c)?

Note: Only choose factors that were changed between part (a) and part (c), not all factors that can affect the number of mistakes

(Choose all that apply.)


Answer = Maximum norm of data points

