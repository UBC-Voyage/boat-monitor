from osmviz.animation import TrackingViz, Simulation
from BoatViz import BoatViz
from LineViz import LineViz
from HudViz import HudViz
import csv
import math

# Define begin/end points, duration, and icon for our train

image_f = "img/boat_small.png"
target_f = "img/target.png"

# Define bounds for the train and zoom level, how much map do we show?

bound_ne_lat,bound_ne_lon = (49.274977,-123.188435)
bound_sw_lat,bound_sw_lon = (49.272410,-123.197729)
zoom = 17 # OSM zoom level
speed = 10


data = []

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data.append([(float(row[1]), float(row[2])), math.degrees(math.atan2(float(row[3]), float(row[4]))), (float(row[5]), float(row[6])), float(row[7])])

    print("data loaded.")

begin_time, end_time = 0, len(data)/speed

# Define an interpolater to create animation points

def dataAtTime(t,n):
    if (t < begin_time): return data[0][n]
    if (t > end_time): return data[len(data)-1][n]
    frac = int(t*speed)
    if (frac >= len(data)): return data[len(data)-1][n]
    return data[frac][n]

def targetLocAtTime(t):
    return dataAtTime(t, 2)

def boatLocAtTime(t):
    return dataAtTime(t, 0)

def angleAtTime(t):
    return dataAtTime(t, 1)

def formHudText(t):
    return ["Nimrod: " + str(dataAtTime(t,0)),
            "Heading: {:+7.1f}".format(dataAtTime(t,1)),
           "Target: " + str(dataAtTime(t,2)),
           "Rudder Angle: {:+7.1f}".format(dataAtTime(t,3)),
           "Time: {:.1f}".format(t)]


# Create a TrackingViz

target = TrackingViz("Target", target_f, targetLocAtTime,
                     (begin_time,end_time),
                     (bound_sw_lat,bound_ne_lat,bound_sw_lon,bound_ne_lon), 1)

viz = BoatViz("Nimrod", image_f, boatLocAtTime, angleAtTime,
                   (begin_time,end_time),
                   (bound_sw_lat,bound_ne_lat,bound_sw_lon,bound_ne_lon),
                  1) # Drawing order

line = LineViz(boatLocAtTime, targetLocAtTime)

hud = HudViz(formHudText, fontsize=16)

# Add our TrackingViz to a Simulation and then run the simulation

sim = Simulation([viz,],[target,line,hud],0) # ([actor vizs], [scene vizs], initial time)
sim.run(speed=1,refresh_rate=speed,osmzoom=zoom)
