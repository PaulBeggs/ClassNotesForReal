from typing import *

import pygame
from pygame.locals import *
import random




# Reminders
# Exam #3 Monday - Practice Exam posted, will go over on Friday
# Design Document for Project #3 is also due Monday morning

#################################
# First we are going to go over Homework #9
#################################

# Sample Solution for Homework #9


# def vowel_count(lst: List[str]) -> Dict[str, int]:
#     vowels = 'aeiou' # it is fine to use a list instead here, or to pre-populate the dictionary
#     d = {}
#     for vowel in vowels:
#         d[vowel] = 0
#
#     for item in lst:
#         for vowel in d:
#             if vowel in item:
#                 d[vowel] += 1
#
#
#     return d
#
#
# def char_remaining(s: str) -> Dict[str, int]:
#     d= {}
#     for i in range(len(s)):
#         if s[i] not in d: # this is how we make sure not to count a character the second time
#             d[s[i]] = len(s) - i - 1 # the fact that it is len(s) - i - 1 may not be obvious -- test your code!!
#     return d
#
#
# def dict_count(d: Dict[str, int], s: str) -> int:
#     count = 0
#     for key in d:
#         if s in key:
#             count += d[key]
#
#     # notice that you have to loop over the keys, since you ask at each stage if s is in the key
#
#     return count
#
#
# class BouncyBall:
#
#     def __init__(self):
#         self.air = 10
#         self.exploded = False
#
#     def bounce(self):
#         if not self.exploded:
#             if self.air <= 3:
#                 print('Thupp.')
#             else:
#                 print('Bounce!')
#                 self.air -= 2
#         else:
#             print('You cannot bounce this ball! It has exploded.')
#
#     def inflate(self):
#         if self.exploded:
#             print('You cannot inflate this ball! It has exploded.')
#         else:
#             self.air += 3
#             if self.air > 12:
#                 self.exploded = True
#                 print('BANG!!!')
#                 self.air = 0
#
#
# class Gradebook:
#
#     def __init__(self):
#         self.grades = []
#         self.extra = 0
#
#     def add_grade(self, g: int):
#         self.grades.append(g)
#
#     def add_ec(self, ec: int):
#         self.extra += ec
#
#     def average(self):
#         return (sum(self.grades) + self.extra) / len(self.grades)


###############################################################
# Now more pygame
###############################################################

# Write a program that, when you push the c key will put a circle
# at a random spot on the screen, with a random velocity (both between -5 and +5 pixels per frame in each direction)
#Circles will also have a random color
# the circles should "bounce" off the top and bottom of the screen
#
# if we have time, we will also add that if you click on a circle, it will change to a random color

class Circle:

    def __init__(self):
        self.x = random.randint(0,1000)
        self.y = random.randint(0,800)
        self.radius = random.randint(10,50)

        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

        self.velx = ((-1) ** random.randint(0,1)) * random.randint(1,5)
        self.vely = ((-1) ** random.randint(0, 1)) * random.randint(1, 5)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    # def move(self):
    #     self.x += self.velx
    #     self.y += self.vely

    def move(self, xmax, ymax): # we need to know the size of the screen to 'bounce'
        if self.x - self.radius <= 0:
            self.velx = abs(self.velx)
        if self.x + self.radius >= xmax:
            self.velx = -1 * abs(self.velx)

        if self.y - self.radius <= 0:
            self.vely = abs(self.vely)
        if self.y + self.radius >= ymax:
            self.vely = -1 * abs(self.vely)

        self.x += self.velx
        self.y += self.vely

    # fix issue using the abs fucntion!







def draw_all(surface, circle_list):
    surface.fill('white')

    for circ in circle_list:
        circ.draw(surface)

    pygame.display.update()


def hit(x, y, targ: Circle): # to determine if the mouse clicked on it
    if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= targ.radius ** 2:
        return True
    else:
        return False


