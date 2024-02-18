#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium
from datetime import datetime

# Current system time
now = datetime.now()
current_hour = now.hour

# Initialize the map
mapNYC = folium.Map(location=[40.69, -73.88], zoom_start=10)

# Load data
tutors = pd.read_csv('mockTutorList.csv')
libraries = pd.read_csv('library.csv')


# Function to add markers, with time checking inside
def add_markers(map_object, dataframe, icon_type, popup_text):
  for index, row in dataframe.iterrows():
    lat = row["Latitude"] if "Latitude" in row else row["LATITUDE"]
    long = row["Longitude"] if "Longitude" in row else row["LONGITUDE"]
    name = row["name"] if "name" in row else row["NAME"]
    subj = row["SUBJECT"] if "SUBJECT" in row else ""

    if 9 <= current_hour < 17:
      folium.Marker([lat, long],
                    popup=f"{name}{', ' + subj if subj else ''}",
                    icon=folium.Icon(icon=icon_type,
                                     color='green')).add_to(map_object)
    else:
      folium.Marker([lat, long],
                    popup="CLOSED",
                    icon=folium.Icon(icon="ban-circle",
                                     color='red')).add_to(map_object)


# Add markers for libraries and tutors for the current time interval
add_markers(mapNYC, libraries, "book", "name")
add_markers(mapNYC, tutors, "user", "NAME, SUBJECT")

# Save the map
mapNYC.save(outfile='output.html')
