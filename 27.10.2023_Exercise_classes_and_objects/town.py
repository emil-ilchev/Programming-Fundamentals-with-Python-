class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longitude = "0°E"

    def set_latitude(self, latitude: str):
        self.latitude = latitude

    def set_longitude(self, longitude: str):
        self.longitude = longitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"

town = Town("Sofia")
town1 = Town("Kiova")
town2 = Town("Oslo")
town2.set_latitude("12° 41\' 44.04\" N")
town2.set_longitude("35° 19\' 15.94\" E")
town1.set_latitude("85° 41\' 88.04\" N")
town1.set_longitude("65° 19\' 55.94\" E")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town1)
print(town)
print(town2)
