import geocoder
import folium
loc_1=input("Enter your ip address")
g=geocoder.ip(loc_1)
myAddress=g.latlng
my_map1=folium.Map(location=myAddress,
                   zoom_control=100)
folium.CircleMarker(location=myAddress,radius=50).add_to(my_map1)

folium.Marker(myAddress).add_to(my_map1)
my_map1.save('my_map.html')
