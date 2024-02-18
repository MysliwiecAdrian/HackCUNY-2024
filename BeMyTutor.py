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
        # Assuming the CSV has 'Latitude' and 'Longitude' columns. Adjust the names as necessary.
        folium.Marker(
            location=[row['Latitude'], row['Longitude']],  # Update these column names based on your CSV structure
            popup=f"Library: {row['NAME']}",  # Assuming there's a 'NAME' column for the library's name
            icon=folium.Icon(icon='book')
        ).add_to(map_object)

# Add markers to the map
add_library_markers(mapNYC, libraries)


# Save the map
mapNYC.save(outfile="output.html")
