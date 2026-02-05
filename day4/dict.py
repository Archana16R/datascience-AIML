# creating dictionary and perform their methods

dict={"id":"105",
      "name":"Acchu",
      "Course":"MCA",
      "sem":"4"}
print(dict)           
#methods
#keys()
print(dict.keys())    
#values()
print(dict.values())   
#items()
print(dict.items())
#get()
print(dict.get("name"))
#update
dict["name"]="Archana"
print(dict)
#pop
dict.pop("sem")
print(dict)
#clear
#dict.clear()
#print(dict)
#loop
for k,v in dict.items():
    print(k,":", v)