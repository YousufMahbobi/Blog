import json
import os

def read_json():
    with open(os.path.join(os.path.dirname(__file__), 'blog_data.json'), 'r') as f:
        return json.loads(f.read())


