#Thompson Algorithm

#importing the lib.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#Implementing the UCB
import random
N = 10000
d = 9
ads_selected = []
numbers_of_reward_1 = [0] * d
numbers_of_reward_0 = [0] * d
total_reward = 0
for n in range(0,N):
    max_random = 0
    ad = 0
    for i in range(0,d):
        random_beta = random.betavariate(numbers_of_reward_1[i]+1,numbers_of_reward_0[i]+1)
        if(random_beta > max_random):
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n,ad]
    if reward == 1:
        numbers_of_reward_1[ad] = numbers_of_reward_1[ad] + 1
    else:
        numbers_of_reward_0[ad] = numbers_of_reward_0[ad] + 1
    total_reward = total_reward + reward
    
#Visualising the result
plt.hist(ads_selected)
plt.title('Histogram of ads selected')
plt.xlabel('Ads')
plt.ylabel('No. of times the ad was sel')
plt.show()