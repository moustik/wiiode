# pyODE example 1: Getting started

import ode


def run():
    data = []

    # Create a world object
    world = ode.World()
    world.setGravity((0, -9.81, 0))

    # Create a body inside the world
    body = ode.Body(world)
    M = ode.Mass()
    M.setSphere(2500.0, 0.05)
    M.mass = 1.0
    body.setMass(M)

    body.setPosition((0, 2, 0))
    body.addForce((0, 200, 0))

    # Do the simulation...
    total_time = 0.0
    dt = 0.04
    while total_time < 2.0:
        x, y, z = body.getPosition()
        u, v, w = body.getLinearVel()
        fx, fy, fz = body.getForce()
        datum = {
            't': total_time,
            'pos': (x, y, z),
            'vel': (u, v, w),
            'f': (fx, fy, fz),
            }
        data.append(datum)
        world.step(dt)
        total_time += dt

    return data
