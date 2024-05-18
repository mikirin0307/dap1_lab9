class Agent():
    def __init__(self, x, y, id):
        self.id = id
        self.x = x
        self.y = y 

    def update(self, x, y):
        self.x = x 
        self.y = y 


class World():
    def __init__(self, x, y):
        self.grid = {}
        self.ax = x 
        self.ay = y
        for i in range(x):
            for j in range(y):
                self.grid[(i, j)] = None 
        self.agents = {}
        
    def find_empty_patch(self):
        ret = []
        for key, val in self.grid.items():
            if not val:
                ret.append(key)

        return ret 
    
    def add_agent(self, x, y, agent):
        if agent.id in self.agents:
            print("Agent already exists in this world")
            return 1
        
        if not (0 <= x < self.ax and 0 <= y < self.ay):
            print("Invalid coordinate")
            return 1 

        if self.grid[(x, y)]:
            print("Non-empty space")
            return 1
        
        self.grid[(x, y)] = agent
        self.agents[agent.id] = (x, y)
        
    def move_agent(self, x, y, agent):
        if agent not in self.agents:
            print("Agent doesn't exist")
            return 1
        
        if not (0 <= x < self.ax and 0 <= y < self.ay):
            print("Invalid coordinate")
            return 1

        if self.grid[(x, y)]:
            print("Non-empty space")
            return 1
        
        old_x, old_y = self.agents[agent.id]
        self.grid[(old_x, old_y)] = None 
        
        self.grid[(x, y)] = agent 
        self.agents[agent.id] = (x,y)

def simualte():

    world = World(5, 5)
    num_agents = int(input("how many agents"))
    list_agents = []
    for i in range(num_agents):
        empty_patches = world.find_empty_patch
        print("current empty patches:")
        print(empty_patches)

        init_x = int(input(f"initial x location for agent {i}"))
        init_y = int(input(f"initial y location for agent {i}"))
        curr_agent = Agent(init_x, init_y, i)
        list_agents.append(curr_agent)

        world.add_agent(init_x, init_y, curr_agent)

    while(True):

        end = input('End? y/n')
        if end == 'y':
            break 

        for i in range(num_agents):
            curr_empty_patches = world.find_empty_patch
            print("current empty patches:")
            print(curr_empty_patches)

            new_x = int(input(f"initial x location for agent {i}"))
            new_y = int(input(f"initial y location for agent {i}"))

            if world.move_agent(new_x, new_y, list_agents[i]):
                print("Error")
                continue 
            list_agents[i].update(new_x, new_y)
            

