maxX = 67
maxY = 115
minX = 10
minY = 10
def enemiesAtDistance(dist):
    n = 0
    ene = self.findEnemies()
    for en in ene:
        if self.distanceTo(en) < dist:
            n=n+1
    return n

def runFrom(enemy):
    distance = 20
    x = enemy.pos.x
    y = enemy.pos.y
    myX = self.pos.x
    myY = self.pos.y
    # premikamo se po polju
    #smo na levem robu
    if myX - distance < minX:
        # če smo gori gre desno
        if myY + distance > maxY:
            self.moveXY(myX + distance, myY)
        # ali gor
        else:
            self.moveXY(myX, myY + distance)
    # pri zgornji
    elif myY + distance > maxY:
        # če smo že desno pojdi dol
        if myX + distance > maxX:
            self.moveXY(myX, myY - distance)
        # ali desno
        else:
            self.moveXY(myX + distance, myY)
    # pri desni
    elif myX + distance > maxX:
        # če smo spodaj idi levo
        if myY - distance < minY:
            self.moveXY(myX - distance, myY)
        # ali dol
        else:
            self.moveXY(myX, myY - distance)
    # pri spodnji
    elif myY - distance < minY:
        # če smo levo idi gor
        if myX - distance < minX:
            self.moveXY(myX, myY + distance)
        # ali levo
        else:
            self.moveXY(myX - distance, myY)
    else:
        #beži od sovražnika
        if x < maxX/2 and y < maxY/2:
            self.moveXY(myX + distance, myY + distance)
        if x > maxX/2 and enemy.pos.y < maxY/2:
            self.moveXY(myX - distance, myY + distance)
        if enemy.pos.x < maxX/2 and y > maxY/2:
            self.moveXY(myX + distance, myY - distance)
        if enemy.pos.x > maxX/2 and y > maxY/2:    
            self.moveXY(myX - distance, myY - distance)
            
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
                    
                    
        
    
        
    
    
    
