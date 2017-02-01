# To see how the various functions in the DB-API work, take a look at this code,
# then the results that it prints when you press "Test Run".
#
# Then modify this code so that the student records are fetched in sorted order
# by student's name.
#

import sqlite3

# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by students.name;"
c.execute(query)
rows = c.fetchall()

# First, what data structure did we get?
print "Row data:"
print rows

# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]

db.close()

"""
results as follows:

Row data:
[(u'Jade Harley', 441304), (u'Harry Evans-Verres', 172342), (u'Taylor Hebert', 654321), (u'Diane Paiwonski', 773217), (u'Melpomene Murray', 102030), (u'Robert Oliver Howard', 124816), (u'Hoban Washburne', 186753), (u'Trevor Bruttenholm', 162636), (u'Jonathan Frisby', 917151)]

Student names:
   Jade Harley
   Harry Evans-Verres
   Taylor Hebert
   Diane Paiwonski
   Melpomene Murray
   Robert Oliver Howard
   Hoban Washburne
   Trevor Bruttenholm
   Jonathan Frisby


"""
