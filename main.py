#writing a  new file
employe_data=open("employee1.txt","w")
employe_data.write("\n how are you \n where are you ")
employe_data.close()
#reading all lines in file
employe_data=open("employee1.txt","r")
print(employe_data.readlines())
employe_data.close()
#editing file
employe_data=open("employee1.txt","a")
employe_data.write(" \nlast line")
employe_data.close()
#reading all file
employe_data=open("employee1.txt","r")
print(employe_data.readlines(1))#reading line number  1
employe_data.close()