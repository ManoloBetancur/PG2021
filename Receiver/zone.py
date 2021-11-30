#!/usr/bin/python3
def Zone(GPS_location):
      #Return true if the location is inside the boundaries
      
      #Values
      x=GPS_location[0]
      y=GPS_location[1]
      
      #Boundary 1 in calle 72
      Boundary1_Point1 = (4.6593,-74.061939)
      x1, y1 = Boundary1_Point1
      Boundary1_Point2 = (4.654755,-74.055462)
      x2, y2 = Boundary1_Point2
      #Positive to be inside
      d1=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)
      

      #Boundary 2 Autopista norte
      Boundary2_Point1 = (4.6593,-74.061939)
      x1, y1 = Boundary2_Point1
      Boundary2_Point2 = (4.67831, -74.058423)
      x2, y2 = Boundary2_Point2
      #Negative to be inside
      d2=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)
      

      #Boundary 3 Autopista norte
      Boundary3_Point1 = (4.67831, -74.058423)
      x1, y1 = Boundary3_Point1
      Boundary3_Point2 = (4.699528,-74.055075)
      x2, y2 = Boundary3_Point2
      #Negative to be inside
      d3=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)

      #Boundary 4 calle 116
      Boundary4_Point1 = (4.699528,-74.055075)
      x1, y1 = Boundary4_Point1
      Boundary4_Point2 = (4.693758,-74.033228)
      x2, y2 = Boundary4_Point2
      #Negative to be inside
      d4=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)

      #Boundary 5 carrera 7
      Boundary5_Point1 = (4.693758,-74.033228)
      x1, y1 = Boundary5_Point1
      Boundary5_Point2 = (4.67465, -74.041731)
      x2, y2 = Boundary5_Point2
      #Negative to be inside
      d5=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)

      #Boundary 6 carrera 7
      Boundary6_Point1 = (4.67465, -74.041731)
      x1, y1 = Boundary6_Point1
      Boundary6_Point2 = (4.654911, -74.055454)
      x2, y2 = Boundary6_Point2
      #Negative to be inside
      d6=(x-x1)*(y2-y1)-(y-y1)*(x2-x1)
      
      if (d1>=0 and d2<=0 and d3<=0 and d4<=0 and d5<=0 and d6<=0):
            return True
      else:
            return False
