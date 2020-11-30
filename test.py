# =============================================== #
# === Google FooBar challenge Level 3, part 1 === #
# =============================================== #



# Bomb, Baby!
# ===========
# 
# You're so close to destroying the LAMBCHOP doomsday device you can taste it! But in order to do so, you need to deploy special self-replicating bombs designed for you by the brightest scientists on Bunny Planet. There are two types: Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings, will automatically deploy to all the strategic points you've identified and destroy them at the same time. 
# 
# But there's a few catches. First, the bombs self-replicate via one of two distinct processes: 
# Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
# Every Facula bomb spontaneously creates a Mach bomb.
# 
# For example, if you had 3 Mach bombs and 2 Facula bombs, they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs. The replication process can be changed each cycle. 
#
# Second, you need to ensure that you have exactly the right number of Mach and Facula bombs to destroy the LAMBCHOP device. Too few, and the device might survive. Too many, and you might overload the mass capacitors and create a singularity at the heart of the space station - not good! 
#
# And finally, you were only able to smuggle one of each type of bomb - one Mach, one Facula - aboard the ship when you arrived, so that's all you have to start with. (Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP, but that's not going to stop you from trying!) 
#
# You need to know how many replication cycles (generations) it will take to generate the correct amount of bombs to destroy the LAMBCHOP. Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed. Return the fewest number of generations (as a string) that need to pass before you'll have the exact number of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done! M and F will be string representations of positive integers no larger than 10^50. For example, if M = "2" and F = "1", one generation would need to pass, so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.


import time
start = time.time()

resFast = ['Fast Results']
res = ['Results']


def solutionFast(x, y):
    itrs = 0
    x2, y2 = int(x), int(y)
    x = max(x2, y2)
    y = min(x2, y2)
    if x % 2 == 0 and y % 2 == 0:
        print(x, y)
        return 'impossible'

    while x > 0 and y > 0:
        print('FAST')
        if y == 1:
            return str(int(itrs + (x-1)))
        if x == 1:
            return str(int(itrs + (y-1)))

        if x > (y*10):
            r = x % y
            itrs += (max(x, y) - r) / min(x, y)+1
            x = r
            y = max(x, y) - min(x, y)

        else:
            if x >= y:
                x -= y
                itrs += 1
            else:
                y -= x
                itrs += 1
    return 'impossible'


# -- Python cases -- # 
# print('Answer: 4', 'Solution:', solution('4', '7'))
# print('Answer: 1', 'Solution:', solution('2', '1'))
# print('Answer: 0', 'Solution:', solution('1', '1'))
# print('Answer: 25', 'Solution:', solution('567', '32'))
# print('Answer: 699999', 'Solution:', solution('7'+'0'*5, '1'))
# 
# print('Answer: 142857151', 'Solution:', solution('7'+'0'*9, '4'+'9'*9))
# 
# print('Answer: impossible', 'Solution:', solution('2', '4'))
# print('Answer: impossible:', 'Solution:', solution('1', '0'))
# print('Answer: impossible', 'Solution:', solution('-3', '7'))
# print('Answer: impossible', 'Solution:', solution('0', '0'))



print(time.time() - start)








