import shelve
shelf_file = shelve.open('mydata')
cats = ['Yuki', 'Kumo']
shelf_file['cats'] = cats
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()