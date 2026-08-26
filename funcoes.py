# python 

função1 0.0024148999982571695
função1 0.0017143000004580244
função1 0.00156539999989036
função1 0.001769399999830057
função1 0.001523799999631592


# numpy 

função2 0.0005595000002358574
função2 0.0005667999994329875
função2 0.0005844999996043043
função2 0.0049902999999176245
função2 0.0020982000005460577
import timeit
import numpy as np


# def soma1 ():
#     lista =  list(range(1,2000))
#     print(lista)
#     return lista


# soma1()
# time = timeit.timeit(soma1, number=10)
# print('função1', time)


lista =  list(range(1,2000))
def soma():
    aleatorio1 =  np.array(lista)
    # print(aleatorio1)
    print(aleatorio1)
    return aleatorio1


time = timeit.timeit(soma, number=10)
print('função2', time)

