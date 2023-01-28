import numpy as np
import copy, logging
from time import sleep
from .socket import send_to_socket
from pythonosc import udp_client

class BeesAlgorithm3D(BeesAlgorithm):
    def __init__(self, score_function, range_min, range_max, **kwargs):
        super().__init__(score_function, range_min, range_max, **kwargs)
        self.client = udp_client.SimpleUDPClient("localhost","3003")


    def compute_and_send(self):
        self.keep_bees_trace = True

        iteration = 0

        while True:
            iteration += 1
            self.performSingleStep()
            points_x, points_y, points_z = [], [], []
            for b in self.to_save_best_sites:
                points_x += [b.values[0]]
                points_y += [b.values[1]]
                points_z += [b.values[2]]
                for fs in self.to_save_foragers:
                    for f in fs:
                        points_x += [f.values[0]]
                        points_y += [f.values[1]]
                        points_z += [f.values[2]]

            for i, (x,y,z) in enumerate(zip(points_x, points_y, points_z)):
                self.client.send_message("/bee", i,x,y,z)
