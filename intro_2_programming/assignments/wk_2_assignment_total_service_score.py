#Customer score program

def customer_score():
    count = 0
    daily_score = int(input('Enter number of days to score: '))
    for score in range (daily_score):
        score_days = int(input('Enter score for the day: '))
        count += score_days
    print(f'The total score of the {daily_score} days is {count}')
customer_score()