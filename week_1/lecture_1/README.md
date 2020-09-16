# Unit One: Linear Classifiers and generalisations

# Lecture One: Introduction to Machine Learning


## Machine Learning is everywhere:

There are numerous fields that ML is applied:

* Google uses ML to interperate your queries
* Netflix recommends movies using ML
* Alexia responds to queries using ML
* George Hotz is using ML to win level 3 in three years
* A program called AlphaGo used ML to ebat the world champion at Go


## Whats the definition of ML

```
	"Machine Learnig as a discipline aims to design, understand and aplly computer programs to learn from experience(ie, data) for the purpose of modeling, prediction or control
```

## Prediction problems


We will start our journey with some examples of the problems prediction can aim to solve.

There are many types of peroblems that ML can tackle:

### Future Events

<img src="img1.png" alt="future events  img" width="300"/>

* We might want tpo predict the price of a stock/index/dirivative based on the price pattern up untill now. If we want to know the price one week, month, year into the future, ML can help with that. 

* We can also use ML to find out if a diesese will return or the likelihood of it spreading/getting worse.

* A self driving car would use ML to judge what the traffic around it might do to avoid accidents or simply to stay in lane and abide my the local laws.


### BAout properties we don't know

* Based on the preference of a viewer (the movies he/she saw) we can use ML to recommend movies the user might be interested in to watch nextand not show ones the user mihght dislike.

* We can predict whether a compound will be soluble in water or not

* We can train a model to tell us what an image is of or what it containes

* Translation from one lanuage to another. This is not as simple as one might first think as we need to take into account the structure of the grammer in the local dialects. ML can observe this and learn it rather than  word for word translation that will sound broken to the native speaker


### Basic idea

 - **Supervised learning**

For the beginning section of this course we will studyt supervised learning.
```
Wikipedia Says:

	Supervised learning is the machine learning task of learning a function that maps as
	input to an out put based on an example input to an output based on example input-output pairs

	It infers a function from labeled training data consisting of a set of training examples 

```

What this definition means will be clear eventually, but lets looley look at what the idea is


### A loose example: Supervised Learning

Suppose we want to train a model to to cassify an image. What this means is we willfeed the model an image and it will make a prediction of what it thinks the image is of.

Now we must first note that the machine does not have a brain of its own. We need to tell it what the possibilities of the image can be of. We will provide different categories for the model to use and have it make a prediction as to what the input image might be of. There can be many caterories for it to choose from (> 1000). This problem is called the image classification problem.

The hardcoded engernering way of accomplishing the image classification problem might be to provide specific rules for each category. For instance if we have an image of a mushroom

<img src="img2.png" alt="mush img" width="300"/> 















