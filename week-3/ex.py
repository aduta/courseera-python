d = {"Johnny": "5 years old", "Sally": "7 years old", "Eva":"10 years old",
 "Peggy": "7 years old"}


namelist = ["George", "Sally", "Catherine", "James", "Peggy"]
x,y,z = "George","Sally","Catherine"
mytuple = x,y,z
agedict = {"George":"17","Sally":"19",
             "Catherine":"18"}

def write_to_file(filename, myname, myage, major):
    # open file first
    outfile = open(filename, 'w')
    outfile.write("My name is "+ myname + " \n")
    outfile.write("My age is "+ myage + " \n")
    outfile.write("I am majoring in "+ major + " \n")
    outfile.close()

# write_to_file('namefile.txt', 'Anshul', 43, 'Maths')        

import csv
def read_csv_file(filename):
	infile = open(filename)
	rows = csv.reader(infile)
	for row in rows:
		print(row[0], row[1], row[2])

def write_csv(filename):
    import csv
   
    L = [['Date', 'Name', 'Notes'], 
         ['2016/1/18', 'Martin Luther King Day', 'Federal Holiday'],
         ['2016/2/2','Groundhog Day', 'Observance'], 
         ['2016/2/8','Chinese New Year', 'Observance'], 
         ['2016/2/14','Valentine\'s Day', 'Obervance'], 
         ['2016/5/8','Mother\'s Day', 'Observance'], 
         ['2016/8/19','Statehood Day', 'Hawaii Holiday'], 
         ['2016/10/28','Nevada Day', 'Nevada Holiday']]
    
    f = open(filename, 'w', newline='')
    for item in L:
        csv.writer(f).writerow(item)
    f.close()

write_csv('BooksWritten.csv')
