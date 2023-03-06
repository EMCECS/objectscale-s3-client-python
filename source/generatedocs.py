import os
import json
from docutils.core import publish_parts

def generate_docs():
    if not os.path.exists('reference'):
        os.makedirs('reference')


    with open('../src/main/python/service-2.sdk-extras.json', 'r') as f:
        data = json.load(f)

    # rst = publish_parts(json.dumps(data['merge']['operations']), writer_name="rst")['body']
    
    def bullet_list(elements, level=0, indent_size=4):
        try:
            items = elements.items()
        except AttributeError:
            for bullet_point in elements:
                yield '{}* {}'.format(' ' * (indent_size * level), bullet_point)
        else:
            for bullet_point, sub_points in items:
                yield '{}* {}'.format(' ' * (indent_size * level), bullet_point)
                yield from bullet_list(sub_points, level=level + 1, indent_size=indent_size)
    
    
    
    

    with open('reference/output.rst', 'w') as f:
        for line in bullet_list(data['merge']['operations']):
            f.write(line)

generate_docs()