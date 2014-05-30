import foursquare
import os
import json

# import credentials from extra file:
from credentials import USER_TOKEN


def write_to_file(item):
    fn = item.get('id') + ".json"
    with open(os.path.join("backup", fn), "w") as fp:
        fp.write(json.dumps(item))
    return fn


def main():

    if not USER_TOKEN or len(USER_TOKEN) == 0:
        raise ValueError, "invalid USER_TOKEN?"

    client = foursquare.Foursquare(access_token=USER_TOKEN)

    for item in client.users.all_checkins():
        print(write_to_file(item))


if __name__ == '__main__':
    main()
