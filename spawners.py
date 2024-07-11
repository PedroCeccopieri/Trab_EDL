from src.blocks.bulletLauncher import BulletLauncher

def checkBullets(blockGroup, enemyGroup):

    bullets = []
    
    for b in blockGroup:
        if (isinstance(b, BulletLauncher)):
            if (b.shoot):
                b.shoot = False
                bullets.append(b.getBullet())

    for b in bullets:
        enemyGroup.add(b)