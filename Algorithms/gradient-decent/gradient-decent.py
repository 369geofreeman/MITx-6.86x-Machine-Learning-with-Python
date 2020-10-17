import numpy as np
import matplotlib.pyplot as plt

## When Testing

# When testing these algorithms it's a good idea to start
# with a smaller iteration rate and see if the cost is
# being reduced with each iteration. If so, try and make the
# learning rate (step size) bigger by increasing it while
# still achieving the same results of a smaller cost with
# each iteration.
# If the cost is too big we will increase the global minima
# and start to head in the wrong direction (up)


## How the results are calculated for gradient decent

# Here we start with the input array [1, 2, 3, 4, 5]
# and the output array [5, 7, 9, 11, 13]
# y = m*x + b,
# if I have m=2 and b=3 (which is the result of running this function) then:
# 5 = 2*1 + 3
# 7 = 2*2 + 3
# 9 = 2*3 + 3
# and so on. So these values of m and b satisfies our equation hence they are 
# our expected values


## The code

def gradient_decent(x, y):
    # start with 0 and take small steps to reach
    # a global minima
    m_curr = b_curr = 0
    # how many steps to take (to be fine tuned) 
    iterations = 1500
    # length of the data points (should be the same)
    n = len(x)
    # Define the learning rate (to be fine tuned)
    learning_rate = 0.08
    # Set up the scatterplot for visulisation
    plt.scatter(x, y, color='red', marker='+', linewidth='2')

    for i in range(iterations):
        # Start by calcualting the predicted value of y
        y_predicted = m_curr * x + b_curr
        # Set the cost function
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        # Calculate m & b derivative
        m_der = -(2/n) * sum(x * (y-y_predicted))
        b_der = -(2/n) * sum(y - y_predicted)
        # Calculate the next step with the learning rate
        # for m and b
        m_curr = m_curr - learning_rate * m_der
        b_curr = b_curr - learning_rate * b_der
        # printing results to see the algorithm in each step
        print("m: {}, b: {}, cost: {}, iteration: {}".format(m_curr, b_curr, cost, i))
        # Plot the results
        plt.plot(x, y_predicted, color='green')
    plt.show()

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])


gradient_decent(x, y)
