import networkx as nx
import state_bird.data.read as read
import matplotlib.pyplot as plt

def get_events():
    events = read.get_events()
    return events

def get_states():
    states = read.get_states()
    return states
    
# Create a function that returns a graph of the current module
def get_graph():
    G = nx.MultiDiGraph()
    states = get_states()
    events = get_events()
    for state in states:
        #print(state)
        G.add_node(state[2])
    for event in events:
        #print(event)
        G.add_edge(event[3], event[4], name=event[2])
    # Draw a multidigraph and edges
    pos = nx.spring_layout(G, k=0.5)
    nx.draw_networkx(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=15, edge_color='black', linewidths=1, font_color='black')
    edge_labels = nx.get_edge_attributes(G, 'name')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=15, font_color='black')
    plt.show()
    
    return G

