#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium
import re  # Import the regular expressions library

# Load library and tutor data
libraries = pd.read_csv("library.csv")
tutors = pd.read_csv("mockTutorList.csv")

# Initialize map (You can later set this dynamically based on user input)
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)

# Function to extract latitude and longitude from the_geom column
def extract_lat_lon(the_geom):
    match = re.search(r'POINT \((-?\d+\.\d+) (-?\d+\.\d+)\)', the_geom)
    if match:
        return float(match.group(2)), float(match.group(1))  # Latitude, Longitude
    return None, None

# Function to add markers for libraries
def add_library_markers(map_object, data):
    for index, row in data.iterrows():
        latitude, longitude = extract_lat_lon(row['the_geom'])  # Use extract_lat_lon function
        if latitude and longitude:
            folium.Marker(
                location=[latitude, longitude],
                popup=f"Library: {row['NAME']}",
                icon=folium.Icon(color='blue', icon='book')
            ).add_to(map_object)

# Function to add markers for tutors
def add_tutor_markers(map_object, data):
    for index, row in data.iterrows():
        # Assuming 'X' and 'Y' columns exist for tutors with proper lat/lon data
        folium.Marker(
            location=[row['X'], row['Y']],
            popup=f"Tutor: {row['NAME']} - {row['SUBJECT']}",
            icon=folium.Icon(color='green', icon='graduation-cap', prefix='fa')
        ).add_to(map_object)

# Add markers to the map
add_library_markers(mapNYC, libraries)
add_tutor_markers(mapNYC, tutors)

# Save the map
mapNYC.save(outfile="output.html")
