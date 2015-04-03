import json
from json2html import *
import subprocess


def setup():
    data = build_json()
    table = generate_table(data)
    generate_html_page(table)


def build_json():
    json = {}
    cmd = "dpkg -l | awk '{print $2, \"\t\", $3}'"
    output = subprocess.check_output(cmd, shell=True)
    lineiterator = iter(output.splitlines())
    for line in lineiterator:
        kvp = line.split(" ")
        json[kvp[0]] = kvp[2]
    return json


def generate_table(data):
    table = json2html.convert(json=json.dumps(data, sort_keys=True))
    return table


def generate_html_page(table):
    html_file = open('sysview.html', 'w+')
    html_file.write(table)
    html_file.close()

if __name__ == '__main__':
    setup()
