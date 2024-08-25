# Imports
#import gym, gym_walk
#import numpy as np

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
--------- Frozel Lake (FL) -----------

States : 0, 1, 2, ..., 15

---------------------
|   0|   1|   2|   3|
| S  |    |    |    |   S : start
---------------------
|   4|   5|   6|   7|
|    | H  |    | H  |   H : hole
---------------------
|   8|   9|  10|  11|
|    |    |    | H  |
---------------------
|  12|  13|  14|  15|
| H  |    |    | G  |   G : goal
---------------------


Actions: 0, 1, 2, 3 
        
        Up
         ^
         |
         0
         |
<--2---Agent---3-->     (Stochastic)
Left     |   Right
         1
         |
         v
        Down

"""
def P_FL():
    """
    Descr
        Returns the Frozel Lake MDP (pg. 46, 61) as a Python dictionary
    """
    return {
        # Corner
        0 : {
            0 : [(2./3., 0, 0.0, False), (1./3., 1, 0.0, False)],
            1 : [(1./3., 4, 0.0, False), (1./3., 0, 0.0, False), (1./3., 1, 0.0, False)],
            2 : [(2./3., 0, 0.0, False), (1./3., 4, 0.0, False)],
            3 : [(1./3., 1, 0.0, False), (1./3., 0, 0.0, False), (1./3., 4, 0.0, False)],
            },
        1 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        2 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        # Corner
        3 : {
            0 : [(2./3., 3, 0.0, False), (1./3., 2, 0.0, False)],
            1 : [(1./3., 7, 0.0,  True), (1./3., 3, 0.0, False), (1./3., 2, 0.0, False)],
            2 : [(1./3., 2, 0.0, False), (1./3., 3, 0.0, False), (1./3., 7, 0.0,  True)],
            3 : [(2./3., 3, 0.0, False), (1./3., 7, 0.0,  True)],
            },
        4 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        5 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        6 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        7 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        8 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        9 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        10 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        11 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        12 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        13 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        14 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        15 : {
            0 : [],
            1 : [],
            2 : [],
            3 : [],
            },
        }

# P = P_BW()
# P = gym.make('BanditWalk-v0').env.P
pass