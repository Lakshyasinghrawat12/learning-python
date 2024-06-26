# from itertools import product


# a=int(input("Input the number"))
# b=int(input("Input the number"))
# product=0
# for i in range(1,b+1):
#     product=product+a
#     print("Multiplication of number", product)

# Python program to shuffle a deck of card

# # importing modules
# import itertools, random

# # make a deck of cards
# deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# # shuffle the cards
# random.shuffle(deck)

# # draw five cards
# print("You got:")
# for i in range(5):
#    print(deck[i][0], "of", deck[i][1])

# import pygame, sys
# from pygame.locals import *

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# while True: # main game loop
#     for event in pygame.event.get():
#         if event.type == QUIT:
#              pygame.quit()
#              sys.exit()
#     pygame.display.update()

# import turtle

# t=turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.pencolor("red")


# a=0
# b=0
# t.speed(10)
# t.penup()
# t.goto(0,200)
# t.pendown()
# while True:
#     t.forward(a)
#     t.right(b)
#     a+=3
#     b+=1

#     if b==210:
#         break
#     t.hideturtle()

# turtle.done()