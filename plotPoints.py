import pandas as pd
import folium
from tqdm import tqdm
import numpy as np
import webbrowser
from folium import plugins

theInputData = "FullCleanDatasetPaths.csv"
##df = pd.read_csv(theInputData,header=[0],quotechar='"',skipinitialspace=True,sep="|")
df = pd.read_csv(theInputData,quotechar='"',skipinitialspace=True,sep=",")
print(df.head())
##df = df.head()


continueToMap = input("Write to map?")
if continueToMap[0]=="y":
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    print(df.head())
    map1 = folium.Map(
        location=[35.10557825769856, -106.62943653321837],
        tiles='Stamen Terrain',
        zoom_start=12,
    )
    colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred','lightred',
              'beige', 'darkblue', 'darkgreen', 'cadetblue',
              'darkpurple', 'white', 'pink','lightblue','lightgreen',
              'gray', 'black', 'lightgray']


    uniqueFlights = df['flight_id'].unique()
    ##print(uniqueFlights)
    colorCounter = 0
    for flight in uniqueFlights:
        lineColor = colors[colorCounter]
        miniDf = df.loc[df['flight_id'] == flight]
        uniqueFlightDate = miniDf['realDate'].unique()
        uniqueFlightDate = uniqueFlightDate[0]
        miniDf['new_col'] = list(zip(miniDf.latitude, miniDf.longitude))
        tupleList = tuple(list(miniDf['new_col']))
        folium.PolyLine(tupleList, color=lineColor, weight=2.5, opacity=1,popup = uniqueFlightDate).add_to(map1)
        if colorCounter == 18:
            colorCounter = 0
        else:
            colorCounter += 1
    map1
    map1.save("map_1.html")
    webbrowser.open("map_1.html")

##    print(miniDf.head())
##    print()
##                
##df['new_col'] = list(zip(df.latitude, df.longitude))
####print(df.head())
##tupleList = tuple(list(df['new_col']))
####print(tupleList)
                

##            
##
##
##continueToMap = input("Write to map?")
##if continueToMap[0]=="y":
####    df = Assaults
##    df['latitude'] = df['latitude'].astype(float)
##    df['longitude'] = df['longitude'].astype(float)
####    
####    df['marker_color'] = pd.cut(df['X202110.USAGE'], 4, labels=['green', 'blue','yellow', 'red'])
####    print("Working?")
####    print(df.head)
##    print(df.head())
##    map1 = folium.Map(
##        location=[35.10557825769856, -106.62943653321837],
##        tiles='Stamen Terrain',
##        zoom_start=12,
##    )
##    folium.PolyLine(tupleList, color="red", weight=2.5, opacity=1).add_to(map1)
####    df.apply(lambda row:folium.CircleMarker(location=[row["latitude"], row["longitude"]], popup=row["flight_id"],color=row['realDate'],radius=500).add_to(map1), axis=1)
##    map1
##    map1.save("map_1.html")
##    webbrowser.open("map_1.html")
