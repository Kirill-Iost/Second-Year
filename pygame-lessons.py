import pygame
import random

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Жёлтый круг')
    size = width, height = 1000, 1000
    screen = pygame.display.set_mode(size)
    balls = []

    running = True
    circle_size = 0
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        balls.append({"vy": random.choice([-1000, 1000]), "vx": random.choice([-1000, 1000]), "pos-x": random.randint(0, width), "pos-y": random.randint(0, height), "size": 10})
        screen.fill((0, 0, 0))
        for ball in balls:
            if (ball['pos-x'] - ball["size"] < 0 and ball['vx'] < 0) or (
                    ball["pos-x"] + ball["size"] > width and ball['vx'] > 0):
                ball['vx'] = -ball['vx']
            if (ball['pos-y'] - ball["size"] < 0 and ball['vy'] < 0) or (
                    ball["pos-y"] + ball["size"] > height and ball['vy'] > 0):
                ball['vy'] = -ball['vy']
            ball["pos-x"] += ball['vx'] // fps
            ball["pos-y"] += ball['vy'] // fps
            pygame.draw.circle(screen, (255, 255, 255), (ball["pos-x"], ball["pos-y"]),
                               ball["size"])
        clock.tick(fps)
        print(len(balls))
        pygame.display.flip()
    pygame.quit()
