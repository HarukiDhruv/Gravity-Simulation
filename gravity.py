from vpython import *

scene.title = "Solar System "
scene.background = color.black
scene.width = 1000
scene.height = 800
scene.camera.pos = vector(0, 80, 100)
scene.camera.axis = vector(0, -80, -100)

dt = 0.005

star = sphere(pos=vector(0,0,0), radius=5, color=color.white, emissive=True)
sun_light = local_light(pos=star.pos, color=color.white)

planet_1 = sphere(pos=vector(20, 0, 0), radius=1, color=color.magenta)
planet_1.orbit_radius = 20
planet_1.angle = 0
planet_1.speed = 0.8

planet_2 = sphere(pos=vector(-35, 0, 0), radius=1.5, color=color.cyan)
planet_2.orbit_radius = 35
planet_2.angle = pi
planet_2.speed = 0.5

planet_3 = sphere(pos=vector(0, 0, 45), radius=2, color=color.yellow)
planet_3.orbit_radius = 45
planet_3.angle = pi/2
planet_3.speed = 0.3

planet_4 = sphere(pos=vector(0, 0, -60), radius=1.2, color=color.green)
planet_4.orbit_radius = 60
planet_4.angle = -pi/2
planet_4.speed = 0.2

planets = [planet_1, planet_2, planet_3, planet_4]

def get_y_coordinate(x, z):
    distance = sqrt(x**2 + z**2)
    return -40 * exp(-distance**2 / 1000)

grid_spacing = 8.0
grid_range = 80
line_radius = 0.05
for x_coord in range(-grid_range, grid_range + 1, int(grid_spacing)):
    curve(pos=[vector(x_coord, get_y_coordinate(x_coord, z), z) for z in range(-grid_range, grid_range + 1, int(grid_spacing))], color=color.white, radius=line_radius)
for z_coord in range(-grid_range, grid_range + 1, int(grid_spacing)):
    curve(pos=[vector(x, get_y_coordinate(x, z_coord), z_coord) for x in range(-grid_range, grid_range + 1, int(grid_spacing))], color=color.white, radius=line_radius)

running = True

def toggle_animation(evt):
    global running
    if evt.key == 'p':
        running = not running

scene.bind('keydown', toggle_animation)

while True:
    if running:
        rate(200)
        for p in planets:
            p.angle = p.angle + p.speed * dt
            p.pos.x = p.orbit_radius * cos(p.angle)
            p.pos.z = p.orbit_radius * sin(p.angle)
            p.rotate(angle=0.01, axis=vector(0,1,0))
        star.rotate(angle=0.001, axis=vector(0,1,0.05))