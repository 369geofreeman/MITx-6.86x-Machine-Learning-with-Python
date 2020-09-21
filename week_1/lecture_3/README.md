# Lecture 3 Hinge loss, Margin boundaries and Regularization


## Objective

### Hinge loss, Margin boundaries, and Regularization

At the end of this lecture, you will be able to

* Understand the need for maximizing the margin

* Pose linear classification as an optimization problem

* Understand hinge loss, margin boundaries and regularization


# Linear Classification

In the previous lectures, we discussed the idea of finding a hyperplane (line in 2d) that can classify our points. We also are equipped with an algorithm called the Perceptron, that will find a solution if the test set Sn is linearly seprable. 

However we never talked about how good the solution is. For example look at the following figure

<img src="img/img1.png" alt="" width="600"/>


Three choices are plotted for a traning set. As we can clearly see that the set is linearlyu separable. So we don't want something like decision boundry A to be our choice because clearly  we have better classifiers, like B and C.

Even if we run our perceptron here, we will find a line like B or C or any other line that seperates **AL** points correctly.

So A is out of the question. Lets look at choice B AND C


<img src="img/img2.png" alt="" width="600"/>


Now somehow intuitively we feel that choice C is a better choice than choice B. And the reasonis simple. The choice B is just grazing a point labelled +1. Ie, a point is very close to the decission boundry B, while all the points seem to be at a moderate distancefrom choice C.

We are doing all this calculation in order for us to classify new points.
Suppose some new cases from the test set are such that they are located in the vicinity of this +1 label point, that is very close to the decission boundry.

These points must clearly have label +1 because, they are very close to a feature vector with +1 label. (This is not a robust claim, just a logical assumption), But we see that our choice B will misclassify many such test cases.

However chooice C is still far far away from these points, and therefore it will properly classify them

So we need to understand how these delicates plau out in mathematical terms, but before that we need...


## MATHEMATICAL INTERLUDE: Distance between line and point


Throughout this lecture, we willuse the concept of distance in order to formulate our problem. Lets see how the distance between a line and a point is calculated.

Although we are finding the distance between a line and a points, the procedure we will use and the result we obtained is the general for for distance between a point in ℝᵈ and a hyperplane in ℝᵈ given by 𝜣 ﹒x + 𝜣₀ = 0

Lets start 


<img src="img/img3.png" alt="" width="600"/>


So the problem is simple. we have a point P and we denote it vectorily as ẋ₀.
We wish to find its **PERPENDICULAR** distance from the line with equation 𝜣 ﹒ẋ + 𝜣₀ = 0

* We draw a vector starting from the line at A and meeting point P. This vector ĀP will be perpendicular to the line

* There's only one direction perpendicular to the line. That is 𝜣's direction. Therefore we can say that  ĀP is a multiple of 𝜣, ie ĀP = ℷ𝜣 where ℷ ∈ℝ

* Now by vector addition ȰA + ĀP = ȰP. ȰP is ẋ₀ by definition and ĀP = ℷ𝜣 decided above

* So we have ȰA = ẋ₀ - ℷ𝜣

* But the point A lies on the line 𝜣 ﹒ẋ + 𝜣₀ = 0 so ȰA vector should satisfy the equation, ie : 𝜣 ﹒ȰA + 𝜣₀ = 0

* This gives us 𝜣 ﹒(ẋ₀ - ℷ𝜣) + 𝜣₀ = 0 ⟹  ℷ = 𝜣 ﹒ẋ₀ + 𝜣₀ / ||𝜣||²

* Finally we can get the distance between P and the line by finding the length of vector ĀP

<img src="img/img4.png" alt="" width="500"/>

So finally we have 


<img src="img/img5.png" alt="" width="600"/>


Note that during the derivation, we never mentioned d the dimension we are in. All equations we used were in vector form. So this is a formular in general for perfendicular distance between a point in ℝᵈ and hyperplane: 𝜣 ﹒x + 𝜣₀ = 0

