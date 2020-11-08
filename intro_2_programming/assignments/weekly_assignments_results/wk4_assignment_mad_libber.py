                                               
# create lyrics to the song and implement literals
song_lyrics = """                                       
A fat {animal} live in a hat.  This {animal}
liked singing and  {activity}, quaratine, was like a bad dream
so no one could {activity}.  But the weekend came and the  {animal} 
wanted to {activity}.  So the 
{animal} took a chance and went to the  {size} city, where it could
 {activity} as  much as it wanted.  However,
the {animal} became sick, because of his trick and could not {activity} for 14 days.

LA..LA..LA..LALALALA
"""                                                 
#create main function
def sing_song():   
 # define literals                                     
    cues = ['animal', 'activity', 'size']     
# create list to keep user picks        
    user_picks = dict()                                                                                  
    for cue in cues:                          
        add_pick(cue, user_picks)               
    song = song_lyrics.format(**user_picks)
    print(song)
                           

def add_pick(cue, dictionary):
  # prompt user to make the animal selection 
    user_prompt_message = "Enter any  {name} you like!: "
    prompt = user_prompt_message.format(name=cue)
    response = input(prompt)
    dictionary[cue] = response                                                             

sing_song()                                      

