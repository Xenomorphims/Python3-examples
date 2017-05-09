class Enemy:
    life = 100

    def attack(self):
        print('Ouch!')
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print('The Enemy Is Dead')
        else:
            print(str(self.life) + ' life left')


enemy1 = Enemy()
enemy2 = Enemy()
enemy3 = Enemy()

enemy1.check_life()
enemy2.check_life()
enemy1.check_life()

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy2.attack()
enemy2.attack()
enemy2.attack()
enemy1.attack()
enemy2.attack()
enemy1.attack()
enemy3.attack()
enemy1.attack()
enemy3.attack()
enemy2.attack()
enemy3.attack()
enemy3.attack()
enemy2.attack()

enemy1.check_life()
enemy2.check_life()
enemy3.check_life()