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

def attack(enemy):
    if hero.isReady("attack"):
        hero.attack(enemy)
    elif hero.isReady("bash") and enemy.health > 0:
        hero.bash(enemy)
    else:
        hero.shield()
            
        
def castLightning(enemy):
    if hero.canCast("chain-lightning", enemy):
        hero.cast("chain-lightning", enemy)


INITIALPOSITION = hero.pos;






CIRCLE=[[110, 90], [125, 79], [125, 57], [115, 46], [105, 46], [95, 57], [95, 79], [105, 91]]
def MoveInCircle(side, C, POS):
    if side == "LEFT":
        hero.moveXY(C[POS][0] - 60, C[POS][1])
        if POS < 7:
            POS=POS+1
        else:
                POS=0
    elif side == "RIGHT":
        hero.moveXY(C[POS][0], C[POS][1])
        if POS < 7:
            POS=POS+1
        else:
            POS=0
    else:
        hero.say("ERROR")
    return POS
        
        
SIDE="LEFT"       
C_POS=0        
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
    
    
        
    if enemiesAtDistance(20) > 2:
        if ENEMY and hero.canCast("chain-lightning", ENEMY):
            castLightning(ENEMY)
        else:
            attack(ENEMY)
            C_POS=MoveInCircle(SIDE, CIRCLE, C_POS)
            hero.shield()
            
            
    elif HERO and self.distanceTo(HERO) < 5 :
        castLightning(HERO)
        while HERO.health > 0:
            attack(HERO)
            
            e = hero.findNearestEnemy()
            if hero.distanceTo(e)<5:
                hero.attack(e)
    elif ENEMY and hero.distanceTo(ENEMY) < 3:
        attack(ENEMY)
    elif BURL and self.distanceTo(BURL) < 15:
        castLightning(BURL)
        if BURL.health > 0:
            if hero.isReady("bash"):
                if hero.canElectrocute(BURL):
                    hero.electrocute(BURL)
                self.bash(BURL)
            if BURL.health > 0:
                attack(BURL)
    elif OGRE and self.distanceTo(OGRE) < 15:
        castLightning(OGRE)
        if OGRE.health > 0:
            if hero.isReady("bash"):
                if hero.canElectrocute(OGRE):
                    hero.electrocute(OGRE)
                self.bash(OGRE)
            if OGRE.health > 0:
                attack(OGRE)
    elif FANGRIDER and self.distanceTo(FANGRIDER) < 60:
        castLightning(FANGRIDER)
        e = hero.findNearestEnemy()
        if hero.distanceTo(e)<2:
                attack(e)
        elif FANGRIDER.health > 0:
            if hero.canElectrocute(FANGRIDER):
                hero.electrocute(FANGRIDER)
            attack(FANGRIDER)
    elif THROWER and self.distanceTo(THROWER) < 30:
        if THROWER.health > 0:
            attack(THROWER)
    elif SKELETON and self.distanceTo(SKELETON) < 20:
        if hero.canElectrocute(OGRE):
            hero.electrocute(OGRE)
        attack(SKELETON)
    elif BRAWLER and self.distanceTo(BRAWLER) < 20:
        if hero.canElectrocute(BRAWLER):
            hero.electrocute(BRAWLER)
        attack(BRAWLER)
    elif MERLIN and self.distanceTo(MERLIN) < 20 and MERLIN.health > 0:
        attack(MERLIN)
    elif MUNCHKIN and self.distanceTo(MUNCHKIN) < 20 and MUNCHKIN.health > 0:
        attack(MUNCHKIN)
    elif SHAMAN and self.distanceTo(SHAMAN) < 50:
        attack(SHAMAN)
    elif ENEMY and self.distanceTo(ENEMY) < 10 and ENEMY.health > 1:
        attack(ENEMY)
