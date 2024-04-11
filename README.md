Assignment is written in python 3.
Assigned method is saved in file verify_input_json.py. 
It is named verify_input_json() and reguires path to json file, saved as string.
It returns boolean value.
There is also created custom exception for invalid data format (AWS::IAM::Role Policy).
Unit tests are saved in file main.py.
During unit tests there is created json file (file.json) to verify work of mehtod.

!!!
Requirments:
Python 3.9+

!!!
HOW TO RUN:
a) Method:
* Create python file in same folder as method (example.py)
* Import function: from verify_input_json import verify_input_json
* Provide data for method (path to json file you want to verify saved as string): verify_input_json('file.json')
* Method returns bool
* Run this command in shell in this folder: python name_of_your_file.py

example.py:

from verify_input_json import verify_input_json

verify_input_json('file.json')

shell:

python name_of_your_file.py


b) Unit tests:
* Run this command in shell in this folder: python main.py

shell:

python main.py
