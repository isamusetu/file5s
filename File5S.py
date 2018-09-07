import os
import time
import shutil
import datetime
    
def recu(orgpath, tarpath):
        
    if not os.path.exists(tarpath):
        os.mkdir(tarpath)    
        
    nodeinspecifiedfolder = os.listdir(orgpath)
        
    for node in nodeinspecifiedfolder:
        filenameorpath = os.path.join(orgpath,node)
        
        if os.path.isdir(filenameorpath):
            recu(filenameorpath, tarpath)
        elif os.path.isfile(filenameorpath):
            
            YM = findYMfromfilename(filenameorpath)
            
            if YM is None:                
                YM = getcreatedatefromfileproperty(filenameorpath)                

            filenamewithpath = filenameorpath
            filename = node

            global count
            copyfile(filename, filenamewithpath, tarpath, YM, count)
            count +=1
        
def getcreatedatefromfileproperty(filename):
    date = time.localtime(os.stat(filename).st_ctime)
    year = time.strftime("%Y", date)
    month = time.strftime("%m", date)
    
    return year + month
            
def copyfile(orgfilename,orgfilenamewithpath,tarpath,YM,count):
    tarpath = tarpath + "\\"+ YM
    newfilenamewithpath = tarpath +"\\" + orgfilename
    
    if not os.path.isdir(tarpath):
        os.mkdir(tarpath)

    
    starttime = time.clock()
    shutil.copyfile(orgfilenamewithpath, newfilenamewithpath)
    endtime = time.clock()

    costtime = endtime - starttime

    strInfo = "("+ str(count) +")"
    strInfo = strInfo + "File is copying from (" + orgfilenamewithpath + ") to (" + newfilenamewithpath + ")"
    strInfo = strInfo + "%f"%(costtime*1000) + "ms"
    print (strInfo)

def findYMfromfilename(filename):
    #find the filename whether contains a substring like 20XXXX
    npos = 0

    for c in filename:
        if c == "2":    
            str = filename[npos:npos+6]
            try:            
                dateconvertfromstring = time.strptime(str, "%Y%m")            
                YMconvertfromdate = time.strftime("%Y%m",dateconvertfromstring)
                
                return YMconvertfromdate
            except:
                YMconvertfromdate = None
        npos +=1
    

print ("===========================================================")
print ("Group and categorize the file depends on the Year and month")
print ("===========================================================")

orgpath = input("Please input the orginal path:")
tarpath = orgpath + ("_After")
print ("The result which grouped and categorized by this tool would be saved under:" + tarpath)
print("The recu is processing.")
count = 0    
recu(orgpath, tarpath)
print("The recu process is end.")


