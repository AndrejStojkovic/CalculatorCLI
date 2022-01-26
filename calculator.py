import sys, argparse
import calcFunctions as calc

def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")

    funcs = {
        #arg: description
        "add": "Addition function.",
        "sub": "Subtraction function.",
        "mul": "Multiplication function.",
        "div": "Division function.",
        "sqrt": "Square Root function. Takes 1 argument.",
        "cbrt": "Cube Root function. Takes 1 argument.",
        "pow": "Power function. Takes 2 arguments.",
        "avg": "Average of numbers function.",
        "abs": "Absolute value function.",
        "sin": "Sine function. Takes 1 argument.",
        "cos": "Cosine function. Takes 1 argument.",
        "tan": "Tangent function. Takes 1 argument.",
        "asin": "ASIN function. Takes 1 argument.",
        "acos": "ACOS function. Takes 1 argument.",
        "atan": "ATAN function. Takes 1 argument.",
        "log": "Logarithmic function. Takes 2 arguments. (Num and Base)",
        "loge": "Logarithmic function. Takes 1 argument",
        "log10": "Logarithmic function with base 10 default. Takes 1 argument"
    }

    for key, value in funcs.items():
        parser.add_argument("--" + key, type=float, nargs='+', help=value)
        
    args = parser.parse_args() 

    argDict = {
        calc.add:args.add, calc.sub:args.sub, calc.mul:args.mul, calc.div:args.div, calc.sqrt:args.sqrt, calc.cbrt:args.cbrt,
        calc.pow:args.pow, calc.avg:args.avg, calc.abs:args.abs, calc.sin:args.sin, calc.asin:args.asin, calc.cos:args.cos,
        calc.acos:args.acos, calc.tan:args.tan, calc.atan:args.atan, calc.log:args.log, calc.loge:args.loge, calc.log10:args.log10
    }

    for key, value in argDict.items():
        if value is not None:
            res = key(value)
            if res - int(res) == 0:
                print(int(res))
            else:
                print(res)
        
        
if __name__ == "__main__":
    if not sys.argv[1:]:
        print("Usage: python {} -h (--help)".format(sys.argv[0]))
    main()
