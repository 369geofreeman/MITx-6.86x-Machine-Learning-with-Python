import random as rand
import copy


# this is the activation function applied on yin
# ----------------------------------------------
def activation_function(yin):
    if yin == 0:
        return 0
    elif yin > 0:
        return 1
    elif yin < 0:
        return -1


# -----------------------------------------------


# this function will find change in weights
# ------------------------------------------------
def change_in_weights(inputs, learning_rate, target):
    delta_weight = inputs * learning_rate * target
    return delta_weight


# ------------------------------------------------

# this function calculates the change in bias
# ------------------------------------------------
def change_in_bias(bias, learning_rate, target):
    new = bias + learning_rate * target
    return new


# ------------------------------------------------

# this function checks for match with the target class
# ------------------------------------------------
def check_target(y, target):
    if y == target:
        return True
    else:
        return False


# ------------------------------------------------

# this function calculates neuron hit i.e yin
# ------------------------------------------------
def neuron_fire(weight_1, weight_2, input_1, input_2, bias):
    yin = (weight_1 * input_1) + (weight_2 * input_2) + bias
    return yin


# ------------------------------------------------

# this function checks the for all weights in updates weights list i.e function of stopping condition
# ------------------------------------------------
def check_equal(i_list):
    return i_list[1:] == i_list[:-1]


# ------------------------------------------------


# this is main function of perceptron algo
# ------------------------------------------------
def main():
    iterator = 0
    alpha = 1
    bias = 0
    flag = True
    input_1 = [1, 1, 0, 0]
    input_2 = [1, 0, 1, 0]
    target = [1, 1, 1, -1]
    updated_weights = [0, 0, 0, 0]
    weights = list()
    for i in range(0, 2):
        weights.append(rand.randint(-1000, 1000))
    print("Initial Weights and bias before learning Iterations")
    print("Bias =>", bias)
    print("Weights =>", weights)
    while flag:
        for i in range(0, 4):
            yin = neuron_fire(weights[0], weights[1], input_1[i], input_2[i], bias)
            y = activation_function(yin)
            if y == target[i]:
                updated_weights[i] = copy.deepcopy(weights)
            else:
                w1_new = weights[0] + change_in_weights(input_1[i], alpha, target[i])
                weights[0] = copy.deepcopy(w1_new)
                w2_new = weights[1] + change_in_weights(input_2[i], alpha, target[i])
                weights[1] = copy.deepcopy(w2_new)
                bias = change_in_bias(bias, alpha, target[i])
                updated_weights[i] = copy.deepcopy(weights)
        print("Updates Weights and bias after the Iteration ", iterator+1)
        print("Bias =>", bias)
        print("Weights =>", weights)
        iterator = iterator + 1
        if check_equal(updated_weights):
            flag = False
        else:
            flag = True


# ------------------------------------------------

if __name__ == "__main__":
    main()
