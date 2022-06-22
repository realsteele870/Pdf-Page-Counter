#@Author Remington Steele
#a program to count the number of pages in a pdf file in a folder and
#output to a text file when the page threshold is reached
from PyPDF2 import  PdfFileReader
import os
#gets the directory that the executable lives in 
directory = os.getcwd()
limit =3000
total=0
file1 = open("output.txt","w")
#used to sort the list of files by the first 5 numbers in the claims file
def numbers(lists):
    return lists[0:5]
#if it is a VVA file uses the last couple digits to sort the files
def VVA(x):
    i=9
    integerString=''
    
    while(x[i].isdigit()):
        integerString+=x[i]
        i+=1
    print("int string: "+integerString)
    toInt=int(integerString)
    return(toInt)
sortedList = os.listdir(directory)
print(sortedList)
r =0
while( r < len(sortedList)):
    print("checking: "+sortedList[r])
    if (not (sortedList[r].endswith(".pdf"))) or sortedList[r].endswith(".exe"):
        print("popped: "+sortedList[r])
        sortedList.pop(r)
    r=r+1
#print(sortedList[1].startswith("VVA",0,3))
sortedList.pop(0)
if sortedList[0].startswith("VVA",0,3):
    print("poo")
   
    
       
    newsortedList= sorted(sortedList,key=VVA)
else:
    newsortedList= sorted(sortedList,key=numbers)


#goes through the claims file pds and prints out to output.txt whenever the number value
#exceeds 3000 
for filename in newsortedList:
    
    if filename.endswith(".pdf"):
        print("on file: "+filename)
        pdf= PdfFileReader(filename,'rb')
        pages = pdf.getNumPages()
        if(total+pages>limit):
            file1.write("ends: "+filename+" with "+ str(total)+" pages\n\n")
            total=pdf.getNumPages()
        else:
            total=total+pages

file1.close()
