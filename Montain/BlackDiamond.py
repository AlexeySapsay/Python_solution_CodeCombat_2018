
# Follow me on youtube  channel Phy Tu
# Help with programming on Python, school math, physics
#https://www.youtube.com/channel/UCP5ycahCEZ24qmRRgNnko5Q/featured
    
while True:
    gem = hero.findNearestItem()
    if gem:
        clear = hero.isPathClear(hero.pos, gem.pos)
    else: 
        clear=False
        
    if clear:
        LastHeroPos={"x":hero.pos.x,"y":hero.pos.y}
        hero.moveXY(gem.pos.x,gem.pos.y)
        # Else, move back to the center point.
    else:
        hero.moveXY(LastHeroPos.x,LastHeroPos.y)
        hero.moveXY(40,35)
