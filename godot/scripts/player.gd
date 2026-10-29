extends CharacterBody2D
## Player controller: left/right movement clamped to screen.
@export var speed := 400.0

func _physics_process(_delta: float) -> void:
	var dir := Input.get_axis("ui_left", "ui_right")
	velocity.x = dir * speed
	move_and_slide()
	position.x = clamp(position.x, 20.0, get_viewport_rect().size.x - 20.0)
