mySprite: Sprite = None
projectile: Sprite = None

def on_on_destroyed(sprite):
    info.change_score_by(1)
sprites.on_destroyed(SpriteKind.enemy, on_on_destroyed)

def on_on_overlap(sprite2, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . 7 7 . . . . . . . . . . .
        . . . 7 7 7 7 . . . . . . . . .
        . . . 7 . . 7 7 7 . . . . . . .
        . . . 7 . . . . 7 7 7 . . . . .
        . . . 7 . . . . . . 7 7 7 . . .
        . . . 7 . . . . . . . . 7 7 7 .
        . . . 7 . . . . . . 7 7 7 . . .
        . . . 7 . . . . 7 7 7 . . . . .
        . . . 7 . . 7 7 7 . . . . . . .
        . . . 7 7 7 7 . . . . . . . . .
        . . . 7 7 . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 0, 50)
mySprite.x = 8
mySprite.set_stay_in_screen(True)
info.set_score(0)

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        -150,
        0,
        SpriteKind.enemy)
    projectile.set_position(scene.screen_width(), randint(0, scene.screen_height()))
    if info.score() < 10:
        projectile.vx += 100
game.on_update_interval(500, on_update_interval)
