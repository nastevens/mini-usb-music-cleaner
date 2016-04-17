# MINI USB Music Cleaner
#
# TODO: Insert license

import os
import sys

from mutagen.id3 import ID3, APIC
from os.path import join

def save_image_tag(mp3, image):
    """Adds the data in `image` to the `mp3`"""
    print mp3.filename, 'added image'
    mp3.delall(u'APIC')
    mp3.add(APIC(mime=u'image/jpeg', type=3, desc=u'None', data=image))
    mp3.save(v2_version=3)


def has_image_tag(id3):
    """Returns true if the ID3 info contains an image tag"""
    return bool(id3.getall(u'APIC'))


def main():
    for root, _, files in os.walk(sys.argv[1], topdown=False):
        if 'folder.jpg' not in files:
            continue

        with open(os.path.join(root, 'folder.jpg'), 'r') as image:
            cover = image.read()

        for f in files:
            if not f.endswith('.mp3'):
                continue
            mp3 = ID3(os.path.join(root, f))
            save_image_tag(mp3, cover)


if __name__ == '__main__':
    sys.exit(main())

