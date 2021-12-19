import xml.etree.ElementTree as ET

ns = {
    'wp': 'http://wordpress.org/export/1.2/',
}

ET.register_namespace('wp', ns['wp'])

files = {
    "posts": ET.parse('posts/posts.xml'),
    "media": ET.parse('posts/media.xml'),
    "testimonials": ET.parse('posts/testimonials.xml'),
    "faqs": ET.parse('posts/faqs.xml'),
}

ids = {
    "media": [3626, 3623, 3622, 3612, 3611, 3610, 3609, 3608, 3607, 3606, 3389, 3388, 3387, 3386, 3385]
}

roots = {}
channels = {}

for name, file in files.items():
    roots[name] = file.getroot()
    channels[name] = roots[name].find('channel')

for item in channels["media"].findall('item'):
    id = item.find("wp:post_id", ns)

    if(int(id.text) in ids["media"]):
        channels["posts"].append(item)
    else:
        channels["media"].remove(item)

for item in channels["testimonials"].findall('item'):
    channels["posts"].append(item)

for item in channels["faqs"].findall('item'):
    channels["posts"].append(item)

files["posts"].write('posts-testimonials-faqs.xml')
files["media"].write('posts/media.xml')