# def main1():
#     pygame.init()
#     xmax = 1000
#     ymax = 800
#     surface = pygame.display.set_mode((xmax, ymax))
#
#     circle_list = []
#     running = True
#
#     while running:
#         draw_all(surface, circle_list)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_c:
#                     circle_list.append(Circle())
#
#
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#
#                 for circ in circle_list:
#                     if hit(x,y,circ):
#                         circ.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#
#
#
#         pygame.time.delay(30)
#         for item in circle_list:
#             #item.move()
#             item.move(xmax, ymax)
#
#
#     pygame.quit()
#
# main1()

#
#
#
#




##############################
#Now, to show off some:
# We will model elastic collisions between the circles
# This uses some math, and is beyond what I'd expect you to do.









#
#
#
# #
# # #
# # #
# # #
# #
# #
# class Circle():
#
#     def __init__(self):
#         self.x = random.randint(0,1000)
#         self.y = random.randint(0,800)
#
#         self.rad = random.randint(5,35)
#         self.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#         self.velx = random.randint(-5,5)
#         self.vely = random.randint(-5,5)
#
#
#
#     def draw(self, surface):
#         pygame.draw.circle(surface,self.color, (self.x, self.y),self.rad)
#
#     def move(self, xmax, ymax):
#         if self.x < self.rad or self.x > xmax - self.rad: # has hit the left side of the screen!
#             self.velx *= -1
#
#         if self.y < self.rad or self.y > ymax - self.rad: # has hit the left side of the screen!
#             self.vely *= -1
#
#         self.x += self.velx
#         self.y += self.vely
#
#
#
#
#
#
# def draw_all(surface, circle_list):
#     surface.fill('white')
#
#     for circ in circle_list:
#         circ.draw(surface)
#
#     pygame.display.update()
#
#
# def hit(x, y, targ: Circle):
#     if (x - targ.x) ** 2 + (y - targ.y) ** 2 <= targ.rad ** 2:
#         return True
#     else:
#         return False
#
# def dist(c1: Circle, c2: Circle) -> bool:
#     return ((c1.x - c2.x) ** 2 + (c1.y - c2.y) ** 2) ** (1 / 2) <= c1.rad + c2.rad
#
#
# # the below function is complicated -- it does the conversation of momentum for an elastic collision
# # This is beyond the scope of what I expect you to do in class, but does show how "real" word physics
# # can be used -- I am assuming that the mass of the objects is proportional to their area.
# def elastic(c1: Circle, c2: Circle):
#
#     v1 = (c1.velx, c1.vely)
#     x1 = (c1.x, c1.y)
#     m1 = c1.rad ** 2
#
#     v2 = (c2.velx, c2.vely)
#     x2 = (c2.x, c2.y)
#     m2 = c2.rad ** 2
#
#
#     new_v1x = v1[0] - (2 * m2)/(m1 + m2) * ((v1[0]-v2[0]) * (x1[0]-x2[0]) + (v1[1]-v2[1])*(x1[1]-x2[1]))/((x1[0]-x2[0])**2 + (x1[1]-x2[1])**2) * (x1[0]-x2[0])
#
#     new_v1y = v1[1] - (2 * m2) / (m1 + m2) * ((v1[0] - v2[0]) * (x1[0] - x2[0]) + (v1[1] - v2[1]) * (x1[1] - x2[1])) / (
#                 (x1[0] - x2[0]) ** 2 + (x1[1] - x2[1]) ** 2) * (x1[1]-x2[1])
#
#     new_v2x = v2[0] - (2 * m1) / (m1 + m2) * ((v2[0] - v1[0]) * (x2[0] - x1[0]) + (v2[1] - v1[1]) * (x2[1] - x1[1])) / (
#                 (x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2) * (x2[0]-x1[0])
#     new_v2y = v2[1] - (2 * m1) / (m1 + m2) * ((v2[0] - v1[0]) * (x2[0] - x1[0]) + (v2[1] - v1[1]) * (x2[1] - x1[1])) / (
#             (x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2) * (x2[1]-x1[1])
#
#     c1.velx = new_v1x
#     c1.vely = new_v1y
#
#     c2.velx = new_v2x
#     c2.vely = new_v2y
#
#
#
#
#
#
#
# def main2():
#     pygame.init()
#     xmax = 1000
#     ymax = 800
#     surface = pygame.display.set_mode((xmax, ymax))
#
#     # these are two circles I added for testing purposes
#     # a = Circle()
#     # b = Circle()
#     # a.x = 100
#     # a.y = 400
#     # b.x = 900
#     # b.y = 400
#     #
#     # a.rad = 20
#     # b.rad = 10
#     #
#     # a.velx = 3
#     # b.velx = -3
#     # a.vely = 0
#     # b.vely = 0
#
#
#
#     circle_list = []
#     # circle_list.append(a) # again, for test purposes
#     # circle_list.append(b)
#     running = True
#
#     while running:
#         draw_all(surface, circle_list)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                running = False
#             elif event.type == KEYDOWN:
#                 if event.key ==K_c:
#                     circle_list.append(Circle())
#
#
#             elif event.type == MOUSEBUTTONDOWN:
#                 (x,y) = (event.pos[0], event.pos[1])
#
#                 for circ in circle_list:
#                     if hit(x,y,circ):
#                         circ.color = pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#
#
#
#
#         pygame.time.delay(30)
#         for item in circle_list:
#             item.move(xmax, ymax)
#
#         for i in range(len(circle_list)):
#             for j in range(i+1, len(circle_list)):
#                 if dist(circle_list[i], circle_list[j]):
#
#                     elastic(circle_list[i], circle_list[j]) # this does the elastic collision (mostly)
#
#                     # # these make the circles bounce off each other, but in awkward ways
#                     # circle_list[i].velx *= -1
#                     # circle_list[j].velx *= -1
#                     # circle_list[i].vely *= -1
#                     # circle_list[j].vely *= -1
#
#
#
#
#
#
#     pygame.quit()
#
# main2()

