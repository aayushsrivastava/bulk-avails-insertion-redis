from prepare_frames import to_redis_proto


if __name__ == "__main__":
    import argparse
    import glob
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d", type=str, required=True)
    args = parser.parse_args()

    path = args.directory

    for filepath in glob.glob(path + "/*.csv"):
        to_redis_proto(filepath)
