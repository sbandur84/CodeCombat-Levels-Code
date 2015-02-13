# COMMON FUNCTIONS LIBRARY FOR CODE COMBAT

def GetEdge(offset, minX, minY, maxX, maxY):
    x = self.pos.x
    y = self.pos.y
    if y < minY + offset and x < minX + offset:
        return "BOTTOM_LEFT"
    elif x < minX + offset:
        return "LEFT_EDGE"
    elif x < minX + offset and y > maxY - offset:
        return "TOP"
    elif y > maxY - offset:
        return "TOP_EDGE"
    elif y > maxY - offset and x > maxX - offset:
        return "TOP_RIGHT"
    elif x > maxX - offset:
        return "RIGHT_EDGE"
    elif x > maxX - offset and y < minY + offset:
        return "BOTTOM_RIGHT"
    elif y < minY + offset:
        return "BOTTOM"
    else:
        return 0
        
        
        
def Go(where, dist, edge):
    if where:
        if where == "UP":
            x = self.pos.x
            y = self.pos.y+dist
            self.moveXY(x, y)
        elif where == "UP_LEFT":
            x = self.pos.x - dist
            y = self.pos.y + dist
            self.moveXY(x, y)
        elif where == "UP_RIGHT":
            x = self.pos.x+dist
            y = self.pos.y+dist
            self.moveXY(x, y)
        elif where == "DOWN":
            x = self.pos.x
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == "DOWN_LEFT":
            x = self.pos.x-dist
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == "DOWN_RIGHT":
            x = self.pos.x+dist
            y = self.pos.y-dist
            self.moveXY(x, y)
        elif where == "RIGHT":
            x = self.pos.x+dist
            y = self.pos.y
            self.moveXY(x, y)        
        elif where == "LEFT":
            x = self.pos.x-dist
            y = self.pos.y
            self.moveXY(x, y)
            
def AwayFromEnemyRelativePos(enemy):
    where = ""
    if enemy:
        ex = enemy.pos.x
        ey = enemy.pos.y
        x = self.pos.x
        y = self.pos.y
        # enemy is DOWN_LEFT
        if ex < x and ey < y:
            where = "UP_RIGHT"
        # enemy is DOWN_RIGHT
        elif ex > x and ey < y:
            where = "UP_LEFT"
        # enemy is UP_RIGHT
        elif ex > x and ey > y:
            where = "DOWN_LEFT"
        # enemy is UP_LEFT
        elif ex < x and ey > y:
            where = "DOWN_RIGHT"
        # enemy is UP
        elif ex == x and ey > y:
            where = "DOWN"
        # enemy is DOWN
        elif ex == x and ey < y:
            where = "UP"
        # enemy is RIGHT
        elif ex > x and ey == y:
            where = "LEFT"
        # enemy is LEFT
        elif ex < x and ey == y:
            where = "RIGHT"
        return where
    else:
        return 0


# walk around room
def WalkAround(dist):
    # premikamo se po polju
    if AttEdge(self, dist+5) == "BOTTOM_LEFT" or AttEdge(self, dist+5) == "LEFT_EDGE":
        # move up
        Go("UP", dist)
    elif AttEdge(self, dist+5) == "TOP_LEFT" or AttEdge(self, dist+5) == "TOP":
        # move right
        Go("RIGHT", dist)
    elif AttEdge(self, dist+5) == "TOP_RIGHT" or AttEdge(self, dist+5) == "RIGHT_EDGE":
        # move down
        Go("DOWN", dist)
    elif AttEdge(self, dist+5) == "BOTTOM_RIGHT" or AttEdge(self, dist+5) == "BOTTOM":
        # move left
        Go("LEFT", dist)


def runFrom(enemy, distance):
    if AttEdge(self, distance):
        WalkAround(distance)
     elif enemy:
        #beži od sovražnika
        Go(AwayFromEnemyRelativePos(enemy), distance)       
        

# returns NUMBER of ENEMIES at given distance --------------------
def enemiesAtDistance(dist):
    n = 0
    ene = self.findEnemies()
    for en in ene:
        if self.distanceTo(en) < dist:
            n=n+1
    return n
# ----------------------------------------------------------------



def Kill(e):
    if e:
        while e.health > 0:
            self.attack(e)
                    
                    
        
    
        
    
    
    

