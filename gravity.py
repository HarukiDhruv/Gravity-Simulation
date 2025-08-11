from vpython import *
import math

scene.title = "Solar System with Dynamic Spacetime"
scene.background = color.black
scene.width = 1200
scene.height = 800
scene.camera.pos = vector(0, 80, 100)
scene.camera.axis = vector(0, -80, -100)

dt = 0.005

# --- SETUP STAR AND PLANETS WITH MASS ---
# MODIFICATION: Sun color changed to orange
star = sphere(pos=vector(0,0,0), radius=5, color=color.orange, emissive=True)
star.mass = 150.0 # Give the star a large mass to create the main well
sun_light = local_light(pos=star.pos, color=color.orange)

# MODIFICATION: Increased speed for all planets
planet_1 = sphere(pos=vector(20, 0, 0), radius=1, color=color.magenta, make_trail=False)
planet_1.orbit_radius = 20
planet_1.angle = 0
planet_1.speed = 1.6 # Was 0.8
planet_1.mass = 1.0

planet_2 = sphere(pos=vector(-35, 0, 0), radius=1.5, color=color.cyan, make_trail=False)
planet_2.orbit_radius = 35
planet_2.angle = math.pi
planet_2.speed = 1.0 # Was 0.5
planet_2.mass = 1.5

planet_3 = sphere(pos=vector(0, 0, 45), radius=2, color=color.yellow, make_trail=False)
planet_3.orbit_radius = 45
planet_3.angle = math.pi/2
planet_3.speed = 0.6 # Was 0.3
planet_3.mass = 2.0

planet_4 = sphere(pos=vector(0, 0, -60), radius=1.2, color=color.green, make_trail=False)
planet_4.orbit_radius = 60
planet_4.angle = -math.pi/2
planet_4.speed = 0.4 # Was 0.2
planet_4.mass = 1.2

bodies = [star, planet_1, planet_2, planet_3, planet_4]
planets = [planet_1, planet_2, planet_3, planet_4]

# --- FUNCTION TO CALCULATE COMBINED CURVATURE ---
def get_y_coordinate(x, z):
    total_y = 0
    # Loop through all massive bodies (sun and planets)
    for body in bodies:
        distance_sq = (x - body.pos.x)**2 + (z - body.pos.z)**2
        # Calculate the depth and width of the curve based on the body's mass
        depth_factor = -0.1
        width_factor = 10.0
        
        depth = depth_factor * body.mass
        width = width_factor * body.mass
        
        # Add this body's contribution to the total curve
        total_y += depth * exp(-distance_sq / width)
        
    return total_y

# --- DYNAMIC GRID SETUP ---
grid_spacing = 8.0
grid_range = 80
line_radius = 0.05
# Create curve objects once, we will update their points in the loop
grid_lines = []
for _ in range(2 * (2 * grid_range // int(grid_spacing) + 1)):
    grid_lines.append(curve(color=color.white, radius=line_radius))

def update_grid():
    """This function redraws the grid each frame to show the moving planet dips."""
    curve_index = 0
    # Draw lines along the z-axis
    for x_coord in range(-grid_range, grid_range + 1, int(grid_spacing)):
        points = [vector(x_coord, get_y_coordinate(x_coord, z), z) for z in range(-grid_range, grid_range + 1)]
        grid_lines[curve_index].clear()
        grid_lines[curve_index].append(points)
        curve_index += 1
    # Draw lines along the x-axis
    for z_coord in range(-grid_range, grid_range + 1, int(grid_spacing)):
        points = [vector(x, get_y_coordinate(x, z_coord), z_coord) for x in range(-grid_range, grid_range + 1)]
        grid_lines[curve_index].clear()
        grid_lines[curve_index].append(points)
        curve_index += 1


# --- ANIMATION LOOP ---
running = True
def toggle_animation(evt):
    global running
    if evt.key == 'p':
        running = not running
scene.bind('keydown', toggle_animation)
wtext(text="\nControls: Right-drag to rotate; Scroll to zoom; 'p' to pause.\n")

# Set initial positions correctly
for p in planets:
    p.pos.y = get_y_coordinate(p.pos.x, p.pos.z)
star.pos.y = get_y_coordinate(star.pos.x, star.pos.z) + star.radius

while True:
    if running:
        rate(100)
        # Animate the planets in their circular paths
        for p in planets:
            p.angle = p.angle + p.speed * dt
            p.pos.x = p.orbit_radius * cos(p.angle)
            p.pos.z = p.orbit_radius * sin(p.angle)
            p.pos.y = get_y_coordinate(p.pos.x, p.pos.z)
            p.rotate(angle=0.01, axis=vector(0,1,0))
        
        # This line makes the star sit down in the well
        star.pos.y = get_y_coordinate(star.pos.x, star.pos.z) + star.radius
        
        star.rotate(angle=0.001, axis=vector(0,1,0.05))
        
        # Redraw the entire grid to reflect the new positions of the planets
        update_grid()