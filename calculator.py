import sys, argparse
import calcFunctions as calc

def main():
    parser = argparse.ArgumentParser(description="Calculator CLI")
    parser.add_argument("--add", type=int, nargs='+', help="Addition function.")
    parser.add_argument("--sub", type=int, nargs='+', help="Subtraction function.")
    parser.add_argument("--mul", type=int, nargs='+', help="Multiplication function.")
    parser.add_argument("--div", type=int, nargs='+', help="Division function.")
    parser.add_argument("--sqrt", type=int, help="Square Root function. Takes only 1 argument.")
    parser.add_argument("--cbrt", type=int, help="Cube Root function. Takes only 1 argument.")
    parser.add_argument("--pow", type=int, nargs='+', help="Power function. Takes only 2 arguments.")
    parser.add_argument("--avg", type=int, nargs='+', help="Average of numbers function.")
    parser.add_argument("--abs", type=int, nargs='+', help="Absolute value function.")
    parser.add_argument("--sin", type=float, help="Sine function. Takes only 1 argument.")
    parser.add_argument("--cos", type=float, help="Cosine function. Takes only 1 argument.")
    parser.add_argument("--tan", type=float, help="Tangent function. Takes only 1 argument.")
    parser.add_argument("--asin", type=float, help="ASIN function. Takes only 1 argument.")
    parser.add_argument("--acos", type=float, help="ACOS function. Takes only 1 argument.")
    parser.add_argument("--atan", type=float, help="ATAN function. Takes only 1 argument.")
    parser.add_argument("--log", type=int, nargs='+', help="Logarithmic function. Takes 2 arguments. (Num and Base)")
    parser.add_argument("--loge", type=int, help="Logarithmic function. Takes 1 argument")
    parser.add_argument("--log10", type=int, help="Logarithmic with base 10 function. Takes 1 argument")

    args = parser.parse_args()

    if args.add is not None:
        print(calc.add(args.add))
    if args.sub is not None:
        print(calc.sub(args.sub))
    if args.mul is not None:
        print(calc.mul(args.mul))
    if args.div is not None:
        print(calc.div(args.div))
    if args.sqrt is not None:
        print(calc.sqrt(args.sqrt))
    if args.cbrt is not None:
        print(calc.cbrt(args.cbrt))
    if args.pow is not None:
        print(calc.pow(args.pow))
    if args.avg is not None:
        print(calc.avg(args.avg))
    if args.abs is not None:
        print(calc.abs(args.abs))
    if args.sin is not None:
        print(calc.sin(args.sin))
    if args.asin is not None:
        print(calc.asin(args.asin))
    if args.cos is not None:
        print(calc.cos(args.cos))
    if args.acos is not None:
        print(calc.acos(args.acos))
    if args.tan is not None:
        print(calc.tan(args.tan))
    if args.atan is not None:
        print(calc.atan(args.atan))
    if args.log is not None:
        print(calc.log(args.log))
    if args.loge is not None:
        print(calc.loge(args.loge))
    if args.log10 is not None:
        print(calc.log10(args.log10))
        
        
if __name__ == "__main__":
    main()
