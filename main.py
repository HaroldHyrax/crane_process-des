import simpy

class JiggingStation:
    
    def __init__(self, env, x, y):
        self.env = env
        self.x = x
        self.y = y

    def jig(self, jig_time):
        #jigging process
        yield env.timeout(jig_time)

class Mobile:

    def __init__(self, env, x, y, moves_x, moves_y, move_speed_x, move_speed_y):
        self.env = env
        self.x = x
        self.y = y
        self.moves_x = moves_x
        self.moves_y = moves_y
        self.move_speed_x = move_speed_x
        self.move_speed_y = move_speed_y

    def move_to(self, x_destination, y_destination):
        # move to (x_destination, y_destination)

        # check if other cranes are in the way

    def pick_up(self, x_loc, y_loc):
        yield self.move_to(x_loc, y_loc)


job_iterator = 0

def job(env, batch, jig_time):
    job_number = batch
    while True:
        # wait for jigging station
        print("Job {} waiting for jigging station (time:{})".format(job_number, env.now))
        jigging_station = yield jigging_stations.get()
        # wait for flybar
        print("Job {} waiting for flybar at jigging station {} (time:{})"
            .format(job_number, jigging_station, env.now))
        flybar = yield flybar_store.get()
        # jig job
        print("Job {} being jigged onto flybar {} (time:{})".format(job_number, flybar, env.now))
        yield env.timeout(jig_time)


        yield flybar_store.put(flybar)
        yield jigging_stations.put(jigging_station)

env = simpy.Environment()

flybar_store = simpy.Store(env)
jigging_stations = simpy.Store(env)

env.run(until=50)