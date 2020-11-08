#create program for customer satisfaction count
def customer_score():
    count = 0
    #create daily count 
    day_count = count + 1
    #get usr input for number of days to score
    daily_score = int(input('Enter number of days to score: '))
    #create loop for days selected by usr
    for score in range(daily_score):
        #create usr input for daily score
        score_days = int(input(f'Enter the score for day {day_count}: '))
        #Day count 
        count += score_days
        day_count += 1
        #print results
    print(f'The total score for the {daily_score} days is {count}')
customer_score()
