Team Green Monkeys; Daniel He, Faiyaz Rafee
SoftDev  
K17 -- SQLite  
2022-10-25  
time spent: 0.5 hrs
# How to SQLite 

## Terminal 
Type "sqlite3" into the terminal to create a temporary database that will be deleted when you exit the program. Exit through CTRL+D

# Tables
The follow command with proper parameters filled will create a table: 
```
create table <name\> (<column name\> <data type\>, ... , <column name\> <data type\>);
```
* All SQLite commands need to be terminated with a semicolon before it is executed.  
* `Data types`: 
  * Null
  * Integer
  * Real (floating point value)
  * Text (string)
  * Blob (blob)
  * Booleans are just stored as 1 or 0

### INSERTION
``` 
insert into <name> values (<field 1>, ... , <field n>)
```
* Not filling out all the fields of a column is WRONG. Parse error. Blanks can be filled with NULL.
* Without PRIMRARY KEY specified at the end of the data type declaration, fields in a single column can be the same, values can be NULL.  

### QUERYING 
```
select <field> from <name>
select <field> from <name> where <field> = <value>
```
* If multiple <field\> are the same, it will return all of them 