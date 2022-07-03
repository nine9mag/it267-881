from cmath import polar
from time import time, timezone


class Geographic:
    def setcordinate(self,lat,long):
        self.latitude = lat
        self.longitude = long

    def getcordinate(self):
        return f'Latitude: {self.latitude}\nLongitude: {self.longitude}'

    def gettimezone(self):
        timezone = round(self.longitude/12 - 1)
        if timezone > 0 :
            return f'TimeZone+{timezone}'
        else:
            return f'TimeZone{timezone}' 
    def getclimate(self):
        if self.latitude<= -66.5 or self.latitude >= 66.5 :
            return 'Polar Zone'
        elif self.latitude <= -23.5 or self.latitude >=23.5 :
            return 'Temperate Zone'
        else:
            return 'Tropical Zone'