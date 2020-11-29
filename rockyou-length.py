f_in = open("rockyou.txt","r")
flines = f_in.readlines()
f_out = open("rockyou-length.csv","a")

for i in range(1,287): # 286 characters is the longest password in rockyou.txt
    counter=0

    for fline in flines:
        if len(fline) == i:
            counter = counter + 1
    
    f_out.write(str(i-1) + "," + str(counter))
    f_out.write("\n")

f_in.close()
f_out.close()
print ("DONE")