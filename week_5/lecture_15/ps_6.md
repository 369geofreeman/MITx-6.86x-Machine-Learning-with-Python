# Prediction



## Predictions of a Generative Multinomial Model


Consider using a multinomial generative model  𝑀  for the task of binary classification consisting of two classes which are denoted by + (positive class) and - (negative class).

Let the parameters of  𝑀  that maximize the likelihood of training data for the positive class be denoted by  𝜃+  and for the negative class be denoted by  𝜃− .

Also, suppose that we classify a new document  𝐷  to belong to the positive class iff

log𝑃(𝐷|𝜃+)𝑃(𝐷|𝜃−)≥0 
 
where  𝑃(𝐷|𝜃)  stands for the probability that document  𝐷  is generated using a multinomial distribution with parameters  𝜃 .

Which of the following option(s) is/are true about this generative classifier? Choose all that apply from the statements below:



Answer = A document is classified as positive iff  𝑃(𝐷|𝜃+)≥𝑃(𝐷|𝜃−)

Answer = The generative classifier  𝑀  can be shown to be equivalent to a linear classifier given by  ∑𝑤∈𝑊(count(𝑤)𝜃′𝑤)≥0  where  𝜃′𝑤=log𝜃+𝑤𝜃−𝑤


## Linear Classifier of the Generative Multinomial Model



Consider the prediction classifier for the two classes  𝜃+  and  𝜃−  introduced in the above video. For this problem, let  0  and  1  represent the classes  +  and  − , respectively.

Let  𝑊={Thor,Loki,Hulk} . Let  𝑝(Thor∣0)=𝑝(Loki∣0)=𝑝(Hulk∣0)=1/3  and let  𝑝(Thor∣1)=𝑝(Loki∣1)=1/4  and  𝑝(Hulk∣1)=1/2 .

We see the following document  𝐷=Thor Thor Hulk Loki Loki . To what class would you classify the document to using the linear classifier for the generative multinomial model? (Type “0" for class 0 (+) and “1" for class 1 (-)).

Answer = 0



