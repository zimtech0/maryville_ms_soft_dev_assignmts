

# create a program to read sales numbers from a text file, total the rows and outputs the data into a new file

# create main function
def main():

# empty list to hold processed file results
    allNums = [] 
    in_file_name = input("Please enter the file name and directory you wish to use: ")
    in_file =  open(in_file_name, "r+") 
    out_file_name = input("Please enter the output file name: ")
    out_file = open(out_file_name, "w+") 
# read text file
    data = in_file.readlines() # read the text file 
    for line in data: 
        allNums += line.strip('#').split() # get a list containing all the numbers in the file 
    index_0 = float(allNums[0].strip('$'))
    index_1 = float(allNums[1].strip('$'))
    index_2 = float(allNums[2].strip('$'))
    index_3 = float(allNums[3].strip('$'))
    index_4 = float(allNums[4].strip('$'))
    index_5 = float(allNums[5].strip('$'))

# create totals variables
    row_1 = index_0 + index_1
    row_2 = index_2 + index_3
    row_3 = index_4 + index_5

    
# print results to screen for review
    print('${0:>8}'.format(index_0), '${0:>8}'.format(index_1), '${0:>8}'.format(row_1),file=out_file)
    print()
    print('${0:>8}'.format(index_2), '${0:>8}'.format(index_3), '${0:>8}'.format(row_2),file=out_file)
    print()
    print('${0:>8}'.format(index_4), '${0:>8}'.format(index_5), '${0:>8}'.format(row_3),file=out_file)
    

    print("Done writing totals to: ",out_file_name)

main()