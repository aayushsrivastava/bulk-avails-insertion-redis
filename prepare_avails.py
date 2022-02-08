import csv

from redis_protocol import generate_redis_protocol


DIGITAL_COLUMNS = ["frame_id", "date_hour", "a", "b", "c"]

def map_digital(row):
    frame_id = row[0]
    date_hour = row[1]
    avails = {
        "available": row[2],
        "reserved": row[3],
        "not_available": row[4],
    }

    key = frame_id + "_" + date_hour
    value = str(avails)
    return key, value

def map_classic(row):
    frame_id = row[0]
    date = row[1]
    avails = row[2]

    key = frame_id + "_" + date
    value = avails
    return key, value

def to_redis_proto(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 5: # is digital avails data
                key, value = map_digital(row)
            else:
                key, value = map_classic(row)

            print(generate_redis_protocol('SET', key, value), end="")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", type=str, required=True)
    args = parser.parse_args()

    filename = args.filename

    to_redis_proto(filename)
