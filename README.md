Task 1: Given the 'scores.csv' file containing student's name, test scores, and project score, we'd create a new csv file that add an extra column, grade, to each student with following rubrics: - each test score weights 20% while the project weights 40% - if a student receives: - 90% or above, give an A; - 80% to 90% (not including 90%), give a B; - with the rest assigning a C grade. - Save the new data (with grade) to 'grades.csv' - Note: you may process .csv file in Python directly, or use Pandas dataframe to add a column, then save the dataframe to csv.

Task 2: The given 'names.txt' file is a collection of student names. (a) For each student, randomly generate a GPA in the range of [2.0 to 4.0], (b) as well as randomly choose a major from the major list ['CS','Bio','Chem','Math']. (c) Save the results (name, GPA, major) to a csv file, say, profile.csv

Task 3: Database practice
(a) Create a database that contains two tables, one from the above grades.csv file and one from the above profile.json file. Use names as unique. In case you spot any duplicate names in the data file, please ignore/delete the duplicates (only keep the first appearance).

(b) Grade inquiry -- Select one student by name and display their grade.

(c) Change of Major processing -- Select a student and update their major. (e.g. display the current major, then enter the new major, then update the database, or what you think is a reasonable way to handle.)

(d) Select excellent CS students – find names of all CS students who earned an A grade or with GPA > 3.5.

(e) Do an additional database query operation of your choice.
