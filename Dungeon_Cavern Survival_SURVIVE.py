bounds = {"minX":93,"minY":10,"maxX":152,"maxY":124}
TOP = 1
BOTTOM = 2
RIGHT_EDGE = 3
LEFT_EDGE = 4
TOP_RIGHT = 5
TOP_LEFT = 6
BOTTOM_RIGHT = 7
BOTTOM_LEFT = 8
UP = 9
DOWN = 10
RIGHT = 11
LEFT = 12
UP_RIGHT = 13
UP_LEFT = 14
DOWN_LEFT = 15
DOWN_RIGHT = 16
# COMMON FUNCTIONS LIBRARY FOR CODE COMBAT
# -------------------------------------------------------------------------------------------------
# return true if item is in bounds
# ( item, leftBound, bottomBound, rightBound, topBound )
def IsInBounds(item, bounds):
    x = item.pos.x
    y = item.pos.y
    if y < bounds.maxY and y > bounds.minY and x < bounds.maxX and x > bounds.minX:
        return 1
    else:
        return 0
def GetEdge(offset, bounds):
    x = self.pos.x
    y = self.pos.y
    if y < bounds.minY + offset and x < bounds.minX + offset:
        return BOTTOM_LEFT
    elif x < bounds.minX + offset:
        return LEFT_EDGE
    elif x < bounds.minX + offset and y > bounds.maxY - offset:
        return TOP_LEFT
    elif y > bounds.maxY - offset:
        return TOP
    elif y > bounds.maxY - offset and x > bounds.maxX - offset:
        return TOP_RIGHT
    elif x > bounds.maxX - offset:
        return RIGHT_EDGE
    elif x > bounds.maxX - offset and y < bounds.minY + offset:
        return BOTTOM_RIGHT
    elif y < bounds.minY + offset:
        return BOTTOM
    else:
        return 0

def AwayFromEnemy(enemy):
    where = 0
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
            if edge == TOP:
                Go(RIGHT, dist, edge)
            x = self.pos.x
            y = self.pos.y+dist
            self.move({"x":x, "y":y})
        elif where == UP_LEFT:
            if edge == TOP_LEFT:
                Go(DOWN_RIGHT, dist, edge)
            x = self.pos.x - dist
            y = self.pos.y + dist
            self.move({"x":x, "y":y})
        elif where == UP_RIGHT:
            if edge == TOP_RIGHT:
                Go(DOWN, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y+dist
            self.move({"x":x, "y":y})
        elif where == DOWN:
            if edge == BOTTOM:
                Go(LEFT, dist, edge)
            x = self.pos.x
            y = self.pos.y-dist
            self.move({"x":x, "y":y})
        elif where == DOWN_LEFT:
            if edge == BOTTOM_LEFT:
                Go(UP, dist, edge)
            x = self.pos.x-dist
            y = self.pos.y-dist
            self.move({"x":x, "y":y})
        elif where == DOWN_RIGHT:
            if edge == BOTTOM_RIGHT:
                Go(LEFT, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y-dist
            self.move({"x":x, "y":y})
        elif where == RIGHT:
            if edge == RIGHT_EDGE:
                Go(DOWN, dist, edge)
            x = self.pos.x+dist
            y = self.pos.y
            self.move({"x":x, "y":y})        
        elif where == LEFT:
            if edge == LEFT_EDGE:
                Go(UP, dist, edge)
            x = self.pos.x-dist
            y = self.pos.y
            self.move({"x":x, "y":y})
            
def fightMove(enemy):
    Go(AwayFromEnemy(enemy), 10, GetEdge(13, bounds))
    
    
def enemiesAtDistance(dist):
    n = 0
    ene = self.findEnemies()
    for en in ene:
        if self.distanceTo(en) < dist:
            n=n+1
    return n
    
    

loop:
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    shamans = self.findByType("shaman")
    shaman = self.findNearest(shamans)
    throwers = self.findByType("thrower")
    thrower = self.findNearest(throwers)
    brawlers = self.findByType("brawler")
    brawler = self.findNearest(brawlers)
    ogres = self.findByType("ogre")
    ogre = self.findNearest(ogres)
    fangriders = self.findByType("fangrider")
    fangrider = self.findNearest(fangriders)
    if enemy and enemy.type:
        if brawler and self.distanceTo(brawler) < 20:
            if self.isReady("electrocute"):
                self.electrocute(brawler)
            if isReady"bash"):
                self.bash("brawler")
            self.attack(brawler)
            fightMove(brawler)
        elif fangrider and self.distanceTo(fangrider) < 50:
            if self.isReady("electrocute"):
                self.electrocute(fangrider)
            self.attack(fangrider)
        elif shaman and self.distanceTo(shaman) < 30:
            self.attack(shaman)
        elif thrower and self.distanceTo(thrower) < 30:
            self.attack(thrower)
        elif ogre and self.distanceTo(ogre) < 20:
            if self.isReady("electrocute"):
                self.electrocute(ogre)
            self.attack(ogre)
            fightMove(ogre)
        elif enemiesAtDistance(20) > 1:
            if self.isReady("bash"):
                self.bash(enemy)
            enemy = self.findNearest(enemies)
            self.attack(enemy)
            fightMove(enemy)
        elif enemiesAtDistance(20) == 1:
            self.attack(enemy)
        else:
            self.shield()
            
    
    
