# Imports
import copy

class GW:
    
    def __init__(
            self, 
            height=4, 
            width=4, 
            fwd_stochasticity=0.8, 
            start_state = (1,1),
            terminal_states=((4,4)),
            reward_default = 0.0,
            rewards = {
                (4,4) : 1.0,
                },
            ):
        self.height = height
        self.width = width
        self.fwd_stochasticity = fwd_stochasticity
        self.orth_stochasticity = (1.-self.fwd_stochasticity)/2
        self.start_state = start_state
        self.terminal_states = terminal_states
        self.reward_default = reward_default
        self.rewards = rewards
        
        self.dynamics = self._setup_dynamics()
    
        
    def _setup_dynamics(self):
        print("Test call was called")
        
        # Generate action list
        action_list = []
        if self.height > 1:
            action_list += ["up", "down"]
        if self.width > 1:
            action_list += ["left", "right"]
        
        action_result = {
            "up"    : (-1, 0),
            "down"  : ( 1, 0),
            "left"  : ( 0,-1),
            "right" : ( 0, 1),
            "stay"  : ( 0, 0),
            }
        action_stochasticity = {
            "up" : {
                action_result["stay"]   : 0.,
                action_result["up"]     : self.fwd_stochasticity,
                action_result["left"]   : self.orth_stochasticity,
                action_result["right"]  : self.orth_stochasticity,
                },
            "down" : {
                action_result["stay"]   : 0.,
                action_result["down"]   : self.fwd_stochasticity,
                action_result["left"]   : self.orth_stochasticity,
                action_result["right"]  : self.orth_stochasticity,
                },
            "left" : {
                action_result["stay"]   : 0.,
                action_result["left"]   : self.fwd_stochasticity,
                action_result["up"]     : self.orth_stochasticity,
                action_result["down"]   : self.orth_stochasticity,
                },
            "right" : {
                action_result["stay"]   : 0.,
                action_result["right"]  : self.fwd_stochasticity,
                action_result["up"]     : self.orth_stochasticity,
                action_result["down"]   : self.orth_stochasticity,
                },
            }
        
        # Generate base action dictionary
        base_dist_dict = {}
        for action in action_list:
            base_dist_dict[action] = []
        
        # Initialize empty dynamics dictionary
        dynamics = {}
        
        # Populate dynamics dictionary
        for i in range(1, self.height+1):
            for j in range(1, self.width+1):
                dist_dict = copy.deepcopy(base_dist_dict)
                
                for action in action_list:
                    
                    # Initialize temp spaces list
                    temp_spaces = []
                    
                    # Populate temp space list
                    for displacement in action_stochasticity[action]:
                        
                        # Determine space (new or same)
                        new_space = (i,j)                       
                        if (i,j) not in self.terminal_states:
                            new_space = (i + displacement[0], j + displacement[1])  
                        
                        """
                        if (i,j) in self.state_characteristics:
                            if self.state_characteristics[(i,j)] in ["Hole", "Goal"]:
                                new_space = (i,j)
                        """
                        
                        # Determine probability
                        new_prob = action_stochasticity[action][displacement]
                        
                        # Determine reward
                        new_reward = self.reward_default
                        if new_space in self.rewards:
                            new_reward = self.rewards[new_space]
                        
                        # Initialize terminality
                        new_term = False
                        if new_space in self.terminal_states:
                            new_term = True
                        
                        
                        """
                        if new_space in self.state_characteristics:
                            if self.state_characteristics[new_space] in ["Hole", "Goal"]:
                                new_term = True
                            if self.state_characteristics[new_space] in ["Goal"]:
                                new_reward = 1.
                        """
                                
                        temp_spaces.append([new_prob, new_space, new_reward, new_term])
                    
                    # Add non-legal space results to the base result of staying in place
                    for temp_space in temp_spaces:
                        if temp_space[1][0] < 1 or temp_space[1][0] > self.height or temp_space[1][1] < 1 or temp_space[1][1] > self.width:
                            for temp_space_bleh in temp_spaces:
                                if temp_space_bleh[1] == (i,j):
                                    temp_space_bleh[0] += temp_space[0]
                    
                    # Combine probabilitites of multiples of the same resulting state
                    for k in range(1,len(temp_spaces)):
                        for l in range(k):
                            if temp_spaces[k][1] == temp_spaces[l][1]:
                                temp_spaces[l][0] += temp_spaces[k][0]
                    
                    # Remove multiples with same state
                    temp_spaces_new_new = []
                    for k in range(0,len(temp_spaces)):
                        in_temp_spaces = False
                        for l in range(k):
                            if temp_spaces[k][1] == temp_spaces[l][1]:
                                in_temp_spaces = True
                        if in_temp_spaces != True:
                            temp_spaces_new_new.append(temp_spaces[k])
                    
                    # Remove zero probability and non-legal space
                    temp_spaces_new = []
                    for temp_space in temp_spaces_new_new:
                        if temp_space[0] <= 0.0 or temp_space[1][0] < 1 or temp_space[1][0] > self.height or temp_space[1][1] < 1 or temp_space[1][1] > self.width:
                            pass
                        else:
                            temp_spaces_new.append(tuple(temp_space))
                    
                    
                    dist_dict[action] = copy.deepcopy(temp_spaces_new)
                    
                dynamics[(i,j)] = dist_dict

        return dynamics
    
    def show_dynamics(self):
        
        # Clear console
        print("\033[H\033[J")
        
        # Show MDP dynamics in nicely organized output
        for state in self.dynamics:
            print("\n\n-----------------------------------\n")
            print(state)
            for action in self.dynamics[state]:
                print("\n", action)
                print(self.dynamics[state][action])
        
        return