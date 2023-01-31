from pythonosc import udp_client
from bees_algorithm import BeesAlgorithm
import benchmark_functions as bf

client = udp_client.SimpleUDPClient("localhost",3003)

b_func = bf.Schwefel(opposite=True, n_dimensions=3)

suggested_lowerbound, suggested_upperbound = b_func.suggested_bounds()

schwefel_bees_parameters = {'ns':0, 'nb':14, 'ne':1, 'nrb':5, 'nre':30, 'stlim':10}

alg = BeesAlgorithm(b_func, suggested_lowerbound, suggested_upperbound, **schwefel_bees_parameters)

while True:
    alg.performSingleStep()
    client.send_message("/bee", map(lambda x:str(x/500*15),alg.current_sites[-1].values))
