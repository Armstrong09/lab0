import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1= Location("Paso",28.3,-135.9)
        loc2=Location("Paso",28.3,-135.9)
        self.assertEqual(loc1,loc2)

    def test_name(self):
        loc=Location("SLO",35.3,-120.7)
        self.assertEqual(loc.name,"SLO")

    def test_lat(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc.lat, 35.3)
    def test_lon(self):
        loc=Location("SLO",35.3,-120.7)
        self.assertEqual(loc.lon,-120.7)


    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
