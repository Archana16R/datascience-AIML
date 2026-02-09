#file = open("example.txt","r")
#print(file.read())
#print(file.readlines())
#file.close()

#file=open("example1.txt","w")
#file.write("hello era")
#file.close()

#file=open("example1.txt","a")
#file.write("welcome to AIML internship")
#file.close()

#with open(r"C:\Users\archana\Downloads\HAND.jpg","rb") as f:
    #image=f.read()
   # print(image)
   
#try:
   #file=open("sample.txt","r")
   #print(file.read())
   
#except FileNotFoundError:
    #print("File not found, pls open existing file")
#finally:
    #file.close()
    
#try:
   #file=open("sample.txt","r")
   #print(file.read())
   
#except Exception as e:
    #print(f"Error: {e}")
#finally:
    #file.close()
    
try:
   file=open("example1.txt","r")
   print(file.read())
   
except FileNotFoundError:
    print("File not found, pls open existing file")
finally:
    file.close()