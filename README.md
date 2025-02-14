# Monte Carlo Method Area Finder

This program allows the user to choose a shape and it's dimensions. It then finds the approximate area using the Monte Carlo Method, rather than any known area formulas for said shape.

I first learned of the Monte Carlo Method for estimating the area of a shape while reading The Three-Body Problem, by Liu Cixin. I immediately knew that I wanted to attempt to re-create this. 

A brief explanation of using the Monte Carlo Method to approximate the area of a shape:
The unknown area of a shape is calculated by placing it within a known area (I use a 1000x1000 pixel grid) and repeatedly striking the entire grid with tiny balls at random points. After bombarding the grid, we can approximate the area of our shape by calculating the ratio of balls that landed inside the shape and balls that landed outside it.


