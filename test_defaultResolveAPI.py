import imp
import sys
import os

print('Python version:', sys.version)
print('Sys path:', sys.path)

print("1. Try to load simple file as string")
stream = open('./data.txt', 'r')
print('    data.txt:', stream.read())
print('---')

print('Import fusionscript.so')
script_module = imp.load_dynamic("fusionscript", "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Libraries/Fusion/" + "fusionscript.so")
print('Done.')

print("2. Try to load simple file as string AGAIN")
stream = open('./data.txt', 'r')
print('    data.txt:', stream.read())
print('---')

print("Establish a Resolve() object.")
Resolve = script_module.scriptapp('Resolve')
print('Done.')

print("3. Try to load simple file as string AGAIN")
stream = open('./data.txt', 'r')
print('    data.txt:', stream.read())
print('---')