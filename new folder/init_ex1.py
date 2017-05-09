class Enemy:
    def __init__(self, x):
        self.energy = x
    def get_energy(self):
        print(self.energy, "is the enemy's strength")

bob = Enemy(5)
scorpy = Enemy(25)
boss = Enemy(100)

bob.get_energy()
scorpy.get_energy()
boss.get_energy()