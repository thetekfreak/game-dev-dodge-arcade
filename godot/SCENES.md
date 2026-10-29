Build these scenes in the Godot editor (scene files are editor-generated):
- `Main.tscn`: Node2D (main.gd) > Player (CharacterBody2D, player.gd, Sprite + CollisionShape2D), SpawnTimer (Timer, autostart), UI (CanvasLayer) > Score (Label). Set `block_scene` to Block.tscn.
- `Block.tscn`: Area2D (block.gd) > ColorRect + CollisionShape2D.
