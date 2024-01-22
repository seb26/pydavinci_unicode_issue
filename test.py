print("Begin: ✅ Emoji on stdout")
print('---')

print("Try to load simple file as string")
stream = open('./data.txt', 'r')
print('    data.txt:', stream.read())
print('---')

print('Try to load YAML file with emojis')
import yaml
stream = open('./data.yml', 'r')
print( yaml.safe_load(stream) )
print('---')

print('Try to import pydavinci')
import pydavinci
print('Imported pydavinci.')
if hasattr(pydavinci, '__version__'):
	print('Pydavinci version:', pydavinci.__version__)
print("✅ Emoji after pydavinci import")
print('---')

print('Try to create a Resolve object/contact API')
Resolve = pydavinci.davinci.Resolve()
print(Resolve)
print("✅ Emoji after printing Resolve obj")
print('---')

print("Try to load simple file as string")
stream = open('./data.txt', 'r')
print('data.txt:', stream.read())
print("✅ Emoji after reading back a file")
print('---')

print('Try to load emojis again...')
stream = open('./data.yml', 'r')
print( yaml.safe_load(stream) )
print("✅ Emoji after safe loading yaml file")
print('---')

