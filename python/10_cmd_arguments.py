import sys

print(sys.argv)
print(sys.argv[0])              # script name
print(len(sys.argv))

import argparse

# BASICS
# python 09_cmd_arguments.py --name Alice --age 25 --city Boston

parser = argparse.ArgumentParser(description="Demo CLI")
parser.add_argument("--name", default="Guest")
parser.add_argument("--age", type=int, default=0)
parser.add_argument("--city", default="Unknown")

args = parser.parse_args()
print(args.name, args.age, args.city)

# SHORT & LONG FLAGS
# python 09_cmd_arguments.py -n Alice -a 25 or python 09_cmd_arguments.py --name Alice --age 25

parser2 = argparse.ArgumentParser()
parser2.add_argument("-n", "--name", default="Guest")
parser2.add_argument("-a", "--age", type=int, default=0)

# BOOLEAN FLAG
# python 09_cmd_arguments.py --verbose

parser3 = argparse.ArgumentParser()
parser3.add_argument("--verbose", action="store_true")
parser3.add_argument("--quiet", action="store_false")

# MULTIPLE VALUES (nargs)
# python 09_cmd_arguments.py --values 10 20 30 40

parser4 = argparse.ArgumentParser()
parser4.add_argument("--values", nargs="+", type=int, default=[1, 2, 3])

# REQUIRED & POSITIONAL
# python 09_cmd_arguments.py data.txt --output result.txt --count 5

parser5 = argparse.ArgumentParser()
parser5.add_argument("input_file")                  # positional, required
parser5.add_argument("--output", required=True)     # named, required
parser5.add_argument("--count", type=int, default=1)

# CHOICES (restrict values)
# python 09_cmd_arguments.py --mode prod

parser6 = argparse.ArgumentParser()
parser6.add_argument("--mode", choices=["dev", "prod", "test"], default="dev")

# HELP MESSAGE (argparse auto-generates help from descriptions and defaults)
# python 09_cmd_arguments.py --help

parser7 = argparse.ArgumentParser(description="File processor")
parser7.add_argument("--input", help="input file path")
parser7.add_argument("--lines", type=int, help="number of lines to read")