## Finally, a simple point and click keyboard

class Key:

    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter.upper()

        self.size = 50
        self.color = 'gray'

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size,self.size))


        totalText = set_text(self.letter, self.x + self.size // 2, self.y + self.size // 2 + 3, 30)
        surface.blit(totalText[0], totalText[1])

    def toggle_click(self):
        if self.color == 'gray':
            self.color = 'yellow'
        else:
            self.color = 'gray'




def draw_all(surface, key_list: List['Key'], let):
    surface.fill(pygame.Color('white'))

    for key in key_list:
        key.draw(surface)

    totalText = set_text1(let, 100, 500, 30)
    surface.blit(totalText[0], totalText[1])


    pygame.display.update()




def set_text(string, coordx, coordy, fontSize):
    font = pygame.font.SysFont('Helvetica', fontSize)
    # font.bold = True
    text = font.render(string, True, (255,255,255))
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def set_text1(string, coordx, coordy, fontSize):
    font = pygame.font.SysFont('Helvetica', fontSize)
    # font.bold = True
    text = font.render(string, True, 'black')
    textRect = text.get_rect()
    textRect.center = (coordx, coordy)
    return (text, textRect)

def make_keys():
    initx = 100
    inity = 100
    key_list = [['a','b','c'],['d','e','f'],['g','h','i']]
    keys = []
    deltax = 5
    deltay = 5

    currx = initx
    curry = inity

    for row in key_list:
        for item in row:
            keys.append(Key(currx, curry, item))
            currx += deltax + 50
        currx = initx
        curry += deltay + 50

    return keys


def hit(x,y, key):
    if key.x <= x <= key.x + key.size and key.y <= y <= key.y + key.size:
        key.toggle_click()
        if key.color == 'yellow':
            return key.letter
        else:
            return None


def main3():
    pygame.init()
    xmax = 1000
    ymax = 800
    surface = pygame.display.set_mode((xmax, ymax))

    key_list = make_keys()
    running = True

    str = ''


    while running:
        draw_all(surface, key_list, str)
        for event in pygame.event.get():
            if event.type == QUIT:
               running = False
            elif event.type == KEYDOWN:
                if event.key ==K_c:
                    circle_list.append(Circle())


            elif event.type == MOUSEBUTTONDOWN:
                (x,y) = (event.pos[0], event.pos[1])

                for key in key_list:
                    let = hit(x, y, key)

                    if let:
                        str += let









        pygame.time.delay(30)



    pygame.quit()

main3()