r = ["1","2", "3"]
l = [ 1, 'two', 3, {'4': 'four' }, 5 ]
t = ( 'one', 'two', None, 'four', 'five' )
s = set("It's a bird! It's a plane! It's Superman!")
d = dict( one = r, two = l, three = s )
if   isinstance(r, list):  print(r)
elif isinstance(l, range): print(l)
elif isinstance(t, tuple): print(t)
elif isinstance(s, set):   print(s)
elif isinstance(d, dict):  print(d)
#elif o is None: print('Nada', end=' ', flush=True)
else: print(repr(s), end=' ', flush=True)


print(repr(t))