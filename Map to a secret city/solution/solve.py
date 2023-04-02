#!/usr/bin/env python3

# LNC2023{e279a99f2AE} JRHEGMRQGIZXWZJSG44WCOJZMYZECRL5
import pygame
import numpy as np
import cv2


def main():
    pygame.init()

    main_surface = pygame.display.set_mode((4000, 500))

    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        f = open("map.txt", "r")
        data = f.readlines()
        f.close()

        for line in data:
            l = line.strip().split()
            x0 = int(l[1], 16)
            y0 = int(l[0], 16)
            pygame.draw.line(main_surface, (255, 0, 255),
                             (x0, y0), (x0, y0), 1)

        pygame.display.flip()

    pygame.quit()


main()
