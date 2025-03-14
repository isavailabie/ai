from collections import deque

def bfs(start):

    queue = deque([(start, 0)])

    states_list = {start} 
    while queue:
        state, steps = queue.popleft()

        if state == "12345678x":
            return steps 
        x_index = state.index('x')
        xx = x_index // 3  
        xy = x_index % 3
        state_list = list(state) 
        change = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        for dx, dy in change:
            newx, newy = xx + dx, xy + dy
            if 0 <= newx < 3 and 0 <= newy < 3: 
                new_x = newx * 3 + newy
                state_list[x_index], state_list[new_x] = state_list[new_x], state_list[x_index]
                new_state = ''.join(state_list) 

                if new_state not in states_list:
                    states_list.add(new_state)
                    queue.append((new_state, steps + 1))
                state_list[x_index], state_list[new_x] = state_list[new_x], state_list[x_index]

    return -1  

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
    print(bfs(start))
else:
    print(0)


