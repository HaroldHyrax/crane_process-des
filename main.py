import simpy
import math

"""
General design idea:
Classes for each actionable process or resource eg. Crane, Station objects
Collections of each set of proceses eg. Cranes, Stations collections of objects
All objects carry a list of tags identifying for which process sets it is viable,
the process sets can then be specified by the job process for each action.
Managers for each set of actionable process or resource, that can iterate over collections, find the best available 
item to carry out a task, assign it and update the necessary variables.
Job calls are made to managers, managers to objects

"""

class JiggingStation:

    def __init__(self, env, x, y):
        self.env = env
        self.x = x
        self.y = y

    def jig(self, jig_time):
        #jigging process
        yield env.timeout(jig_time)

class Mobile:

    def __init__(self, env, x, y, moves_x, moves_y, move_speed):
        self.env = env
        self.x = x
        self.y = y
        self.moves_x = moves_x
        self.moves_y = moves_y
        self.move_speed = move_speed

    def move_to(self, x_destination, y_destination):
        # move to (x_destination, y_destination)
        x_delta = x_destination - self.x
        y_delta = y_destination - self.y
        distance = math.sqrt(x_delta**2 + y_delta**2)
        move_time = distance/self.move_speed
        # check if other cranes are in the way

    def pick_up(self, x_loc, y_loc):
        yield self.move_to(x_loc, y_loc)

class MobileHandler:
    def __init__(self, env):
        self.env = env

class Job:

    def __init__(self, env):
        self.env = env
        self.action = env.process(self.process())

    def process(self, env, batch, jig_time):
        job_number = batch
        while True:
            # wait for jigging station
            # wait for flybar
            # move to jigging station (release crane or not) 
            # jig job
            # request move to degrease
            # degrease
            # request pickle tank
            # request pickup and move to rinse
            # rinse
            # request move to pickle tank
            # pickle
            # request flux tank
            # request pickup and move to rinse
            # rinse
            # request move to flux
            # flux
            # request dryer position
            # move to dryer

            

env = simpy.Environment()


env.run(until=50)