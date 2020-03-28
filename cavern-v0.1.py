
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
            
while True:
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    shamans = self.findByType("shaman")
    shaman = self.findNearest(shamans)
    throwers = self.findByType("thrower")
    thrower = self.findNearest(throwers)
    ogres = self.findByType("ogre")
    ogre = self.findNearest(ogres)
    brawlers = self.findByType("brawler")
    brawler = self.findNearest(brawlers)
    merlins = self.findByType("fangrider")
    merlin = self.findNearest(merlins)
    cleave = self.isReady("cleave")
    dte = self.distanceTo(enemy)
    if enemy and enemy.type:
        if brawler and self.distanceTo(brawler) < 20:
            self.cast("chain-lightning", brawler)
            Kill(brawler)
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
        if ogre and self.distanceTo(ogre) < 20:
            self.attack(ogre)
            self.cast("chain-lightning", ogre)      
        if enemiesAtDistance(10) > 2 and cleave:
            self.cleave(enemy)
        elif enemiesAtDistance(10) == 1 and not enemy.type == "ogre":
            Kill(enemy)
        else:
            self.attack(enemy)
            
