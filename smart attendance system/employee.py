# database of the employee as dictonary
#add number of employee as many inside the dictonary
employee_dict = {"SBC123461":"Carter","SBC1234601":"Harry","SBC1234602":"Jack","SBC1234603":"Oliver","SBC1234604":"Leo"}# make dictonary of the employee
def search(dec):
            if dec in employee_dict:#check the barcode is in dictonary, if it is present go to inside if statement 
                a = employee_dict[dec]#extract name from barcode using this line
                print(a)

                file=open('data.txt',"r")#open the file in read the file
                file_read = file.read()
                if a in file_read:#check name is present in data.txt file
                    return "already present"
                else:#if the name is not present in data.txt file then append the name in the file(to avoid the duplication)
                    file=open('data.txt',"a+")
                    file.write(a)
                    file.write('\r')#append next line to file
                    file.close()
                    return a
            else:#if barcode is not in dictonary then return False
                return False#return False
            
