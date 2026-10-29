"""3D dodge prototype in Panda3D: player cube moves on X, blocks fall toward it.
Run: pip install panda3d && python main.py
"""
import random
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText

class Dodge(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self.camera.setPos(0, -30, 12)
        self.camera.lookAt(0, 0, 0)
        self.player = self.loader.loadModel("models/box")
        self.player.reparentTo(self.render)
        self.player.setColor(0.2, 0.6, 1, 1)
        self.blocks, self.keys, self.score, self.alive = [], {"left": 0, "right": 0}, 0.0, True
        for k in ("left", "right"):
            self.accept(f"arrow_{k}", self.keys.__setitem__, [k, 1])
            self.accept(f"arrow_{k}-up", self.keys.__setitem__, [k, 0])
        self.text = OnscreenText(pos=(-1.2, 0.9), scale=0.07, align=0)
        self.spawn_t = 0.0
        self.taskMgr.add(self.update, "update")

    def update(self, task):
        dt = globalClock.getDt()
        if not self.alive:
            return task.cont
        self.score += dt
        x = self.player.getX() + (self.keys["right"] - self.keys["left"]) * 12 * dt
        self.player.setX(max(-10, min(10, x)))
        self.spawn_t -= dt
        if self.spawn_t <= 0:
            b = self.loader.loadModel("models/box")
            b.reparentTo(self.render)
            b.setPos(random.uniform(-10, 10), 0, 20)
            b.setColor(1, 0.3, 0.3, 1)
            self.blocks.append(b)
            self.spawn_t = max(0.25, 1.0 - self.score * 0.01)
        for b in self.blocks[:]:
            b.setZ(b.getZ() - 10 * dt)
            if abs(b.getX() - self.player.getX()) < 1 and abs(b.getZ()) < 1:
                self.alive = False
                self.text.setText(f"Game over: {int(self.score)}")
            elif b.getZ() < -5:
                b.removeNode(); self.blocks.remove(b)
        if self.alive:
            self.text.setText(f"Score: {int(self.score)}")
        return task.cont

Dodge().run()
