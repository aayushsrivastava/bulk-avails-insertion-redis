import csv
from redis_protocol import generate_redis_protocol

columns = ["frame_id", "environment", "media_owner", "format", "lat", "long", "inventory_type", "key1", "key2", "state_code", "state", "lat2", "long2"]

def to_redis_proto(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            frame_id = row[0]
            for i, field_name in enumerate(columns):
                field_value = row[i]
                print(generate_redis_protocol('HSET', frame_id, field_name, field_value), end="")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, required=True)
    args = parser.parse_args()

    filename = args.filename

    to_redis_proto(filename)
