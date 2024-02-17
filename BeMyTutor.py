#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium

# Load library and tutor data
libraries = pd.read_csv("LIBRARY_20240216.csv")
tutors = pd.read_csv("mockTutorList.csv")

# Initialize map (You can later set this dynamically based on user input)
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)

# Function to add markers for libraries
def add_library_markers(map_object, data):
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Library: {row['name']}",
            icon=folium.Icon(color='blue', icon='book')
        ).add_to(map_object)

# Function to add markers for tutors
def add_tutor_markers(map_object, data):
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"Tutor: {row['name']} - {row['subject']}",
            icon=folium.Icon(color='green', icon='graduation-cap', prefix='fa')
        ).add_to(map_object)

# Add markers to the map
add_library_markers(mapNYC, libraries)
add_tutor_markers(mapNYC, tutors)

# Save the map
mapNYC.save(outfile="output.html")
