#STATIC command definitions:
TOP = 1
TOP_RIGHT = 2
TOP_RIGHT = 3
BOTTOM = 4
BOTTOM_LEFT = 5
BOTTOM_RIGHT = 6
RIGHT_EDGE = 7
LEFT_EDGE = 8
UP_RIGHT = 9
UP_LEFT = 10
DOWN_LEFT = 11
DOWN_RIGHT = 12
DOWN = 13
UP = 14
LEFT RIGHT = 15
# COMMON FUNCTIONS LIBRARY FOR CODE COMBAT
# -------------------------------------------------------------------------------------------------
# return true if item is in bounds
# ( item, leftBound, bottomBound, rightBound, topBound )
def IsInBounds(item, minX, minY, maxX, maxY):
    x = item.pos.x
    y = item.pos.y
    if y < maxY and y > minY and x < maxX and x > minX:
        return 1
    else:
        return 0

def GetEdge(offset, minX, minY, maxX, maxY):
    x = self.pos.x
    y = self.pos.y
    if y < minY + offset and x < minX + offset:
        return BOTTOM_LEFT
    elif x < minX + offset:
        return LEFT_EDGE
    elif x < minX + offset and y > maxY - offset:
        return TOP_LEFT
    elif y > maxY - offset:
        return TOP
    elif y > maxY - offset and x > maxX - offset:
        return TOP_RIGHT
    elif x > maxX - offset:
        return RIGHT_EDGE
    elif x > maxX - offset and y < minY + offset:
        return BOTTOM_RIGHT
    elif y < minY + offset:
        return BOTTOM
    else:
        return 0
        

def GoAwayFromEnemyRelativePos(enemy):
    where = ""
    if enemy:
        ex = enemy.pos.x
        ey = enemy.pos.y
        x = self.pos.x
        y = self.pos.y
        # enemy is DOWN_LEFT
        if ex < x and ey < y:
            where = UP_RIGHT
        # enemy is DOWN_RIGHT
        elif ex > x and ey < y:
            where = UP_LEFT
        # enemy is UP_RIGHT
        elif ex > x and ey > y:
            where = DOWN_LEFT
        # enemy is UP_LEFT
        elif ex < x and ey > y:
            where = DOWN_RIGHT
        # enemy is UP
        elif ex == x and ey > y:
            where = DOWN
        # enemy is DOWN
        elif ex == x and ey < y:
            where = UP
        # enemy is RIGHT
        elif ex > x and ey == y:
            where = LEFT
        # enemy is LEFT
        elif ex < x and ey == y:
            where = RIGHT
        return where
    else:
        return 0


        
        
def Go(where, dist, edge):
    if where:
        if where == UP:
            if edge == TOP_EDGE:
                Go(DOWN, dist, edge)
            x = self.pos.x
            y = self.pos.y+dist
            self.moveXY(x, y)
        elif where == UP_LEFT:
            if edge == TOP_LEFT:
                Go(DOWN_RIGHT, dist, edge)
            x = self.pos.x - dist
            y = self.pos.y + dist
            self.moveXY(x, y)
        elif where == UP_RIGHT:
            if edge == TOP_RIGHT:
                Go(DOWN_LEFT, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y+dist
            self.moveXY(x, y)
        elif where == DOWN:
            if edge == BOTTOM:
                Go(UP, dist, edge)
            x = self.pos.x
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == DOWN_LEFT:
            if edge == BOTTOM_LEFT:
                Go(UP_RIGHT, dist, edge)
            x = self.pos.x-dist
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == DOWN_RIGHT:
            if edge == BOTTOM_RIGHT:
                Go(UP_LEFT, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == RIGHT:
            if edge == RIGHT_EDGE:
                Go(LEFT, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y
            self.moveXY(x, y)        
        elif where == LEFT:
            if edge == LEFT_EDGE:
                Go(RIGHT, dist, edge)
            x = self.pos.x-dist
            y = self.pos.y
            self.moveXY(x, y)
            


# walk around room
def WalkAround(dist, edge):
    # premikamo se po polju
    if edge == BOTTOM_LEFT:
        Go(UP_RIGHT, dist, edge)
    elif edge == LEFT_EDGE:
        Go(RIGHT, dist, edge)
    elif edge == TOP_LEFT:
        Go(DOWN_RIGHT, dist, edge)
    elif edge == TOP:
        Go(DOWN, dist, edge)
    elif edge == TOP_RIGHT:
        Go(DOWN_LEFT, dist, edge)
    elif edge == RIGHT_EDGE:
        Go(LEFT, dist, edge)
    elif edge == BOTTOM_RIGHT:
        Go(UP_LEFT, dist, edge)
    elif edge == BOTTOM:
        Go(UP, dist, edge)


def RunFrom(enemy, distance, edge):
    if edge:
        WalkAround(distance, edge)
    elif enemy:
        #beži od sovražnika
        Go(GoAwayFromEnemyRelativePos(enemy), distance, edge)    

def fightMoveShaman(enemy):
    if enemy.pos.y == self.pos.y:
        if enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x-20,"y":enemy.pos.y+20})
        else:
            self.move({"x":enemy.pos.x+20,"y":enemy.pos.y-20})
            
    elif enemy.pos.x == self.pos.x:
        if enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x+20,"y":enemy.pos.y-20})
        else:
            self.move({"x":enemy.pos.x-20,"y":enemy.pos.y+20})
    elif enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x-20,"y":enemy.pos.y+20})
    elif enemy.pos.x < self.pos.x:
            self.move({"x":enemy.pos.x+20,"y":enemy.pos.y-20})
    elif enemy.pos.y > self.pos.y:
        self.move({"x":enemy.pos.x+20,"y":enemy.pos.y-20})
    elif enemy.pos.y < self.pos.y:
        self.move({"x":enemy.pos.x-20,"y":enemy.pos.y+20})
def fightMove(enemy):
    if enemy.pos.y == self.pos.y:
        if enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x-20,"y":enemy.pos.y})
        else:
            self.move({"x":enemy.pos.x+20,"y":enemy.pos.y})
            
    elif enemy.pos.x == self.pos.x:
        if enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x,"y":enemy.pos.y-20})
        else:
            self.move({"x":enemy.pos.x,"y":enemy.pos.y+20})
    elif enemy.pos.x > self.pos.x:
            self.move({"x":enemy.pos.x-20,"y":enemy.pos.y})
    elif enemy.pos.x < self.pos.x:
            self.move({"x":enemy.pos.x+20,"y":enemy.pos.y})
    elif enemy.pos.y > self.pos.y:
        self.move({"x":enemy.pos.x,"y":enemy.pos.y-20})
    elif enemy.pos.y < self.pos.y:
        self.move({"x":enemy.pos.x,"y":enemy.pos.y+20})
