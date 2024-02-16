#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium

libraries = pd.read_csv("LIBRARY_20240216.csv")     # reads in CSV file with all library locations
mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)       # generates map of NYC

mapNYC.save(outfile = "output.html")        # saves the image as an html
