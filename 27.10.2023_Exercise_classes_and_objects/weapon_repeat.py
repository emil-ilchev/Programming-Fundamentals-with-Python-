class Weapon:

    def __init__(self, bullets: int):
        self.bullets = bullets
        self.num_bullets = []

    def shoot(self):
        if len(self.num_bullets) > self.bullets:
            self.bullets -= 1
            return "shooting..."

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"


weapon = Weapon(5)
print(weapon.shoot())
print(weapon.shoot())
print(weapon)
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon.shoot())
print(weapon)