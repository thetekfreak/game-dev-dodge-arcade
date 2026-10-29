extends Area2D
## Falling block. Emits hit_player on contact, frees itself off-screen.
signal hit_player
@export var fall_speed := 250.0

func _ready() -> void:
	body_entered.connect(func(b): if b is CharacterBody2D: hit_player.emit())

func _process(delta: float) -> void:
	position.y += fall_speed * delta
	if position.y > get_viewport_rect().size.y + 40:
		queue_free()
