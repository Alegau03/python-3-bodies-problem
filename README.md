# Three-Body Problem Simulation

This is a graphical simulation of the three-body problem using Python. The three balls start from random positions and move under the influence of mutual gravity, showcasing chaotic behavior typical of this dynamic system.  

## Requirements

Make sure you have Python 3 installed along with the following libraries:

- NumPy
- SciPy
- Matplotlib

You can install the necessary libraries using pip:

```bash
pip install numpy scipy matplotlib
```
# Usage
To run the simulation, download or clone this repository, and then execute the main.py file.
```bash
python main.py
```

# Code Description
The code uses SciPy's solve_ivp method to solve the differential equations describing the motion of the three bodies.  
The balls are represented by colored circles, and each ball leaves a trail of its own color to illustrate its movement over time.  

## Main Functions
- three_body_equations(t, y): Defines the equations of motion for the three bodies, calculating the accelerations due to gravity.  
- update(frame): Update function for the animation that computes the positions of the balls and updates the trails.

# Output
The simulation displays a real-time video of the motion of the three bodies. There is no static output image; the simulation can be observed as it runs.  
