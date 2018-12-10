#!/usr/bin/python3

import pygame
import csv
import time

width = 500
height = 300

start_lat = 49.272410
end_lat = 49.274977
start_lon = -123.197729
end_lon = -123.188435

def ll_to_xy(ll):
    lat, lon = ll
    x = -height*(lat-start_lat)/(end_lat-start_lat)
    y = width*(lon-start_lon)/(end_lon-start_lon)
    return (x,y)

def getCenter(surface, pos):
    x, y = pos
    x -= surface.get_height()/2
    y -= surface.get_width()/2
    return(x,y)


data = []

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        data.append([(float(row[1]), float(row[2])), (float(row[3]), float(row[4])), (float(row[5]), float(row[6])), float(row[7])])

    print("data loaded.")

pygame.init()

size = (width, height)
bg = (255, 255, 255) #white?

screen = pygame.display.set_mode(size)

boat = pygame.image.load("boat.png")
boat.convert()
boat = pygame.transform.scale(boat, (20,20))
n = 0

clock = pygame.time.Clock()

while True:
    n = n+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(bg)
    screen.blit(boat, (getCenter(boat, ll_to_xy(data[n][0]))))
    pygame.display.flip()
    clock.tick(30)
