# Imports
import copy

# Clear console
print("\033[H\033[J")

print("test")


"""
--------- Bandit Walk (BW) -----------

States : 0, 1, 2

|   0|   1|   2|
| H  | S  | G  |   (hole, start, goal)


Actions: 0, 1
    
<- 0 - Agent - 1 ->
Left         Right    (Deterministic)


"""
def P_BW ():
    """
    Descr
        Returns the Bandit Walk MDP (pg. 38, 60) as a Python dictionary
    """

    return {
        # STATE : Hole
        0 : {
        #   ACTION : Left
            0 :
        #   Probability distribution for state action pair (0,0) (Hole, Left)
             [
        #       Prob, s'  reward, terminal?
                 (1.0, 0, 0.0, True),
                ],
        #   ACTION : Right
            1 :
        #   Probability distribution for state action pair (0,1) (Hole, Right)
             [
        #       Prob, s'  reward, terminal?        
                (1.0, 0, 0.0, True),
                ],
        },
        # STATE : Start
        1 : {
        #   ACTION : Left
            0 : 
        #   Probability distribution for state action pair (1,0) (Start, Left)
            [
        #       Prob, s'  reward, terminal?
                (1.0, 0, 0.0, True),
                ],
        #   ACTION : Right
            1 : 
        #   Probability distribution for state action pair (1,1) (Start, Right)
            [
        #       Prob, s' reward, terminal?
                (1.0, 2, 1.0, True),
                ],
        },
        # STATE : Goal
        2 : {
        #   ACTION : Left
            0 :
        #   Probability distribution for state action pair (2,0) (Goal, Left)
             [
        #       Prob, s'  reward, terminal?
                 (1.0, 2, 0.0, True),
                ],
        #   ACTION : Right
            1 :
        #   Probability distribution for state action pair (2,1) (Goal, Right)
             [
        #       Prob, s'  reward, terminal?        
                (1.0, 2, 0.0, True),
                ],
        },
    }


"""
--------- Bandit Slippery Walk (BSW) -----------

States : 0, 1, 2

|   0|   1|   2|
| H  | S  | G  |   (hole, start, goal)


Actions: 0, 1
    
<- 0 - Agent - 1 ->
Left         Right    (Stochastic)


"""
def P_BSW():
    """
    Descr
        Returns the Bandit Slippery Walk MDP (pg. 40, 60) as a Python dictionary
    """

    return {
        # STATE : Hole
        0 : {
        #   ACTION : Left
            0 :
        #   Probability distribution for state action pair (0,0) (Hole, Left)
             [
        #       Prob, s'  reward, terminal?
                 (1.0, 0, 0.0, True),
                ],
        #   ACTION : Right
            1 :
        #   Probability distribution for state action pair (0,1) (Hole, Right)
             [
        #       Prob, s'  reward, terminal?        
                (1.0, 0, 0.0, True),
                ],
        },
        # STATE : Start
        1 : {
        #   ACTION : Left
            0 : 
        #   Probability distribution for state action pair (1,0) (Start, Left)
            [
        #       Prob, s'  reward, terminal?     Prob, s' reward, terminal?
                (0.8, 0, 0.0, True),            (0.2, 2, 1.0, True),
                ],
        #   ACTION : Right
            1 : 
        #   Probability distribution for state action pair (1,1) (Start, Right)
            [
        #       Prob, s'  reward, terminal?     Prob, s' reward, terminal?
                (0.8, 2, 1.0, True),            (0.2, 0, 0.0, True),
                ],
        },
        # STATE : Goal
        2 : {
        #   ACTION : Left
            0 :
        #   Probability distribution for state action pair (2,0) (Goal, Left)
             [
        #       Prob, s'  reward, terminal?
                 (1.0, 2, 0.0, True),
                ],
        #   ACTION : Right
            1 :
        #   Probability distribution for state action pair (2,1) (Goal, Right)
             [
        #       Prob, s'  reward, terminal?        
                (1.0, 2, 0.0, True),
                ],
        },
    }


