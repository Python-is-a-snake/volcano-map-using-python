import folium,pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#changing color of the mark depending on elevation 
def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" Meters", icon=folium.Icon(color=color_producer(el))))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read()))

map.add_child(fg)

map.save("Map1.html")