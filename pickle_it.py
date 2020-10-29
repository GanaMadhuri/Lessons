# Pickle It
# Demonstrates pickling and shelving data

import pickle, shelve

print("Pickling lists.")
variety = ["sweet", "hot", "dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]
text = ["alexa","cortazona","siri","sophia"]
numbers = [100.00,200.00,300.23,400.34]
f = open("pickles1.dat", "wb")
pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
pickle.dump(text, f)
pickle.dump(numbers, f)
f.close()

print("\nUnpickling lists.")
f = open("pickles1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)
text =  pickle.load(f)
numbers = pickle.load(f)
print(variety)
print(shape)
print(brand)
print(text)
print(numbers)
f.close()

print("\nShelving lists.")
s = shelve.open("pickles2.dat")
s["variety"] = ["sweet", "hot", "dill"]
s["shape"] = ["whole", "spear", "chip"]
s["brand"] = ["Claussen", "Heinz", "Vlassic"]
s["text"] = ["alexa","cortazona","siri","sophia"]
s.sync()    # make sure data is written

print("\nRetrieving lists from a shelved file:")
print("text -", s["text"])
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()

input("\n\nPress the enter key to exit.")
