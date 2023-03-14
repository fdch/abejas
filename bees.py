from pythonosc import udp_client
from bees_algorithm import BeesAlgorithm
import benchmark_functions as bf

client = udp_client.SimpleUDPClient("127.0.0.1",3003)

b_func = bf.Schwefel(opposite=True, n_dimensions=3)

suggested_lowerbound, suggested_upperbound = b_func.suggested_bounds()

schwefel_bees_parameters = {'ns':0, 'nb':14, 'ne':1, 'nrb':5, 'nre':30, 'stlim':10}

alg = BeesAlgorithm(b_func, suggested_lowerbound, suggested_upperbound, **schwefel_bees_parameters)

while True:
    alg.performSingleStep()
    print(alg.current_sites[-1])
    x, y, z = alg.current_sites[-1].values
    client.send_message("/RoomEncoder/sourceX", str(x/500*15))
    client.send_message("/RoomEncoder/sourceY", str(y/500*15))
    client.send_message("/RoomEncoder/sourceZ", str(z/500*10))
    #client.send_message("/bee", map(lambda x:str(x/500*15),alg.current_sites[-1].values))
