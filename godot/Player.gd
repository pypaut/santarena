extends Area2D

export var speed = 300
var screen_size
var look
var attacking

# Called when the node enters the scene tree for the first time.
func _ready():
    screen_size = get_viewport_rect().size
    look = Vector2()
    attacking = false
    $AnimatedSprite.play()
    


func _process(delta):
    var velocity = Vector2()
    if Input.is_action_pressed("ui_right"):
        velocity.x += 1
    if Input.is_action_pressed("ui_left"):
        velocity.x -= 1
    if Input.is_action_pressed("ui_down"):
        velocity.y += 1
    if Input.is_action_pressed("ui_up"):
        velocity.y -= 1
        
    if Input.is_action_pressed("look_right"):
        look.x += 1
    if Input.is_action_pressed("look_left"):
        look.x -= 1
    if Input.is_action_pressed("look_down"):
        look.y += 1
    if Input.is_action_pressed("look_up"):
        look.y -= 1

    if velocity.length() > 0:
        velocity = velocity.normalized() * speed
        if not attacking:
            $AnimatedSprite.animation = "run"
    else:
        if not attacking:
            $AnimatedSprite.animation = "idle"

    position += velocity * delta
    position.x = clamp(position.x, 0, screen_size.x)
    position.y = clamp(position.y, 0, screen_size.y)
    
    if Input.is_action_pressed("attack"):
        attacking = true
    if attacking:
        $AnimatedSprite.animation = "attack"
        
    look = look.normalized()
    $AnimatedSprite.flip_h = look.x < 0
