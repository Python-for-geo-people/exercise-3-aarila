# Exercise-3

The exercise for this week is meant to help you to understand (for) loops and conditional statements in Python.
Below you have a series of "problems" in which you will be asked to either download and modify, or create new script files.
After making you changes, you will need to upload them to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

## Henkka's earlier exercises related to loops and conditional statements

_Note to lecturers: In AutoGIS course we will produce a lot of output files where there are numbers and text combined. Thus it would be useful to practice those. 
Also I think one topic that should be covered at some point are the escape characters (`\n, \t`) as they are often present when processing text data_ 

Create a variable called *name* with text "Animal". 

### Looping

Here we practice looping over numbers and concatenating strings and numbers. 

a) 
Iterate over numbers 0-30 and print out text as follows: 


    Animal_0
    Animal_1
    Animal_2
    [...]
    [...]
    Animal_30


b)
Create an empty string variable called *text* (`text = "" `). 
Update the *text* variable to contain text as follows (notice --> escape character (`\n`) for newline required): 

    Animal_10.shp
    Animal_11.shp
    Animal_12.shp
    [...]
    [...]
    Animal_30.shp

### Nested loops (optional)

_NOTE: I don't know if we have time to go through 

a)
Create variable *star* with text "\*" and an empty string variable *text*. Use (nested) for-loops to produce following formation: *(2 pnts)*

        *******
        *******
        *******
       
b)
Create variables *star* with text "\*", *line* with text "-" and an empty text variable *flag* (`flag = ""`). 
Use (nested) for-loops and variables *star* and *line* to produce following formation into variable *flag* and print out the result as follows. Hint: you will need
to use a conditional statement to produce the output. : 

        *******------------
        *******------------
        *******------------
        -------------------
        -------------------

## Conditional statements: Working with projections

In Python there is a handy way of asking input from the user using `input` function such as:

   ```python
   >>> name = input('What is your name?\n')
   ... What is your name?
   ... 'Henrikki'
   >>> print("Hello", name)
   ... 'Hello Henrikki'
   ```

- Create a simple program that asks "Determine the EPSG value of the input shapefile."
    - If the user says 4326 print "EPSG value 4326 corresponds to WGS84"
    - If the user says 3067 print “EPSG value 3067 corresponds to ETRS-TM35FIN"
    - If the user says 2392 print “EPSG value 2392 corresponds to KKJ / Finland zone2"
    - If the user mentions any other EPSG value print “There are so many spatial references..I don’t know them all, sorry."

# Answers

## Problem 1


