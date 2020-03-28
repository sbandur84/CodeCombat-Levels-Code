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



hero.moveXY(30, 105)


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
    MUNCHKIN = hero.findNearest(MUNCHKIN)
    ENEMY = hero.findNearestEnemy()
    HERO = [e for e in self.findEnemies() if e.id in ["Hero Placeholder", "Hero Placeholder 1"]][0]
    
    
    
    if OGRE and self.distanceTo(OGRE) < 20:
        if hero.canCast("chain-lightning", OGRE):
            self.cast("chain-lightning", OGRE)
        elif OGRE.health > 0:
            self.bash(OGRE)
            self.attack(OGRE)
    elif THROWER and self.distanceTo(THROWER) < 40:
        if hero.canCast("chain-lightning", THROWER):
            hero.cast("chain-lightning", THROWER)
        elif THROWER.health > 0:
            self.attack(THROWER)
    elif BRAWLER and self.distanceTo(BRAWLER) < 20:
        self.attack(BRAWLER)
    if HERO and self.distanceTo(HERO) < 15:
        if hero.canCast("chain-lightning", HERO):
            self.cast("chain-lightning", HERO)
        elif HERO.health > 0:
            self.bash(HERO)
            self.shield()
            self.attack(HERO)
        self.attack(hero.findNearestEnemy())
    elif MERLIN and self.distanceTo(MERLIN) < 20:
           self.attack(MERLIN)
    elif MUNCHKIN and self.distanceTo(MUNCHKIN) < 20:
            self.attack(MUNCHKIN)
    elif SHAMAN and self.distanceTo(SHAMAN) < 20:
        if hero.isReady("cleave"):
            self.cleave(SHAMAN)
        if SHAMAN.health > 0:
            self.attack(SHAMAN)
    elif ENEMY and self.distanceTo(ENEMY) < 10 and ENEMY.health < 1:
        self.attack(ENEMY)
