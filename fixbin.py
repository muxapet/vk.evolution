#!/usr/bin/python

import zipfile
import os
from os.path import basename
import sys

filename = "./HumanEvolutionCorona.bin"
if len(sys.argv) > 1:
    filename = sys.argv[1]

shortname = basename(filename).replace(".bin", "")
innername = "coronaHtml5App"

with zipfile.ZipFile(filename) as temp:
    with temp.open('{0}.js'.format(innername)) as myfile:
        newfile = myfile.read().decode('UTF-8')
        newfile = newfile.replace('window.innerHeight', 'getActualHeight()').replace('window.innerWidth', 'getActualWidth()')

    with zipfile.ZipFile('{0}.new'.format(filename), 'w', compression=zipfile.ZIP_DEFLATED) as zipFile:
        zipFile.writestr('{0}.js'.format(innername), newfile)
        zipFile.writestr('{0}.html.mem'.format(innername), temp.open('{0}.html.mem'.format(innername)).read())

bakFile = '{0}.bak'.format(filename)
counter = 1
while os.path.isfile(bakFile):
    bakFile = '{0}.{1}.bak'.format(filename, counter)
    counter += 1

os.rename(filename, bakFile)
os.rename('{0}.new'.format(filename), filename)