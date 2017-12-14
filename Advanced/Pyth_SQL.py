#! /usr/bin/env python3
import sqlite3
import sys

def Call_SQL():
	conn = sqlite3.connect('data.sqlite3')
	c = conn.cursor()

	#### UPPGIFT 1 #########
	print("1. What species are in the database?")
	for row in c.execute("select * from species;"):
		print(row)

	#### UPPGIFT 2 #########
	print('\n', "2. Add another species to the database: Sus scrofa!")
	c.execute("insert into species(abbrev, name, common) values('Ss','Sus scrofa', 'Wild Boar');")
	for row in c.execute("select * from species;"):
		print(row)

	#### UPPGIFT 3 #########
	print('\n', "3. What proteins are longer than 1000 aa?")
	for row in c.execute("select accession,species,length(sequence) from protein where length(sequence) > 1000 order by length(sequence);"):
		print(row)

	#### UPPGIFT 4 #########
	print('\n',"4. What species are present in family NHR3? Give a full list with full species names using one SQL statement.")
	for row in c.execute("select * from familymembers where family = 'NHR3';"):
		print(row)

	#### UPPGIFT 5 #########
	print('\n', "5. How many proteins from each species are present in the database?")
	for row in c.execute("select species, count(sequence) from protein group by species;"):
		print(row)

	#### UPPGIFT 6 #########
	print('\n', "6. How do you change the schema to add information about a protein's structure?")
	c.execute('''CREATE TABLE Protein_info
			(id integer PRIMARY KEY, Protein_Structure varchar(10), Method varchar(10), Resolution integer(4))''')


	conn.close()
	
	return

Call_SQL()
