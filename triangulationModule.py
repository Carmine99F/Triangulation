from shapely.geometry import Polygon as Poli
from shapely.geometry import MultiPoint
from shapely.geometry import Polygon as Poli
from shapely.ops import triangulate
import numpy as np



def traingulatePolygon(coordinates):
    if(len(coordinates)>=2):
        pointsCoordinate=np.array(coordinates)
        #print("Tipo cordinate ",type(pointsCoordinate), pointsCoordinate)
        points = MultiPoint(points=list(pointsCoordinate))
        #print("Point ",type(points))
        poly = Poli([[p.x, p.y] for p in points]) #crea un oggetto Polygon data una serie di coordinate
        #print(poly.wkt)   prints: 'POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))'
        triangles=triangulate(points)
        arrayTriangles=[]
        for triangle in triangles:
            if triangle.within(poly):
                pilitriangle=Poli(triangle)
                arrayTriangles.append(list(pilitriangle.exterior.coords))
            else:
                print("Non è interno")
        array3DTriangles=np.array(arrayTriangles)
        return array3DTriangles
    else:
        return None
    