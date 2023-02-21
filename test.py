import argparse
import requests
import csv

parser = argparse.ArgumentParser()
parser.add_argument("host",  type=str)
parser.add_argument("port", type=str)
parser.add_argument("key", type=str)
parser.add_argument("--smaller ", nargs="", default=3, type=int)
parser.add_argument("--accuracy  ", nargs="1", default=1, type=int)
args = parser.parse_args()

print(args.smaller)

url = f'{args.host}:{args.port}'
response = {
    "1_turn": {
        "x": [
            127,
            17,
            93,
            108,
            73
        ],
        "y": [
            139,
            3,
            91,
            98,
            70
        ],
        "z": [
            33,
            50,
            97,
            17,
            21
        ],
        "t": [
            1,
            2,
            3,
            4,
            5
        ]
    },
    "2_turn": {
        "x": [
            79,
            3,
            116,
            65,
            107
        ],
        "y": [
            72,
            131,
            112,
            92,
            149
        ],
        "z": [
            27,
            63,
            93,
            100,
            6
        ],
        "t": [
            1,
            2,
            3,
            4,
            5
        ]
    }
}

with open("orbit_deviation.csv", mode="w") as f:
    writer = csv.writer(f)
    for i in response[args.key]["t"]:
        res = [i]
        value = []
        for j in response[args.key].keys():
            if response[args.key][j][i] >= args.smaller:
                value.append(response[args.key][j][i])
        res.extend([list(response[args.key].keys())[value.index(max(value))], max(value)])
        res.extend([list(response[args.key].keys())[value.index(min(value))], min(value)])
        res.append(round(((response[args.key]["x"]["t"] ** 2 + response[args.key]["y"]["t"] ** 2 + response[args.key]["z"]["t"] ** 2) ** (1/2)), args.accuracy))
        writer.writerow(res)



