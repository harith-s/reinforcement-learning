import numpy as np
import pygame
import time

reward = np.array([[0,0,0,10],[0,0,-10,0],[0,0,0,0],[0,0,0,5]])

# stores the state values

state_val = np.zeros_like(reward).astype(float)

# policy dictates the actions, initially it just sweeps the grid

policy = np.array([['d','r','d','t'],['d', 'u','d','u'],['d', 'u','d','u'],['r', 'u','r','u']])

# evaluating the policy 

def policy_eval(state, policy):
    new_state = state.copy()
    for i in range(4):
        for j in range(4):

            action = policy[i,j]

            if action == 'd': row, column = i + 1, j
            elif action == 'u': row, column = i - 1, j
            elif action == 'r': row, column = i, j + 1
            elif action == 'l': row, column = i, j - 1
            elif action == 't': row, column = 0, 0  

            # changing the value of the state function
                    
            new_state[i,j] = reward[i,j] +  0.7*state[row, column]

    return new_state

# changing the policy after the state value function converges

def change_policy(state_val,policy):

    new_policy = np.zeros_like(policy)
    for i in range(4):
        for j in range(4):

            # checks the adjacent cells, eliminates out of bounds, and finds the maximums

            l  = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            l = [tup for tup in l if 0<= tup[0] < 4 and 0<= tup[1] < 4]
            imax = l[0]
            for k in l:
                if state_val[k] > state_val[imax]:
                    imax = k

            # assigning actions according to maximums

            if imax == (i+1,j): action = 'd'
            elif imax == (i-1,j): action = 'u'
            elif imax == (i,j+1): action = 'r'
            elif imax == (i,j-1): action = 'l'

            new_policy[i,j] = action

    return new_policy

def forloop_policy_iteration(state_val, policy):
    prev_state = state_val.copy()
    for j in range(100):
        for i in range(100):
            state_val = policy_eval(state_val, policy)
        print(state_val)
        policy = change_policy(state_val, policy)

    state_val = np.round(state_val,decimals=1, out=None)
    return policy,state_val

def policy_iteration(state_val, policy):

    for j in range(1000):

        prev_state = state_val.copy()
        state_val = policy_eval(state_val,policy)
        
        # checking whether the function converges or not

        while np.max(state_val - prev_state) > 0.00001:
            prev_state = state_val.copy()
            state_val = policy_eval(state_val, policy)

        # changing the policy after the state value function converges

        policy = change_policy(state_val, policy)

    state_val = np.round(state_val,decimals=1, out=None)
    return policy,state_val


def value_iternation(state_val, policy):
    for j in range(100):
        prev_state = state_val.copy()
        state_val = policy_eval(state_val,policy)
        
        # checking whether the function converges or not

        while np.max(state_val - prev_state) > 0.00001:
            state_val = policy_eval(state_val, policy)

            # changing the policy even before the function converges (value iteration)

            policy = change_policy(state_val, policy)

    state_val = np.round(state_val,decimals=1, out=None)
    return policy,state_val

start = time.time()
policy,state_val = policy_iteration(state_val,policy)
print(f"Time taken: {time.time() - start}")



# visualisation

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("path")

# text class for displaying reward value

class Text(pygame.sprite.Sprite):
    def __init__(self, text, where) -> None:
        super().__init__()
        self.font = pygame.font.Font(None, 30)
        self.image = self.font.render(text, True, "black")
        self.rect = self.image.get_rect(topleft = where)

running = True

#surface imports

up = pygame.image.load("up.png").convert_alpha()
down = pygame.image.load("down.png").convert_alpha()
right = pygame.image.load("right.png").convert_alpha()
left = pygame.image.load("left.png").convert_alpha()

map = {'d':down, 'u': up, 'l': left, 'r': right}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(4):
        for j in range(4):
            action = policy[i,j]
            image = map[action]

            rect = image.get_rect(topleft = (j*200,i*200))
            screen.blit(image, rect)

            value = Text(str(state_val[i,j]), ((j*200 + 25,i*200 + 25)))
            screen.blit(value.image, value.rect)

    pygame.display.update()
