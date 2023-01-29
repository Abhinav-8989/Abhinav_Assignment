# Access the nested key ‘salary’ from the following JSON

import json

f=open("sample.json")
val= json.load(f)

   
print("company1 employee salary: ", val["company1"]["employee"]["payble"])
      