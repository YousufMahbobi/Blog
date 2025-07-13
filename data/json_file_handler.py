import json
import os

def read_json():
    with open(os.path.join(os.path.dirname(__file__), 'blog_data.json'), 'r') as f:
        return json.loads(f.read())


def write_json(data):
    json_data = json.dumps(data)
    with open(os.path.join(os.path.dirname(__file__), 'blog_data.json'), "w") as fileobj:
        fileobj.write(json_data)