"""
--------- Frozel Lake (FL) custom -----------

States : (1,1), (1,2), ..., (4,3), (4,4)

---------------------
| 1,1| 1,2| 1,3| 1,4|
| S  |    |    |    |   S : start
---------------------
| 2,1| 2,2| 2,3| 2,4|
|    | H  |    | H  |   H : hole
---------------------
| 3,1| 3,2| 3,3| 3,4|
|    |    |    | H  |
---------------------
| 4,1| 4,2| 4,3| 4,4|
| H  |    |    | G  |   G : goal
---------------------


Actions: Up, Down, Left, Right
        
        Up
         ^
         |
         |
<------Agent------>     (Stochastic)
Left     |    Right
         |
         v
        Down

"""
def P_FL_custom():
    
    # Generate action list
    action_list = ["up", "down", "left", "right"]
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
            action_result["up"]     : 1./3.,
            action_result["left"]   : 1./3.,
            action_result["right"]  : 1./3.,
            },
        "down" : {
            action_result["stay"]   : 0.,
            action_result["down"]   : 1./3.,
            action_result["left"]   : 1./3.,
            action_result["right"]  : 1./3.,
            },
        "left" : {
            action_result["stay"]   : 0.,
            action_result["left"]   : 1./3.,
            action_result["up"]     : 1./3.,
            action_result["down"]   : 1./3.,
            },
        "right" : {
            action_result["stay"]   : 0.,
            action_result["right"]  : 1./3.,
            action_result["up"]     : 1./3.,
            action_result["down"]   : 1./3.,
            },
        }
    
    # Generate base action dictionary
    base_dist_dict = {}
    for action in action_list:
        base_dist_dict[action] = []
    
    # Initialize state space characteristic dict
    state_characteristics = {
        (1,1) : "Start",
        (2,2) : "Hole",
        (2,4) : "Hole",
        (3,4) : "Hole",
        (4,1) : "Hole",
        (4,4) : "Goal",
        }
    
    # Initialize empty dynamics dictionary
    dynamics = {}
    
    # Populate dynamics dictionary
    for i in range(1,5):
        for j in range(1,5):
            dist_dict = copy.deepcopy(base_dist_dict)
            
            for action in action_list:
                
                # Initialize temp spaces list
                temp_spaces = []
                
                # Populate temp space list
                for displacement in action_stochasticity[action]:
                    new_space = (i + displacement[0], j + displacement[1])
                    new_prob = action_stochasticity[action][displacement]
                    new_term = False
                    new_reward = 0.
                    if new_space in state_characteristics:
                        if state_characteristics[new_space] in ["Hole", "Goal"]:
                            new_term = True
                        if state_characteristics[new_space] in ["Goal"]:
                            new_reward = 1.
                                        
                    temp_spaces.append([new_prob, new_space, new_reward, new_term])
                
                # Add non-legal space results to the base result of staying in place
                for temp_space in temp_spaces:
                    if temp_space[1][0] < 1 or temp_space[1][0] > 4 or temp_space[1][1] < 1 or temp_space[1][1] > 4:
                        for temp_space_bleh in temp_spaces:
                            if temp_space_bleh[1] == (i,j):
                                temp_space_bleh[0] += temp_space[0]
                
                # Remove zero probability and non-legal space
                temp_spaces_new = []
                for temp_space in temp_spaces:
                    if temp_space[0] <= 0.0 or temp_space[1][0] < 1 or temp_space[1][0] > 4 or temp_space[1][1] < 1 or temp_space[1][1] > 4:
                        pass
                    else:
                        temp_spaces_new.append(tuple(temp_space))
                
                
                dist_dict[action] = copy.deepcopy(temp_spaces_new)
                
            dynamics[(i,j)] = dist_dict

    return dynamics


def show_dynamics_dictionary(P_dict):
    
    for state in my_dict:
        print("\n\n-----------------------------------\n")
        print(state)
        for action in my_dict[state]:
            print("\n", action)
            print(my_dict[state][action])
    
    return 
    

my_dict = P_FL_custom()
show_dynamics_dictionary(my_dict)
