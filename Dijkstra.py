from networkx import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt



def dijkstra(graph,src,dest,visited=[],distances={},predecessors={}):
       
    # gerer les execptions
    if src not in graph:
        raise TypeError('le chemin nexiste pas dans le graph')
    if dest not in graph:
        raise TypeError('la Noued Dest nexiste pas dans le graph ')    
    if src == dest:

        path=[]
        pred=dest
        while pred != None:
            path.append(pred)
            pred=predecessors.get(pred,None)
        print('Le plus cout chemin est : '+str(path[::-1])+" Cout="+str(distances[dest])) 
    else :     
        #si la premiere iteration on initialise la distance 
        if not visited: 
            distances[src]=0
        # visiter les voisins
        for neighbor in graph[src] :
            if neighbor not in visited:
                new_distance = distances[src] + graph[src][neighbor]
                if new_distance < distances.get(neighbor,float('inf')):
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = src
        # marquer les noeud visites 
        visited.append(src)                    
        unvisited={}
        for k in graph:
            if k not in visited:
                unvisited[k] = distances.get(k,float('inf'))        
        x=min(unvisited, key=unvisited.get)
        dijkstra(graph,x,dest,visited,distances,predecessors)

        


if __name__ == "__main__":

    graph =  {'Paris':{'Arras':185, 'Nantes':386, 'Lyon':465,'Poitiers':338, 'Brest':593}, 
             'Arras':{'Nantes':561, 'Strasbourg':522, 'Paris':185}, 
             'Nantes':{'Arras':561, 'Brest':298, 'Paris':386, 'Bordeaux':334}, 
             'Brest':{'Nantes':298, 'Paris':593}, 
             'Lyon':{'Paris':465, 'Strasbourg':494, 'Marseille':315,'Montpellier':303}, 
             'Strasbourg' :{'Arras':522, 'Lyon':494, 'Marseille':809, 'Montpellier':797}, 
             'Marseille':{'Lyon':315, 'Arras':809, 'Montpellier':171},
             'Montpellier' :{'Poitiers':338, 'Strasbourg':797, 'Marseille':171, 'Lyon':303},
             'Poitiers' :{'Paris':338, 'Bordeaux':237, 'Montpellier':557},
             'Bordeaux' :{'Poitiers':237,'Nantes':334}}

dijkstra (graph,'Paris','Strasbourg') 

 
'''
    graph = {'s': {'a': 2, 'b': 2},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}}
            
  dijkstra (graph,'s','c') 
'''