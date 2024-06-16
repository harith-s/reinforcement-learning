import numpy as np

state = np.zeros((4,4))
policy = np.array([['durl','durl','durl','durl'],['durl','durl','durl','durl'],['durl','durl','durl','durl'],['durl','durl','durl','durl']])


for k in range(10):
    new_state = state.copy()

    for i in range(4):
        for j in range(4):
            action = policy[i,j]
            adj = []
            if "d" in action: adj.append((i+1,j))
            if "u" in action: adj.append((i-1,j))
            if "r" in action: adj.append((i,j+1))
            if "l" in action: adj.append((i,j-1))

            for cell in adj:
                row, column = cell
                if row < 0: row = 0
                elif column < 0: column = 0
                if row == 4: row = 3
                elif column == 4: column = 3

                if (row,column) == (0,0) or (row, column) == (3,3): reward = 0
                else: reward = -1   
                

                new_state[i,j] += (1/len(adj))*(reward + 0.5*state[row, column])
    new_state[0,0] = 0
    new_state[3,3] = 0
    state = new_state
print(state)

for i in range(4):
    for j in range(4):
        temp = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
        adj = []
        for cell in temp:
            row, column = cell
            if row < 0: row = 0
            elif column < 0: column = 0
            if row == 4: row = 3
            elif column == 4: column = 3
            adj.append((row, column))
        l_imax = []
        imax = adj[0]
        for k in adj:

            if abs(state[k] - state[imax]) < 0.1:

                imax = k
                l_imax.append(k)
            elif state[k] > state[imax]:
                l_imax.clear()
                imax = k
                l_imax.append(imax)

            
            action = ''
        if (i+1,j) in l_imax: action += 'd'
        if (i-1,j) in l_imax: action += 'u'
        if (i,j+1) in l_imax: action += 'r'
        if (i,j-1) in l_imax: action += 'l'

        if imax == (i,j): action = 's'
        policy[i,j] = action
print(policy)

for k in range(10):
    new_state = state.copy()

    for i in range(4):
        for j in range(4):
            action = policy[i,j]
            adj = []
            if "d" in action: adj.append((i+1,j))
            if "u" in action: adj.append((i-1,j))
            if "r" in action: adj.append((i,j+1))
            if "l" in action: adj.append((i,j-1))

            for cell in adj:
                row, column = cell
                if row < 0: row = 0
                elif column < 0: column = 0
                if row == 4: row = 3
                elif column == 4: column = 3

                if (row,column) == (0,0) or (row, column) == (3,3): reward = 0
                else: reward = -1   
                

                new_state[i,j] += (1/len(adj))*(reward + 0.5*state[row, column])
    new_state[0,0] = 0
    new_state[3,3] = 0
    state = new_state
print(state)