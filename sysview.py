import json
import re
import subprocess


def setup():
    data = build_json()
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))


def build_json():
    json = {}
    cmd = "dpkg -l | awk '{print $2, \"\t\", $3}'"
    output = subprocess.check_output(cmd, shell=True)
    lineiterator = iter(output.splitlines())
    for line in lineiterator:
        kvp = line.split(" ")
        json[kvp[0]] = kvp[2]
    return json

if __name__ == '__main__':
    setup()
