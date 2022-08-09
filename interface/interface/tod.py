from matplotlib import pyplot as plt



final = [['Source', 7, 1, 4, 3, 'Sink'], ['Source', 12, 11, 15, 'Sink'], ['Source', 9, 10, 16, 14, 12, 'Sink'], ['Source', 12, 11, 15, 13, 7, 6, 2, 5, 9, 10, 16, 14, 'Sink'], ['Source', 7, 1, 4, 3, 8, 6, 'Sink']]
pos_node = [['4.3', '4.8'], ['1.5', '4.7'], ['2.8', '4.9'], ['3.2', '4.2'], ['3.9', '2.8'], ['5.0', '3.4'], ['5.6', '4.6'], ['6.3', '4.8'], ['5.6', '5.9'], ['5.8', '6.9'], ['3.6', '5.3'], ['4.0', '6.8'], ['5.1', '8.0'], ['3.8', '7.4'], ['5.1', '6.9'], ['4.9', '6.2'], ['4.7', '5.5']]

def plot(path):
    route_id = 0
    color=['green','blue','purple','gray','cyan','pink','olive']
    for route in path:
        # print(path)
        pos_route=[]
        for j in range(len(route)):
            if route[j]=='Source' or route[j]=='Sink':
                route[j] = 0
            # print(route[j])
        print(route)
 

        for k in range(len(route)-1):
            # color = color[0:len(route)-1]
            x = int((float(pos_node[route[k]][0])*10))
            y = int((float(pos_node[route[k]][1])*10))
            

            if route[k]==0:
                plt.plot(x, y, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="red")
                
            else:
                plt.plot(x, y, marker="o", markersize=15, markeredgecolor="black", markerfacecolor="black")
            

            new_x = int((float(pos_node[route[k+1]][0])*10))
            new_y = int((float(pos_node[route[k+1]][1])*10))

            plt.plot([x, new_x], [y, new_y],color=color[route_id], linewidth=1)
        route_id+=1
    plt.show()


        
print(plot(final))