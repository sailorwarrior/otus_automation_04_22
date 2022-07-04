This function is created as as homework for OTUS test automation course
The function should be run from linux terminal using "python linux_logs_analysis.py" command.
The result of the function execution will be printed to a terminal and saved as a separate JSON file in the same
diractory as a target log file.
Function accepts 2 arguments:
-f : path to a log file
-d : path to a log directory
-d and -f arguments could be used simultaneosly.
At least one of the arguments should be provided, otherwise the script will fail with AttributeError.
Provided paths should be absolute or relative to the terminal's CWD.
Function will only process files with .log extension
