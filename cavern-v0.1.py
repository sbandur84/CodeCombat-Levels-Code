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



hero.moveXY(30, 100)


while True:
    
    SHAMAN = hero.findByType("shaman")
    SHAMAN = hero.findNearest(SHAMAN)
    SKELETON = hero.findByType("skeleton")
    SKELETON = hero.findNearest(SKELETON)
    OGRE = hero.findByType("ogre")
    OGRE = hero.findNearest(OGRE)
    BRAWLER = hero.findByType("brawler")
    BRAWLER = hero.findNearest(BRAWLER)
    BURL = hero.findByType("burl")
    BURL = hero.findNearest(BURL)
    MERLIN = hero.findByType("merlin")
    MERLIN = hero.findNearest(MERLIN)
    THROWER = hero.findByType("thrower")
    THROWER = hero.findNearest(THROWER)
    MUNCHKIN = hero.findByType("munchkin")
    MUNCHKIN = hero.findNearest(MUNCHKIN)
    FANGRIDER = hero.findByType("fangrider")
    FANGRIDER = hero.findNearest(FANGRIDER)
    ENEMY = hero.findNearestEnemy()
    HERO = [e for e in self.findEnemies() if e.id in ["Hero Placeholder", "Hero Placeholder 1"]][0]
    
    
    if BURL and self.distanceTo(BURL) < 20:
        if hero.canCast("chain-lightning", BURL):
            self.cast("chain-lightning", BURL)
        elif BURL.health > 0:
            hero.shield()
            if hero.isReady("bash"):
                if hero.canElectrocute(BURL):
                    hero.electrocute(BURL)
                self.bash(BURL)
                self.shield()
                
            if BURL.health > 0:
                self.attack(BURL)
                self.shield()
    elif OGRE and self.distanceTo(OGRE) < 20:
        if hero.canCast("chain-lightning", OGRE):
            self.cast("chain-lightning", OGRE)
        elif OGRE.health > 0:
            hero.shield()
            if hero.isReady("bash"):
                if hero.canElectrocute(OGRE):
                    hero.electrocute(OGRE)
                self.bash(OGRE)
                self.shield()
            if OGRE.health > 0:
                self.attack(OGRE)
                self.shield()
    elif FANGRIDER and self.distanceTo(FANGRIDER) < 50 and FANGRIDER.health > 0:
        if hero.canCast("chain-lightning", FANGRIDER):
            self.cast("chain-lightning", FANGRIDER)
        elif FANGRIDER.health > 0:
            if hero.canElectrocute(FANGRIDER):
                hero.electrocute(FANGRIDER)
            self.attack(FANGRIDER)
    elif THROWER and self.distanceTo(THROWER) < 30:
        if THROWER.health > 0:
            self.attack(THROWER)
    elif SKELETON and self.distanceTo(SKELETON) < 20:
        if hero.canElectrocute(OGRE):
            hero.electrocute(OGRE)
        self.attack(SKELETON)
    elif BRAWLER and self.distanceTo(BRAWLER) < 20:
        if hero.canElectrocute(BRAWLER):
            hero.electrocute(BRAWLER)
        self.attack(BRAWLER)
    elif HERO and self.distanceTo(HERO) < 15:
        if hero.canCast("chain-lightning", HERO):
            self.cast("chain-lightning", HERO)
        elif HERO.health > 0:
            if hero.canElectrocute(HERO):
                hero.electrocute(HERO)
            self.bash(HERO)
            self.shield()
            self.attack(HERO)
        self.attack(hero.findNearestEnemy())
    elif MERLIN and self.distanceTo(MERLIN) < 20 and MERLIN.health > 0:
           self.attack(MERLIN)
    elif MUNCHKIN and self.distanceTo(MUNCHKIN) < 20 and MUNCHKIN.health > 0:
            self.attack(MUNCHKIN)
    elif SHAMAN and self.distanceTo(SHAMAN) < 50:
        if hero.canCast("chain-lightning", SHAMAN):
            self.cast("chain-lightning", SHAMAN)
        if SHAMAN.health > 0:
            self.attack(SHAMAN)
    elif ENEMY and self.distanceTo(ENEMY) < 10 and ENEMY.health > 1:
        self.attack(ENEMY)
