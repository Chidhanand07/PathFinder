import osmnx as ox
import networkx as nx
import folium

# Define the bounding box coordinates (north, south, east, west)
north, south, east, west = 12.9200, 12.9000, 77.5200, 77.5000

# Extract the road network for the specified bounding box
G = ox.graph_from_bbox(north, south, east, west, network_type='drive')

# Plot the graph using osmnx
ox.plot_graph(G, node_size=0, edge_color='k', edge_linewidth=0.5)

# Define the coordinates for the start and end points
start_coords = (12.9103557, 77.5161732)
end_coords = (12.9123557, 77.5181732)

# Find the nearest nodes in the network to the start and end coordinates
start_node = ox.nearest_nodes(G, X=start_coords[1], Y=start_coords[0])
end_node = ox.nearest_nodes(G, X=end_coords[1], Y=end_coords[0])

# Compute the shortest path between the start and end nodes
route = nx.shortest_path(G, start_node, end_node, weight='length')

# Extract the coordinates of the nodes in the shortest path
route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

# Create a Folium map centered around the midpoint of the route
midpoint = ((start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2)
m = folium.Map(location=midpoint, zoom_start=15)

# Add markers for the start and end points
folium.Marker(location=start_coords, popup="Start", icon=folium.Icon(color="green")).add_to(m)
folium.Marker(location=end_coords, popup="End", icon=folium.Icon(color="red")).add_to(m)

# Draw the road path between the start and end points
folium.PolyLine(locations=route_coords, color='grey', weight=5).add_to(m)

# Save the map to an HTML file
m.save('road_highlighted_map.html')

# Optionally, display the map directly in a Jupyter notebook
# m
