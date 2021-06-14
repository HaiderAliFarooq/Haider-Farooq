IDE: Pycharm
Programming Language: Python (Version 3.9.5)
Framework:  Pytest
Reporting: Pytest HTML

Setup Instructions:
1. First, we will need to Install Pytest
   a. Go to File > Settings > Project Interpreter > + > write pytest > install packages
2. Install Requests
   a. Go to File > Settings > Project Interpreter > + > write Requests > install packages
3. For reporting install pytest-html
   a. Go to File > Settings > Project Interpreter > + > write pytest-html > install packages
4. Install PyYAML
   a. Go to File > Settings > Project Interpreter > + > write PyYAML > install packages
5. Set Default test runner: pytest from File > Settings > Python Integrated Tools
6. Edit Configurations and set the Additional Arguments in Python Tests as
 --html=Test_Reports/APIPlayGround_test_results.html for reporting.

To view the execution results:
Test_Cases/Test_Reports/APIPlayGround_test_results.html