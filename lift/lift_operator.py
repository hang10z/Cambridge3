__author__ = 'demi'

import lift

#create a lift object
my_lift = lift.Lift()

#Find out what floor its on

floor = my_lift.get_floor()
print("The lift is on floor", floor)

# move lift to different floor

my_lift.move_to_floor(5)

#Find out where the lift is now

floor = my_lift.get_floor()
print("The lift is on floor", floor)



