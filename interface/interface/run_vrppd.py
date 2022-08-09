#!/usr/bin/env python3
from vrp import VRPPD

vrppd = VRPPD()


def main():
    open = vrppd.open_config()
    adjMatrix = vrppd.adjacency_matrix()
    solver = vrppd.vrppd_solver(max_station=7,capacity=5)
    try:
        astar_path = vrppd.a_star_for_vehicle()
        print ("A* path =  " , astar_path)
        vrppd.plt_show(astar_path)
        # return astar_path
        
    except:
        return False
if __name__=="__main__":
    print(main())