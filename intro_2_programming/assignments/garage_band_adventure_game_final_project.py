#create a garage band text based adventure game.

from os import name
import random

#legends of rock ...enemies
enemy_name_list = ["Aerosmith", "Motley Crue", "ZZ Top", "Bon Jovi"]
enemy_intro_list = ["Walk this way!", "Dr. Feelgood", "La Grange", "Living on a prayer!"]
s = '\n\n{x[0]}: Walk this way! \n\n{x[1]}: Dr. Feelgood \n\n{x[2]}: Le Grange\n\n{x[3]}: Living on a prayer!'
x = ["Aerosmith", "Motley Crue", "ZZ Top", "Bon Jovi"]


# Band_name class
class Band_name:
    # Initializer
    def __init__(self, name, grammy_awards, MTV_points):
        self.name = name
        self.position = 0
        self.grammy_awards = grammy_awards
        self.MTV_points = MTV_points
    # print(band/adventurer name) will call this
    def __str__(self):
        ret = "---------------------------------------------------------------\n"
        ret += "Band Name : " + self.name + "\n"
        ret += "Final Chart Ranking : " + str(self.position) + "\n"
        ret += "Grammy Awards : " + str(self.grammy_awards) + "\n"
        ret += "MTV Points : " + str(self.MTV_points) + "\n"
        ret += "---------------------------------------------------------------\n"
        return ret

# Enemy class
class Enemy:
    # Initializer
    def __init__(self, name, position, introduction, damage):
        self.name = name
        self.position = position
        self.introduction = introduction
        self.damage = damage
    def __str__(self):
        ret = "---------------------------------------------------------------\n"
        ret += "Enemy : " + self.name + "\n"
        ret += "Position : " + str(self.position) +"\n"
        ret += "Song : " + str(self.introduction) + "\n"
        ret += "Damage : " + str(self.damage) + "\n"
        ret += "---------------------------------------------------------------\n"
        return ret

# Main game loop
def play(adventurer, enemies, path_length):
    print("\n\nSo you wanna be a rock star!.  We'll here's your chance. \n\nCollect enough Grammy Awards without losing MTV points\n")
    print(".. all while going head to head with the Legends:\n\n")
    print (s.format (x=x))
    print("\n\n..Win and get the chance to go on tour!\n")
    print('..Lose and back to the garage you go!\n')
    print("So if you think your band has what it take's..then let's Rock Out!")

    for i in range(1, path_length+1): # Loop over the path
        input("\nPress RETURN and..Let's Get it!.\n") # Wait for keypress
        adventurer.position = i # Move adventurer/band forward
        print(adventurer.name + " Rolling Stone Chart position wk: " + str(adventurer.position))
        for enemy in enemies:
            if adventurer.position == enemy.position: # If there's an enemy at this position,
                adventurer.MTV_points -= enemy.damage # it causes damage to the adventurer/band
                print("Got attacked by " + enemy.name + " and lost " + str(enemy.damage) + " MTV Points")
                break
        else: # This gets executed if no enemy was encountered
            pickup = random.randint(11, 50)
            adventurer.grammy_awards += pickup
            print("\nRecieved " + str(pickup) + " Grammy Awards")
        if adventurer.MTV_points <= 0: # If the adventurer/band has fallen in chart rankings
            print("\n\n" + adventurer.name + " lost..back to the garage you go!")
            break
    else:
        print("\nParty up! " + adventurer.name + " won!..Get ready to go on tour.") # If adventurer/band reached the end of the game

# Initialize players, start the game, show results
def main():
    path_length = 11
    adventurer = Band_name("Rock-a-Lot", 0, 100)
    num_enemies = random.randint(int(0.3*path_length), int(0.7*path_length)) # 30%-70% steps will have enemies
    enemies = []
    for _ in range(num_enemies):
        enemy_name, enemy_intro = random.choice(enemy_name_list), random.choice(enemy_intro_list)
        enemy_position, enemy_damage = random.randint(1, path_length), random.randint(20, 50)
        enemies.append(Enemy(enemy_name, enemy_position, "It's " + enemy_name + enemy_intro, enemy_damage))
    play(adventurer, enemies, path_length) # Play the game
    print("\n\nBand Stats Totals:") # Print the results
    print(adventurer)

if __name__ == "__main__":

    
    main()