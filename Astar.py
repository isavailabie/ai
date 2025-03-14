from heapq import heappop, heappush

def h(state):
    dist = 0
    tp = {'1': (0, 0),'2': (0, 1),'3': (0, 2),'4': (1, 0),'5': (1, 1),'6': (1, 2),'7': (2, 0),'8': (2, 1),'x': (2, 2)}

    for i in range(len(state)):
        char = state[i]
        x = i // 3 
        y = i % 3  
        tx, ty = tp[char]
        dist += abs(x - tx) + abs(y - ty)
    return dist

def astar(start):
    directions = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}
    queue = [(h(start), 0,  start, "")]
    states = {start}

    while queue:
        hh, steps,state, path = heappop(queue)

        if state == '12345678x':
            return path  
        x_index = state.index('x')
        x, y = x_index // 3, x_index % 3

        for move, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nx_index = nx * 3 + ny
                state_list = list(state)
                state_list[x_index], state_list[nx_index] = state_list[nx_index], state_list[x_index]
                new_state = ''.join(state_list)

                if new_state not in states:
                    states.add(new_state)
                    heappush(queue, (steps + 1 + h(new_state), steps + 1,  new_state, path + move))

    return "unsolvable"  

def countin(li):
    li.remove('x') 
    count = 0
    for i in range(len(li)):
        for j in range(i + 1, len(li)):
            if li[i] > li[j]:
                count += 1
    return count

li = input().split()
a2= li.copy()
rx = 3-(li.index('x')//3)
inv_count = countin(li)
if (inv_count + rx) % 2 == 0:
    start = ''.join(a2)  
    print(astar(start))
else:
    print("unsolvable")

