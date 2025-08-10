# Interactive 3D Solar System Simulator 🪐

This is a 3D solar system simulation built with **Python** and the **VPython** library. It starts with a central star and allows users to interactively add new planets by simply clicking on the grid. Each new planet automatically calculates a stable orbit and begins revolving around the star.

---
## Demo

Check out this short demo of the simulator in action!

[**Watch the Instagram Reel Here**](https://www.instagram.com/reel/DNJaxPMzVqP/?igsh=MTN3bmtmczgxY2szeQ==)

---
##  Features

* **Interactive Planet Creation:** Click anywhere on the grid to add a new planet to the simulation.
* **Physics-Based Orbits:** The simulation uses a physics engine to calculate the gravitational pull of the central star, ensuring each new planet enters a stable orbit.
* **3D Visualization:** The scene is rendered in 3D, and the camera can be rotated and zoomed for different perspectives.
* **Real-Time Animation:** All celestial bodies, including the Sun and planets, spin on their own axes while orbiting, creating a dynamic and visually appealing scene.
* **Spacetime Grid:** A decorative, curved grid represents the Sun's gravitational field in the background.

---
## How I Made It

This project was a journey of progressive development, starting with a simple idea and adding complexity step-by-step.

1.  **The Initial Concept:** The project began with the goal of visualizing a static gravity well, similar to the reference video. The first version was just a stationary grid with a sphere in the middle.
2.  **Adding Planets:** I then added a few planets to the scene, placing them on the curved grid to show the effect of gravity.
3.  **Introducing Motion:** The next big step was to make the planets move. I implemented a basic physics engine using Newton's law of universal gravitation ($F = G \frac{m_1 m_2}{r^2}$). This involved creating a `while True:` loop that would continuously update each planet's position based on the Sun's pull.
4.  **Refining the Simulation:** The initial orbits were unstable, so I spent time fine-tuning the physics constants (`G` and `dt`) and initial velocities to ensure the planets didn't fly off into space. I also added rotation to the Sun and planets to make the scene more dynamic.
5.  **Making it Interactive:** The final and most exciting feature was adding user interaction. I used VPython's `scene.bind('click', ...)` method to detect mouse clicks. When a click occurs, a function calculates the perfect velocity for a stable circular orbit at that point and launches a new planet.

---
##  Inspiration

The initial idea for this project was inspired by the amazing visual explanations of gravity in this YouTube video. It sparked my curiosity to see if I could replicate and expand upon the concept myself using code.

[**Watch the inspirational YouTube video here**](https://youtu.be/_YbGWoUaZg0?si=vS1elZXk8pb_Vf5-)

---
## Technologies Used

* **Language:** Python 3
* **Library:** [VPython](https://vpython.org/) (GlowScript) for 3D graphics and animation.

---
##  How to Run

1.  Make sure you have [Python](https://www.python.org/downloads/) installed.
2.  Clone this repository to your local machine:
    ```bash
    git clone [https://github.com/HarukiDhruv/Gravity-Simulation.git](https://github.com/HarukiDhruv/Gravity-Simulation.git)
    ```
3.  Navigate into the project directory:
    ```bash
    cd Gravity-Simulation
    ```
4.  Install the VPython library:
    ```bash
    pip install vpython
    ```
5.  Run the main script:
    ```bash
    python main.py
    ```
    (Or whatever you named your Python file)

---
## How to Use

* Once the simulation is running, simply **left-click** anywhere on the grid.
* A new planet with a random color will appear at your cursor's location and immediately start orbiting the Sun.
* You can add as many planets as you like!