Now that this is out of the way we are ready to tackle our problem.


## Learning as Optimisation


now we had the problem where we had to find a decission boundry given the traning data. We will now see this problem with a different perspective.
We will find 𝜣 and 𝜣₀ taht will minimise something, This is a common practice in MAths and we will do that. But forst we will set the problem up.


<img src="img/img6.png" alt="" width="600"/>


We have the traning points below, and instead of fitting / finding just one decision boundry, we will fit a broad thick boundry inbetweenthe points as shown

* The right line (or hyperpolane) that's close to -1 labelled points is called negative margin boundry
* The left line (or hyperplane) that's close to the +1 labelled points is called the possitive margin boundry


The idea is simple : The actual decision boundry will lie slightly inbetween the left and right margin boundry. Note that all these three boundries are parallel to each other


<img src="img/img7.png" alt="" width="600"/>


If you wish to see it another way, here is the idea. We will have our decision boundry, and parallel to it will be two more boundries, one on each side. we will somehow strech these two boundries along 𝜣's direction and see how our problems solution can be found in an optimal way


## Linear Classification : Margin

Lets now try to write the equation of these margin boundries. Forst we must note that these are just lines (hyperplanes in general) that are parallel to our decission boundry 𝜣 ﹒x + 𝜣₀ = 0.
So the normal vector for all boundries, decision(one) and margin(two) will be the same direction

<img src="img/img8.png" alt="" width="600"/>


So we can with confidence say that the equation of margin boundries will be of the form 𝜣 ﹒x + c = 0.
	- C is some real value and will differ for possitive and negative margin boundries


Now for  given 𝜣 vector and 𝜣₀, that is for a given  decision boundry. We want two lines (hyperplanes generally). that are parallel to the decission boundry. One we impose (by construction) this parallality conditioin it's fixed that the equasions of margins will be of form 𝜣 ﹒x + c = 0

Now note that we only have one more constraint left for these margin boundries and that is c. Once the c is fixed they are fixed, amd thet can't move towards or away from decision boundry along 𝜣 vector.

And now out of nowhere we clain that the equation of margins are:

	* Positive margin classifier : 𝜣 ﹒x + 𝜣₀ = 1
	* Negative margin classifier : 𝜣 ﹒x + 𝜣₀ = -1

WHY?

how can we say that? What about the idea of moving these margins along 𝜣 vectors direction in order to find a good margin classifier? 
It seems that we have fixed the margins once we assign the above two equations to the two margins respectively

But before we rush to judgement lets just try to find the perpendicular distance between any of the margin boundry and the decision bounry.

We already know the distance of point with x₀ from line 𝜣 ﹒x + 𝜣₀ = 0 is 

<img src="img/img9.png" alt="" width="600"/>

We can use this trick to find the distance between

	* Line 1 : 𝜣 ﹒x + 𝜣₀ = 0
and
	* Line 2 : 𝜣 ﹒x + 𝜣₀ = 1



**The idea si as following**

Finding the distance between line 1 and line 2 is equivalent to finding the perpendicular distance between **ANY** point on line 2, and line 1. We can take any point on line 2 because, line 1 and line 2 are parallel, so the distance between and point on line 2, to that of line 1 will be the distance between the two lines

<img src="img/img10.png" alt="" width="600"/>

So lets take a general point on pline 2 with vector V₀. 
The distance between V₀(point) and line 1 will be

<img src="img/img11.png" alt="" width="600"/>

Now vector V₀ lies on line 2 so it must satisfy
```
	𝜣 ﹒V₀ + 𝜣₀ = 1
```

Substituting we get the distance between line 1 and line 2 that is
```
	  1
	-----
	||𝜣||
```

if we wanted to find the distance between 𝜣 ﹒x + 𝜣₀ = -1 and line 1.
It would similiarly be 

<img src="img/img12.png" alt="" width="600"/>





















