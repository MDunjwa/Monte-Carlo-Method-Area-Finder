import unittest
from area_finder import *

from unittest.mock import patch
import sys
from io import StringIO

class TestAreaFinder(unittest.TestCase):
    
    
    def test_Display_Shapes(self):
        shapes_list = ["circle","square","rectangle","ellipse"]
        printed_text = StringIO()
        sys.stdout = printed_text
        display_shapes(shapes_list)

        self.assertEqual(printed_text.getvalue(),"""Choose one of the following shapes by typing its corresponding number, and we will estimate its area using the Monte Carlo method!
1. circle
2. square
3. rectangle
4. ellipse
""")

    def test_Select_Shape(self):
        shapes_list = ["circle","square","rectangle","ellipse"]
        self.assertEqual(select_shape(1,shapes_list),"circle")
        self.assertEqual(select_shape(2,shapes_list),"square")
        self.assertEqual(select_shape(3,shapes_list),"rectangle")
        self.assertEqual(select_shape(4,shapes_list),"ellipse")


    def test_Find_Actual_Area(self):
        self.assertAlmostEqual(find_actual_area("circle",diameter=5),19.634954084936)
        self.assertAlmostEqual(find_actual_area("square",diameter=5),25)
        self.assertAlmostEqual(find_actual_area("rectangle",width=5,length=10),50)
        self.assertAlmostEqual(find_actual_area("ellipse",radius1=13,radius2=6),245.04423)

        


 
