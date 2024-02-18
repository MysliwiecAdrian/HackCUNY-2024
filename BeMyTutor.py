
#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pyarrow
import pandas as pd
import folium

mapNYC = folium.Map(location=[40.75,-74.125], zoom_start=10)

#tutors = pd.read_csv('mockTutorList.csv')
libraries = pd.read_csv('library.csv')

folium.Marker(location = [40.7420577, -74.0101494], icon=folium.Icon(icon='home')).add_to(mapNYC)
for index,row in libraries.iterrows():
    lat = row["Latitude"]
    long = row["Longitude"]
    folium.Marker([lat,long]).add_to(mapNYC)

mapNYC.save(outfile='output.html')
