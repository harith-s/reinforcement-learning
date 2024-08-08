import numpy as np
import matplotlib.pyplot as plt
import time
f = open("log.txt", "w")

# - Gaussian Distribution with mean reward 0 and variance 1
# - Fair Coin Toss with a reward of +3 for head and -4 for tail
# - Poisson Distribution with variance in reward 2
# - Gaussian Distribution with mean reward +1 and variance 2
# - Exponential Distribution with mean reward +1
# - The last but not the least, this button chooses any of the previous options with equal probability
    
def reward_function(choice):
    if choice == 0:
        return np.random.normal(0,1)
    elif choice == 1:
        return np.random.choice([3,-4])
    elif choice == 2:
        return np.random.poisson(2.0)
    elif choice == 3:
        return np.random.normal(1,2)
    elif choice == 4:
        return np.random.exponential(1)
    elif choice == 5:
        return reward_function(np.random.randint(0,4))

def choose_button(state, epsilon=0, i = 0):

    if np.random.rand() < epsilon or i < 7:
        # print("Random", end = " ")
        return np.random.randint(0,5)
    
    else:
        max = np.max(state[:,0])
        # f.write(f"{state}\n")
        l_max = []
        for nrow in range(state.shape[0]):
            if state[nrow][0] == max:
                l_max.append(nrow)
    
        return np.random.choice(l_max)
        # return np.argmax(state[:,0])

# reward array -> along x axis steps vary

def main(epsilon, reward_array):
    state = np.zeros((6,2))
    tot_reward = 0  
    for i in range(1000):

        # choosing the button

        if np.random.rand() < epsilon or i < 7: choice = np.random.randint(0,5)
        else: 
            max = np.max(state[:,0])
            l_max = []
            for nrow in range(state.shape[0]):
                if state[nrow][0] == max:
                    l_max.append(nrow)
    
            choice = np.random.choice(l_max)

        # reward according to choice

        if choice == 0: reward = np.random.normal(0,1)
        elif choice == 1: reward= np.random.choice([3,-4])
        elif choice == 2: reward =np.random.poisson(2.0)
        elif choice == 3: reward =np.random.normal(1,2)
        elif choice == 4: reward =np.random.exponential(1)
        elif choice == 5: reward = reward_function(np.random.randint(0,4))

        # adding the reward to the reward array according to the step it was present in

        reward_array[i] += reward
        tot_reward += reward
        state[choice][1] += 1
        state[choice][0] = state[choice][0] + ((reward - state[choice][0]) / state[choice][1])

if __name__ == "__main__":
    l  = []
    start = time.time()
    l_ep = [0,0.01,0.1]
    x = np.arange(1,1001)
    for j in range(len(l_ep)):
        print(j)
        epsilon = l_ep[j]
        reward_array = np.zeros(1000)
        for i in range(10000):
            main(epsilon, reward_array)
        l.append(reward_array/10000)
    
    plt.title("Assignment 1")
    plt.xlabel("Steps")
    plt.ylabel("Average reward")
    for i in range(len(l_ep)):
        plt.plot(x,l[i], label = f"e = {l_ep[i]}")
    plt.legend()
    print(f"Time taken: {time.time() - start} seconds")
    plt.show()







# def main(epsilon, steps):
#     tot_reward = 0
#     array_rewards = np.zeros(1000)
#     state = np.zeros((6,2))
#     for i in range(1000):
#         # choice = choose_button(state,epsilon,i)
#         if np.random.rand() < epsilon or i < 7: choice = np.random.randint(0,5)
#         else: choice = np.argmax(state[:,0])
#         # print(choice)
#         # reward = reward_function(choice)
#         if choice == 0: reward = np.random.normal(0,1)
#         elif choice == 1: reward= np.random.choice([3,-4])
#         elif choice == 2: reward =np.random.poisson(2.0)
#         elif choice == 3: reward =np.random.normal(1,2)
#         elif choice == 4: reward =np.random.exponential(1)
#         elif choice == 5: reward = reward_function(np.random.randint(0,4))
#         tot_reward += reward
#         state[choice][1] += 1
#         state[choice][0] = state[choice][0] + ((reward - state[choice][0]) / state[choice][1])
#         array_avgRewards[i] = (tot_reward/(i+1))
#     return tot_reward/steps

# if __name__ == "__main__":
#     l  = []
#     start = time.time()
#     max_mean = 0
#     max_ep = 0
#     # l_ep = np.arange(0,0.2,0.01)
#     l_ep = [0]
#     x = np.arange(1,501)
#     for j in range(len(l_ep)):
#         epsilon = l_ep[j]
#         temp = []
#             # print(step_count)
#         totRewardOverEp = 0
#         for i in range(1000):
#                 totRewardOverEp += main(epsilon, step_count)
#         temp.append(totRewardOverEp/1000)
#         # array = np.array(temp)
#         # print(f"Mean: {np.mean(array)}")
#         # if max_mean < np.mean(array):
#         #     max_mean = np.mean(array)
#         #     max_ep = epsilon

#         l.append(temp)
    
#     # plt.title("Assignment 1")
#     # plt.xlabel("Episode")
#     # plt.ylabel("Total reward at end of episode")
#     # # for i in range(len(l_ep)):
#     #     # plt.plot(x,l[i], label = f"e = {l_ep[i]}")
#     # plt.legend()
#     print(f"Time taken: {time.time() - start} seconds")
#     plt.show()
