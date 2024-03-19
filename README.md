# leetcode platform tester
The goal of this project is to implement a platform similar to leetcode

# how to use
To use the tester you must run the main.py specifying the following arguments:
> python3 main.py --name <TEST_CASE_PATH> --input <INPUT_FILE_PATH> --output <OUTPUT_FILE_PATH> --golden <GOLDEN_FILE_PATH>
<br />> PASS

<br /><TEST_CASE_PATH> should contain the solution.py created by the *user* and tester.py created by the *platform*.
The tester.py comes with every problem, with its own way of parsing the arguments string(received as a single line). So the problem creator should add it inside the folder, where it expects the user's solution.py.
<br /><INPUT_FILE_PATH> this file contains arguments of testcases for the specific problem, separated by a newline.
<br /><OUTPUT_FILE_PATH> This is where our test results should be written to. Testcase results are separated by a newline, and each line corresponds to the same index of arguments from --input.
<br /><GOLDEN_FILE_PATH> this file holds the ground truth expected as results for the given --input. It is compared with --output results file, and if all testcases pass, then we see pass on terminal.
