# create a sales invoice finder program

# create a sales invoice finder program

# create main function
def main():
# set search criteria to empty until defined by user
    search_criteria = None
# instructions to help user perform search
    while True:
        search_criteria = input("Enter 'id' to search by invoice id or 'lname' to search by customer last name: ")
        if search_criteria == 'id' or search_criteria == 'lname':
            break
        else:
            print("Please enter how you would like to search:  Enter 'id' to search by invoice id or 'lname' to search by customer last name")

 # user select customer from file to look up   
    search_term = input("Enter customer invoice id or  last name to look-up: ")
 # file to open and searched   
    sales_file_name = open('sales_data.csv', 'r')
    lines = sales_file_name.readlines()
#  set records 
    matched_records = 0
# loop through records in file
    for line in lines:
   
        line_search = line.strip().split(',')
   

        target_column = 2
        if search_criteria =='id':
            target_column = 0
    
        if line_search[target_column] == search_term:
            print(line.strip())
            matched_records += 1
#print results
    print('records found: {0}'.format(matched_records))
# close file searched
    sales_file_name.close()

#call function
main()
