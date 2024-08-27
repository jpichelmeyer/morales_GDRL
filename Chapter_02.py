# Imports
from gridworld import GW


# Clear console
print("\033[H\033[J")


"""
--------- Bandit Walk (BW) -----------

States : (1,1), (1,2), (1,3)

| 1,1| 1,2| 1,3|
| H  | S  | G  |   (hole, start, goal)


Actions: left, right
    
<----- Agent ----->
Left         Right    (Deterministic)


"""
GW_BW = GW(
    width=3, 
    height=1, 
    fwd_stochasticity=1.,
    start_state=(1,2),
    terminal_states=((1,1),(1,3)),
    reward_default=0.0,
    rewards={
        (1,3) : 1.0,
        }
    )
# GW_BW.show_dynamics()


"""
--------- Bandit Slippery Walk (BSW) -----------

States : (1,1), (1,2), (1,3)

| 1,1| 1,2| 1,3|
| H  | S  | G  |   (hole, start, goal)


Actions: left, right
    
<----- Agent ----->
Left         Right    (Stochastic : 0.8 intended way, 0.2 opposite)


"""
GW_BSW = GW(
    width=3, 
    height=1, 
    fwd_stochasticity=0.8,
    start_state=(1,1),
    terminal_states=((1,1),(1,3)),
    reward_default=0.0,
    rewards={
        (1,3) : 1.0,
        }
    )
# GW_BSW.show_dynamics()


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
<------Agent------>     (Stochastic : 1/3 intended way, 1/3 orthogonal left, 1/3 orthogonal right)
Left     |    Right
         |
         v
        Down

"""

GW_FL = GW(
    width=4, 
    height=4, 
    fwd_stochasticity=1./3.,
    start_state=(1,1),
    terminal_states=((2,2),(2,4),(3,4),(4,1),(4,4)),
    reward_default=0.0,
    rewards={
        (4,4) : 1.0,
        }
    )
# GW_FL.show_dynamics()