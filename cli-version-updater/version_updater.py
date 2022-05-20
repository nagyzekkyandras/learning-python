#!/usr/bin/python3
import argparse
import sys
import os
# file import
import version_update_hepler as version

conigFile='version_update_hepler.py'
versionTag=""

if not os.path.exists(conigFile):
    print(conigFile + ' config file not exists')
    sys.exit(os.EX_OSFILE)

def major():
    changeVersionFromFile(0)
    sys.exit(os.EX_OK)

def minor():
    changeVersionFromFile(1)
    sys.exit(os.EX_OK)

def patch():
    changeVersionFromFile(2)
    sys.exit(os.EX_OK)

def changeVersionFromFile(changeoktet: int):
    with open(version.file, "r", encoding="utf-8") as f: # read
        for l in f:
            l = l.strip()
            if "version:" in l:
                v=l.split(" ")
                versionTag=v[1]
                old=versionTag
                for i in range(0, 3):
                    oktet=versionTag.split(".")
                    oktet[changeoktet]=int(oktet[changeoktet])+1
                    new=str(oktet[0])+"."+str(oktet[1])+"."+str(oktet[2])
        f.close()
    print("old: "+old) # for debug
    print("new: "+new) # for debug

    with open(version.file) as f:
        newText=f.read().replace(old, new)
    
    with open(version.file, "w") as f:
        f.write(newText)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

parser_major = subparsers.add_parser('major', help='major')
parser_major.set_defaults(func=major)

parser_minor = subparsers.add_parser('minor', help='minor')
parser_minor.set_defaults(func=minor)

parser_patch = subparsers.add_parser('patch', help='patch')
parser_patch.set_defaults(func=patch)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()

options.func()

# links:
# https://stackoverflow.com/questions/27529610/call-function-based-on-argparse
# https://www.delftstack.com/howto/python/python-import-variable-from-another-file/
# https://careerkarma.com/blog/python-check-if-file-exists/
# https://stackoverflow.com/questions/285289/exit-codes-in-python
# https://stackabuse.com/python-check-if-string-contains-substring/
# https://stackoverflow.com/questions/2489669/how-do-python-functions-handle-the-types-of-the-parameters-that-you-pass-in
# https://www.guru99.com/reading-and-writing-files-in-python.html