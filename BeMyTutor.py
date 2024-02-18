#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium

# Path to your CSV file
csv_file = "library.csv"

# Read the CSV file using Pandas
data = pd.read_csv(csv_file)

# Initialize a Folium map. The location is a list [latitude, longitude], and zoom_start is the initial zoom level.
# Adjust the location and zoom_start as needed, possibly to the average of your points for centering.
map = folium.Map(location=[40.7128, -74.0060], zoom_start=10)

# Function to add markers to the map
def add_markers(map_object, df):
    for _, row in df.iterrows():
        # Extracting Latitude, Longitude, and Name
        latitude = row['X']
        longitude = row['Y']
        name = row['Name']  # Adjust this if your CSV uses a different column name for the location name

        # Adding a marker to the map
        folium.Marker(
            location=[latitude, longitude],
            popup=name,
            icon=folium.Icon(icon='info-sign', color='blue')  # You can customize the icon and color
        ).add_to(map_object)

# Add markers to the map
add_markers(map, data)

# Save the map to an HTML file
map.save('output.html')
