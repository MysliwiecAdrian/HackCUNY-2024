#HackCUNY 2024
#Be My Tutor
#Adrian Mysliwiec & Rosa Rivera

import pandas as pd
import folium

libraries = pd.read_csv("LIBRARY_20240216.csv")                     # reads in CSV file with all library locations
tutors = pd.read_csv("mockTutorList.csv")                           # reads in the list of tutors and their locations

# borough = str(input("Enter the borough of choosing"))             # wasn't sure on the plans but i just kept it here
# mapNYC = folium.Map(location=[40.75, -74.125], zoom_start=10)     # generates map of NYC (was thinking to make the location change based on the borough of choice)

# plot out all the libraries in that specific borough
# need to add an overlapping marker or something so that information for the tutors currently there
# looking into making the markers time sensitive? if its even possible  

mapNYC.save(outfile = "output.html")                                # saves the image as an html
