
def genReport(dd):
    dottedline = '-'*70
    template = '{0:8} | {1:10} | {2:3} | {3:3} | {4:3} | {5:3} | {6:3} | {7:6} | {8:3}'
    print('CLASS REPORT')
    print(dottedline)
    print(template.format('REGID', 'NAME', 'AGE', 'P', 'C', 'M', 'B', 'AVG', 'R'))
    print(dottedline)
    for regid in dd.keys():
        name = dd[regid]['name']
        age  = dd[regid]['age']
        regid = dd[regid]['regid']
        phy = dd[regid]['phy']
        chem = dd[regid]['chem']
        math = dd[regid]['math']
        bio = dd[regid]['bio']
        avg = dd[regid]['avg']
        rank = dd[regid]['rank']
        print(template.format( regid, name, age,phy, chem, math, bio, avg, rank))
    print(dottedline)

# ------------ [LAB] Complete the write2file() --------------- #
def write2file(dd, path):
    pass
# ------------ ------------------------------- --------------- #



# Read the csv file as a text file
path = r"students.csv"
f = open(path)
content  = f.readlines()
f.close()

print(content)
print('-'*60 + ' > First Step')



# ------------------------ csv file is read and its content is available for further processing

# Read the coloums --> name,age,regid,phy,chem,math,bio,avg,rank
# Read a row --> "Vijay,14,HPE001,99,98,97,96,0,0"
# Construct a dictionary out of the column and the row
# Add that dictionary to the main dictionry that represents the class
# Repeat this process for all the entries in the csv file

classdict = {}
coldata = content[0]
columns = [s.strip() for s in coldata.split(',')]

for rowdata in content[1:]:
    rows = [s.strip() for s in rowdata.split(',')]
    temp = dict(zip(columns, rows))
    classdict[temp['regid']] = temp

print(classdict)
print('-'*60 + ' > Second Step')

# ------------------------- csv data is in the form of a dictionary

# Access the dictionary iteratively and calculate the average marks and
# update in the dictionary

# ------------ [LAB] Average calculation --------------- #

print(classdict)
print('-'*60 + ' > Third Step')

# ------------------------- dictionary updated with average data

# Calculate the rank
# collect all the averages -> into a list
# arrange the averages in descending order
# iterate the entire dictionary and update the rank based on the descending
# order of averages

# ------------ [LAB] Rank calculation --------------- #

print(classdict)
print('-'*60 + ' > Fourth Step')   



# ------------------------- dictionary updated with rank data

# Re-write the csv file

path = r"students_completed.csv"
f = open(path, "w")

# ------------ [LAB] Write a csv file with updated information --------------- #

f.close()

# ------------------------- resultant csv file is now ready with averages and ranks updated

genReport(classdict)
