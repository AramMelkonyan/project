import argparse
import sys

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument("Name", help = "test case path")
    parser.add_argument("Input", help = "test inputs file path")
    parser.add_argument("Output", help = "test outputs file path")
    parser.add_argument("Golden", help = "golden file path for comparison")
    args = parser.parse_args()
    return args.Name, args.Input, args.Output, args.Golden


def xor_files(result_path, golden_path):
    res = "PASS"
    try:
        with open (result_path, 'r') as f1:
            try:
                with open (golden_path, 'r') as f2:
                    result_arr = f1.read()
                    golden_arr = f2.read()
                    if len(result_arr) == len(golden_arr):
                        for i in range(len(result_arr)):
                            if result_arr[i] != golden_arr[i]:
                                res = "FAIL"
                                break
                    else:
                        res = "FAIL"
                    print(res)
            except IOError:
                print(f"Cannot open result file: {golden_path}")
    except IOError:
        print(f"Cannot open golden file: {result_path}")


def main():
    test_path, input_path, output_path, golden_path = init()
    sys.path.append(test_path)
    from tester import Evaluator
    try:
        with open(input_path, 'r') as f_in:
            try:
                with open(output_path, 'w') as f_out:
                    evaluator = Evaluator(f_out)
                    # all arguments in one string
                    for args_str in f_in.readlines():
                       evaluator.evaluate(args_str)
            except IOError:
                print(f"Cannot open output file: {output_path}")
    except IOError:
        print(f"Cannot open input file: {input_path}")
        exit(1)
    xor_files(output_path, golden_path)


if __name__ == "__main__":
    main()
    # input("please enter to exit")
