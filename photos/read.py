from os import walk
mypath = '/Users/elizabethlin/Downloads/instagram.css-master/photos'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    print(f)
    print(filenames)
    break

















