extends Area2D

export var speed = 300
var screen_size
var look


func _ready():
    screen_size = get_viewport_rect().size
    look = Vector2()
    $AnimatedSprite.play()


func _process(delta):
    # Movement
    var velocity = Vector2()
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1
    if Input.is_action_pressed("ui_down"):
        velocity.y += 1
    if Input.is_action_pressed("ui_up"):
        velocity.y -= 1
    velocity = velocity.normalized() * speed
    position += velocity * delta
    position.x = clamp(position.x, 0, screen_size.x - 50)
    position.y = clamp(position.y, 0, screen_size.y - 50)

    # Look
    if Input.is_action_pressed("look_right"):
        look.x += 1
    if Input.is_action_pressed("look_left"):
        look.x -= 1
    if Input.is_action_pressed("look_down"):
        look.y += 1
    if Input.is_action_pressed("look_up"):
        look.y -= 1
    look = look.normalized()

    # Animation
    if velocity.length() > 0:
        $AnimatedSprite.animation = "run"
    else:
        $AnimatedSprite.animation = "idle"

    $AnimatedSprite.flip_h = look.x < 0
