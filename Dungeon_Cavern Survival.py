# playground BOUNDS ----------------------------------------------
maxX = 75
maxY = 125
minX = 0
minY = 0
# ----------------------------------------------------------------
def Go(where, dist):
    x = self.pos.x
    y = self.pos.y
    if where:
        if where == "UP":
            self.moveXY(x, y+dist)
        elif where == "UP_LEFT":
            self.moveXY(x-dist, y+dist)
        elif where == "UP_RIGHT":
            self.moveXY(x+dist, y+dist)
        elif where == "DOWN":
            self.moveXY(x, y-dist)
        elif where == "DOWN_LEFT":
            self.moveXY(x-dist, y-dist)
        elif where == "DOWN_RIGHT":
            self.moveXY(x+dist, y-dist)
        elif where == "RIGHT":
            self.moveXY(x+dist, y)        
        elif where == "LEFT":
            self.moveXY(x-dist, y)   
            
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

def AttEdge(what, offset):
    x = what.pos.x
    y = what.pos.y
    if what:
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
# walk around room
def WalkAround(dist):
    myX = self.pos.x
    myY = self.pos.y
    # premikamo se po polju
    if AttEdge(self, 10) == "BOTTOM_LEFT" or AttEdge(self, 10) == "LEFT_EDGE":
        # move up
        Go("UP", dist)
    elif AttEdge(self, 10) == "TOP_LEFT" or AttEdge(self, 10) == "TOP":
        # move right
        Go("RIGHT", dist)
    elif AttEdge(self, 10) == "TOP_RIGHT" or AttEdge(self, 10) == "RIGHT_EDGE":
        # move down
        Go("DOWN", dist)
    elif AttEdge(self, 10) == "BOTTOM_RIGHT" or AttEdge(self, 10) == "BOTTOM":
        # move left
        Go("LEFT", dist)


def runFrom(enemy, distance):
    x = enemy.pos.x
    y = enemy.pos.y
    myX = self.pos.x
    myY = self.pos.y
    if enemy:
        #beži od sovražnika
        Go(AwayFromEnemyRelativePos(enemy))
    elif AttEdge(self, 15):
        WalkAround(distance)
        
        

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
            
loop:
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    shamans = self.findByType("shaman")
    shaman = self.findNearest(shamans)
    throwers = self.findByType("thrower")
    thrower = self.findNearest(throwers)
    ogres = self.findByType("ogre")
    ogre = self.findNearest(ogres)
    merlins = self.findByType("fangrider")
    merlin = self.findNearest(merlins)
    cleave = self.isReady("cleave")
    dte = self.distanceTo(enemy)
    if enemy and enemy.type:
        if merlin:
            if cleave and enemiesAtDistance(10) > 1:
                self.cleave(merlin)
            elif self.distanceTo(merlin) < 50:
                Kill(merlin)
        if shaman:
            if cleave and enemiesAtDistance(10) > 1:
                self.cleave(shaman)
            elif self.distanceTo(shaman) < 30:
                Kill(shaman)
        if thrower:
            if cleave and enemiesAtDistance(10) > 1:
                self.cleave(thrower)
            elif self.distanceTo(thrower) < 30:
                Kill(thrower)
        if ogre:
            if cleave and self.distanceTo(ogre) < 5:
                self.cleave(ogre)
            elif self.distanceTo(ogre) > 5 and self.distanceTo(ogre) < 30:
                runFrom(ogre)        
        if enemiesAtDistance(10) > 2 and cleave:
            self.cleave(enemy)
        elif enemiesAtDistance(10) > 2 and not cleave:
            runFrom(enemy)
        elif enemiesAtDistance(10) > 1 and not cleave:
            Kill(enemy)
        elif enemiesAtDistance(10) == 1 and not enemy.type == "ogre":
            Kill(enemy)
        else:
            runFrom(enemy)
                    
                    
        
    
        
    
    
    
