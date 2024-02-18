#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium
import re  # Import the regular expressions library

# Load library
libraries = pd.read_csv("library.csv")

# Initialize map (You can later set this dynamically based on user input)
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)


for index,row in libraries.iterrows():
    lat = row["Latitude"]
    long = row["Longitude"]
    folium.Marker([lat, long]).add_to(mapNYC)

# Add markers to the map
#add_library_markers(mapNYC, libraries)


# Save the map
mapNYC.save(outfile="output.html")
