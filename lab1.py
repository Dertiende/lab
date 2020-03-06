import random

##import networkx as nx

##g = nx.Graph()
##nodes = 10
##for i in range(nodes):
##    g.add_node(i)
##for i in range(nodes):
##    b = random.randint(1, nodes+1)
##    while i == b:
    ##    b = random.randint(1, nodes)
  ##  g.add_edge(i, b)
##print(g.edges())
##print(g.nodes())
from typing import Dict, Any, Union

graph: dict = {}


def orient_generate_edges(graph,nodes): #weak
    for i in range(nodes):

        for j in range (nodes):
            onodedges=[]
            numedges = random.randint(2, nodes)
            #print("numedge", numedges)
            lnodes = [q for q in range(nodes) if q!=i]
            #print("q",random.choice(lnodes))
            for k in range(numedges-1):
                #print("''",k)
                #print ("rr",p)
                onodedges.append(random.choice(lnodes))
                lnodes.remove(onodedges[k])
            graph[i] = onodedges
    return graph


def norient_generate_edges(graph,nodes): #strong
    for i in range(nodes):

        for j in range (nodes):
            onodedges=[]
            numedges = random.randint(2, nodes)
            #print("numedge", numedges)
            lnodes = [q for q in range(nodes) if q!=i]
            #print("q",random.choice(lnodes))
            for k in range(numedges-1):

                #print("''",k)
                #print ("rr",p)
                onodedges.append(random.choice(lnodes))
                lnodes.remove(onodedges[k])
            graph[i] = onodedges
            print(graph)
    for l in range(nodes):
        for m in graph[l]:
            #print("l",l)
            #print("before", graph[m])
            if graph[m].count(l)<1:
                graph[m]= graph[m]+[l]
            #print("after", graph[m])
    return graph

def orient_generate_edges_ves (graph,nodes): #weak
    for i in range(nodes):

        for j in range (nodes):
            onodedges=[]
            numedges = random.randint(2, nodes)
            #print("numedge", numedges)
            lnodes = [q for q in range(nodes) if q!=i]
            #print("q",random.choice(lnodes))
            for k in range(numedges-1):
                #print("''",k)
                #print ("rr",p)
                a = ''
                b =random.choice(lnodes)
                a= a+ str(b)+' - {**1**}'
                onodedges.append(a)
                lnodes.remove(b)
            graph[i] = onodedges
    return graph


def norient_generate_edges_ves(graph,nodes): #strong
    ves =[]
    for j in range (nodes):
        ves.append([])
        onodedges=[]
        numedges = random.randint(2, nodes)
        #print("numedge", numedges)
        lnodes = [q for q in range(nodes) if q!=j]
        #print("q",random.choice(lnodes))
        for k in range(numedges-1):

                #print("''",k)
                #print ("rr",p)

            b = random.choice(lnodes)
            vesint = random.randint(1,50)
            ves[j].append({b:vesint})
            a = ''
            a = a + str(b)+' *'+str(vesint)+'* '
            onodedges.append([b,'*'+str(vesint)+'*'])
            lnodes.remove(b)
            print("lnodes", lnodes)
        graph[j] = onodedges
        print(graph)
        print("ves", ves)
    for l in range(nodes):
        for m in range(len(graph[l])):
            #print("l",l)
            #print("before", graph[m])
            #for k in range(len(graph[l].get(m))):

            if graph[m][0] :
                graph[m] = graph[m]+[l]
            #print("after", graph[m])
    return graph

#def ns_con_generate_edges(): #not stated
#def generate_edges(graph):

    #edges = []
    # for each node in graph
    #for node in graph:

        # for each neighbour node of a single node
        #for neighbour in graph[node]:
            # if edge exists then append
            #edges.append((node, neighbour))
    #return edges
print(norient_generate_edges_ves (graph,5))
