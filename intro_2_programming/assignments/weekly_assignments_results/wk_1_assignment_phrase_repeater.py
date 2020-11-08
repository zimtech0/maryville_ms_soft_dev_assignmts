# program that repeats a phrase, given by a user, the number of times a user requests it be repeated.

def phrase_repeater():
# user phrase to be repeated
    phrase_to_repeat = input("Please enter a phrase you would like to repeat: ")
# user requested times to repeat ..based on usr input   
    repeat_times=(int(input("Please enter the number of time you would like the phrase repeated: ")))
    for times_repeated in range (1,repeat_times+1):
       
 #print output/ order list  with phrase repeated
        print(str(times_repeated) + '. ' + phrase_to_repeat)   
phrase_repeater()