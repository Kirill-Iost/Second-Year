import argparse


def read_file(path_to_file, line=None):
    with open(path_to_file, mode="r") as f:
        return list(map(str.strip, f.readlines()[:line]))


def write_file(path_to_file, upper=False, *data):
    data = list(map(str.upper, data)) if upper else data
    with open(path_to_file, mode="w") as f:
        f.write("\n".join(data))


parser = argparse.ArgumentParser()
parser.add_argument("--upper", action="store_true")
parser.add_argument("--lines", type=int)
parser.add_argument("read_file", type=str)
parser.add_argument("write_file", type=str)
args = parser.parse_args()
data = read_file(args.read_file, args.lines)
write_file(args.write_file, args.upper, *data)
