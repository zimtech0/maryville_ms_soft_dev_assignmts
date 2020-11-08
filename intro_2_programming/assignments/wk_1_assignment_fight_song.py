# Program to output fight song

#lyric go team go
def go_team_go():
    print ("Go, team, go!")
    print ("Defeat your foe.")

#lyric repeating section
def repeating_lyrics():
    print ("Go, team, go!")
    print ("Defeat your foe.")
    print("Simply the best,")
    print ("Better than the rest.")
    print ("Go, team, go!")
    print ("Defeat your foe.")

    

# function named `sing_fight_song`
def sing_fight_song():
    go_team_go()
    print()

    for go_team_go_repeat in range(2):
         repeating_lyrics()  
         print()
    go_team_go()
    

sing_fight_song()
    





