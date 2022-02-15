import csv
from redis_protocol import generate_redis_protocol

columns = ["frameId", "env", "mo", "format", "lat", "lon", "type", "geoid", "city", "statecode", "state", "statelat", "statelon"]

def to_redis_proto(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            frame_id = row[0]
            for i, field_name in enumerate(columns):
                field_value = row[i]
                print(generate_redis_protocol('HSET', "9"+frame_id[1:], field_name, field_value), end="")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, required=True)
    args = parser.parse_args()

    filename = args.filename

    to_redis_proto(filename)
