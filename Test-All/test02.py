

class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def sides_no(self):
        pass

polygon=Polygon()
triangle=Triangle()

print(type(polygon)==Polygon)
print(type(triangle)==Polygon)

print(isinstance(polygon,Polygon))
print(isinstance(triangle,Polygon))