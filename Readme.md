Description

A script that extracts specified data from a pdf file to a json file


Prerequisited:
-	Ensure the user running the script has rights to:
		1. Install packages
		2. create and delete files
-	Install packages found under requirements directory using requirements.sh. 

Usage.

-	Extract the zip file into your working directory
-	Have the pdf file inside the script directory (containerdir directory in this case with a sample test.pdf)
-	Install the required modules by running requirements.sh under requirements directory.
		$ cd requirements 
		$ sh requirements.sh
-	Run the extractscript.py with the pdf file as the second argument with python3
		$ cd ..
		$ python3 extractscript.py test.pdf
-	The output of this script is placed under the scripts working directory with the name output.json
		$ ls -l
			extractscript.py
			output.json
			requirements
			test.pdf
