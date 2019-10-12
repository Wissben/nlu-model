import re
import random

OBJECT = 'objects.txt'
COLORS = 'colors.txt'
SIZES = 'sizes.txt'


def load_objects(path):
    return [f[:-1] for f in open(path,'r').readlines()]

