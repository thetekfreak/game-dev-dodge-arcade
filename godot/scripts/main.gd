extends Node2D
## Spawns falling blocks, tracks score, handles game over and restart.
@export var block_scene: PackedScene
var score := 0.0
var alive := true

func _ready() -> void:
	$SpawnTimer.timeout.connect(_spawn)

func _process(delta: float) -> void:
	if alive:
		score += delta
		$UI/Score.text = "Score: %d" % int(score)
	elif Input.is_action_just_pressed("ui_accept"):
		get_tree().reload_current_scene()

func _spawn() -> void:
	var b := block_scene.instantiate()
	b.position = Vector2(randf_range(20, get_viewport_rect().size.x - 20), -20)
	b.hit_player.connect(_on_hit)
	add_child(b)
	# Speed up spawning as score grows
	$SpawnTimer.wait_time = max(0.25, 1.0 - score * 0.01)

func _on_hit() -> void:
	alive = false
	$SpawnTimer.stop()
	$UI/Score.text = "Game over: %d  (Enter to restart)" % int(score)
