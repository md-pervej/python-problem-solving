
# -----78:Python Program to Differentiate Between type() and isinstance()-----

class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def sides_no(self):
        pass

poly=Polygon()
tri=Triangle()


print(type(tri)==Triangle)
print(type(tri)==Polygon)

print(isinstance(tri,Triangle))
print(isinstance(tri,Polygon))