# -*- coding:UTF-8 -*-
import pickle

# The name of the file where we will store the object
shoplistfile = 'shoplist.data'
# The list of whings to buy
shoplist = ['apple', 'mango', 'carrot']

# Write to the file
f = open(shoplistfile, 'wb')
# Dump the object to a file
pickle.dump(shoplist, f)
f.close()

# Destroy the shoplist variable
del shoplist
# Read back from the storagef
f = open(shoplistfile, 'rb')
# load the object from the file
storedlist = pickle.load(f)
print(storedlist)
f.close()