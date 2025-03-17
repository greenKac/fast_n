"""
Mostly a python translation of this implementation: https://rtouti.github.io/graphics/perlin-noise-algorithm
"""

import math
import random

random.seed = 1

def Shuffle(table):
    for j in range(len(table)-1, 0, -1):
        i = random.randint(0, j-1)
        table[j], table[i] = table[i], table[j]

def Permute():
    permTable = list(range(256))
    Shuffle(permTable)
    permTable.extend(permTable)
    return permTable

def GenerateGradients():
    gradients = []
    for i in range(256):
        g = (random.random() * 2 - 1, random.random() * 2 - 1)
        l = math.sqrt(g[0] * g[0] + g[1] * g[1])
        gradients.append((g[0] / l, g[1] / l))
    return gradients

permTable = Permute()
gradients = GenerateGradients()

def Generate(x, y):
    xF = math.floor(x)
    yF = math.floor(y)
    
    gX = xF & 255
    gY = yF & 255

    xDist = x - xF
    yDist = y - yF

    dotTL = Dot((xDist, yDist - 1.0), gradients[permTable[permTable[gX] + gY + 1]])
    dotTR = Dot((xDist - 1.0, yDist - 1.0), gradients[permTable[permTable[gX + 1] + gY + 1]])
    dotBL = Dot((xDist, yDist), gradients[permTable[permTable[gX] + gY]])
    dotBR = Dot((xDist - 1.0, yDist), gradients[permTable[permTable[gX + 1] + gY]])

    yFade = Fade(yDist)

    return Lerp(
        Lerp(dotBL, dotTL, yFade),
        Lerp(dotBR, dotTR, yFade),
        Fade(xDist)
    )

# ================== MATH UTILS ==================

def Dot(a: tuple[float, float], b: tuple[float, float]) -> float:
        return (a[0] * b[0] + a[1] * b[1])

def Fade(t):
    return ((6 * t - 15) * t + 10) * t * t * t

def Lerp(a, b, t):
    return a + t * (b - a)