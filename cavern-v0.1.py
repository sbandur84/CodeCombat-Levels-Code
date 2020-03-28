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
    return






while True:
    
    SHAMAN = hero.findByType("shaman")
    SHAMAN = hero.findNearest(SHAMAN)
    OGRE = hero.findByType("ogre")
    OGRE = hero.findNearest(OGRE)
    BRAWLER = hero.findByType("brawler")
    BRAWLER = hero.findNearest(BRAWLER)
    MERLIN = hero.findByType("merlin")
    MERLIN = hero.findNearest(MERLIN)
    THROWER = hero.findByType("thrower")
    THROWER = hero.findNearest(THROWER)
    MUNCHKIN = hero.findByType("munchkin")
    MUNCHKIN = hero.findNearest(SHAMAN)
    
    
    
    if OGRE and self.distanceTo(OGRE) < 20:
        self.cast("chain-lightning", OGRE)
        self.attack(OGRE)
    elif THROWER and self.distanceTo(THROWER) < 40:
        if hero.isReady("cleave":
            self.cleave(THROWER)
        if
        self.attack(THROWER)
    elif BRAWLER and self.distanceTo(BRAWLER) < 20:
        self.attack(BRAWLER)
    elif merlin and self.distanceTo(merlin) < 20:
           self.attack(merlin)
    elif munchkin and self.distanceTo(munchkin) < 20:
            self.attack(munchkin)
    elif shaman and self.distanceTo(shaman) < 20:
        if cleave:
            self.cleave(shaman)
        self.attack(shaman)
    
    elif enemy and self.distanceTo(enemy) < 10 and enemy.health < 1:
        self.attack(enemy)
   
