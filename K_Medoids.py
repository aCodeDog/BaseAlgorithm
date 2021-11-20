%matplotlib inline
from matplotlib import pyplot
import numpy as np
from numpy import zeros, array, tile
from scipy.linalg import norm
import numpy.matlib as ml
import random
from sklearn.metrics.pairwise import pairwise_distances
from scipy.spatial import distance


def find_center(point,center,D):
    min_point = 0
    mindis = 10000
    for i in range(len(center)):
        if( mindis > D[point,int(center[i])] ):
            mindis = D[point,int(center[i])]
            min_point = int(center[i])
    return [min_point,mindis]


#k is the number of class
#x is the data  ,it's shape is [ [ x1 y1]
#                                [ x2 y2]
#                                ...
#                                [ xn yn] ]
          
def kmedoids(k,x):
    center = []
    dis = []
    mindis_p = []
    Dis = distance.cdist(x, x, 'euclidean')
    cluster_num = k
    point_num = len(x)
    if(point_num != len(Dis)):
        return print("dimension of Dis and x  is not same!")
    state = 1 
    n =1
    colour = ['r', 'b', 'g', 'y', ' c', 'm']
    for i in range(cluster_num):
        center = np.append(center,random.randint(0,point_num))
        dis = np.append(dis,0)
        mindis_p = np.append(mindis_p,0) 

    while state :
        state = 0
        plt.figure(n)
        point_attribute =[]
        for i in range(point_num):  
            k = find_center(i,center,Dis) #find the centre
            point_attribute = np.append(point_attribute,k[0])#class the point    
            for num in range(cluster_num):   
                if(k[0] == center[num]): #plot initial state and 
                    plt.plot(x[i][0],x[i][1],color=colour[num],markerfacecolor=colour[num],marker='o')
                    if(n == 1):# calculate the initial sum of cnetre[i] distance
                        dis[num] = dis[num]+ k[1]
        for i in range(cluster_num):#plot centre point
            plt.plot(x[int(center[i])][0],x[int(center[i])][1],color='k',markerfacecolor='k',marker='^')
        for i in range(cluster_num): #refresh centre
            #更新 k 个中心
            #print("circle_%d class_%d "%(n,i))
            for j in range(point_num): 
                distance = 0.0
                if(point_attribute[j] == center[i]): 
                    for l in range(point_num): #calculate class[i]-point[j] sum of distance
                        if(point_attribute[l] == center[i]): 
                            distance = distance + Dis[j,l] 
                    #print("circle_%d class_%d p_%d dis: %.2f  %.2f"%(n,i,j,distance,dis[i]))
                    if(distance < dis[i]):
                        print("circle_%d class_%d p_%d dis:%.2f %.2f"%(n,i,j,distance,dis[i]))
                        dis[i] = distance
                        mindis_p[i] = j
                        state = 1 #发生中心点移动    
            center[i] = mindis_p[i]  #更新第 i 个 center
        for i in range(cluster_num):#plot centre point
            print("circle_%d center %d: %d"%(n,i,center[i]))
        n=n+1 
        if( n >50 ):
            state = 0
