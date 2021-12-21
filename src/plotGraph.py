import pygame

from src.Node import Node

SCREEN_WIDTH = 1300
SCREEN_HEIGHT = 800


class circle:
    def __init__(self, node: Node, min_x, max_x, min_y, max_y):
        self.key = node.getKey()
        self.x = ((node.getLocation()[0] - min_x) / (max_x - min_x)) * SCREEN_WIDTH
        self.y = ((node.getLocation()[1] - min_y) / (max_y - min_y)) * SCREEN_HEIGHT
        self._radius = 3

    def drawBall(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self._radius, 10)


class line:
    def __init__(self, startBall: circle, endBall: circle):
        self._src = (startBall.x, startBall.y)
        self._dest = (endBall.x, endBall.y)

    def drawLine(self, screen, inOut):
        pygame.draw.line(screen, (70, 70, 70), self._src, self._dest, 2)
        size = 4
        if inOut == "out":
            x = (self._dest[0], self._dest[1])
            y = (self._dest[0] + size, self._dest[1] - size)
            z = (self._dest[0] + size, self._dest[1] + size)
            pygame.draw.polygon(screen, (0, 0, 0), [x, y, z])

        if inOut == "in":
            x = (self._dest[0] - size, self._dest[1] - size)
            y = (self._dest[0] - size, self._dest[1] + size)
            z = (self._dest[0], self._dest[1])
            pygame.draw.polygon(screen, (0, 0, 0), [x, y, z])


def getBall(balls, node):
    j = 0
    for i in balls:
        if i.key == node.getKey():
            return j
        j += 1


def plot(graph):
    min_x = float('inf')
    for i in graph.get_all_v().keys():
        if graph.get_all_v().get(i).getLocation()[0] < min_x:
            min_x = graph.get_all_v().get(i).getLocation()[0]
    max_x = - float('inf')
    for i in graph.get_all_v().keys():
        if graph.get_all_v().get(i).getLocation()[0] > max_x:
            max_x = graph.get_all_v().get(i).getLocation()[0]

    min_y = float('inf')
    for i in graph.get_all_v().keys():
        if graph.get_all_v().get(i).getLocation()[1] < min_y:
            min_y = graph.get_all_v().get(i).getLocation()[1]
    max_y = - float('inf')
    for i in graph.get_all_v().keys():
        if graph.get_all_v().get(i).getLocation()[1] > max_y:
            max_y = graph.get_all_v().get(i).getLocation()[1]

    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    running = True

    # set nodes
    nodes = []
    balls = []
    for i in graph.get_all_v().keys():
        node = graph.get_all_v().get(i)
        nodes.append(node)
        ball = circle(node, min_x, max_x, min_y, max_y)
        balls.append(ball)

    # set edges
    lines_in = []
    lines_out = []
    for i in nodes:
        ball_i = balls[getBall(balls, i)]
        for j in balls:
            if j.key in i.getEdgesFromNode():
                ln = line(ball_i, j)
                lines_out.append(ln)
            if j.key in i.getEdgesToNode():
                ln = line(ball_i, j)
                lines_in.append(ln)

    # run the plot
    clock = pygame.time.Clock()
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screan
        screen.fill((200, 210, 200))
        for i in balls:
            i.drawBall(screen)
        for i in lines_out:
            i.drawLine(screen, "out")
        for i in lines_in:
            i.drawLine(screen, "in")

        pygame.display.flip()

    pygame.quit()

