import pprint
cats = [{'name' : 'Yuki', 'desc ' : 'the most beautiful'}, {'name': 'Kumo', 'desc' : 'the escaper'}]
print(pprint.pformat(cats))
file_obj = open('my_cats.py', "w")
file_obj.write('cats =' + pprint.pformat(cats) + '\n')
file_obj.close()

#my_cats can be open in vc