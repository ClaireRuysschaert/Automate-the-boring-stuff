#json module 
# only have these data type : str, int, floats, bool, list, dict and Nonetype

import json

#reading : loads()
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)

#writing : dumps() = dump string
#python value into str of json 


