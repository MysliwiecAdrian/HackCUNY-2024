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

# Function to add markers for libraries using X and Y columns for longitude and latitude
def add_library_markers(map_object, data):
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['Y'], row['X']],  # Use Y for latitude and X for longitude
            popup=f"Library: {row['NAME']}",
            icon=folium.Icon(color='green')
        ).add_to(map_object)

# Add markers to the map
add_library_markers(mapNYC, libraries)


# Save the map
mapNYC.save(outfile="output.html")
