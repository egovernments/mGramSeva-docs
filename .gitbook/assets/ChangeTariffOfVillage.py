import base64
import requests
import csv
import openpyxl
import json


updatedFile = openpyxl.load_workbook("/home/admin1/Documents/eGov/Script/06 Nov - Master Rate.xlsx")
sheet = updatedFile.active
localFilePath="/home/admin1/Documents/Github/"
col = csv.writer(open("new_updated_file4.csv",'w',))
fields = ['VillageName', 'newTariff', 'OldTariff', 'Success', 'fileExist'] 
for row in sheet.rows:
    uniqueVillageName=row[2].value
    oldminimumCharge=row[7].value
    newminimumCharge=row[8].value
    uniqueVillageName = str(uniqueVillageName)  
    uniqueVillageName=uniqueVillageName.replace(" ", "") 
    uniqueVillageName=uniqueVillageName.replace("/","") 
    if((str(uniqueVillageName) != 'UniqueVillageName') and (str(uniqueVillageName) != '17')): 
        print(localFilePath + "uniqueVillageName:"+str(uniqueVillageName)+ " oldminimumCharge:"+ str(oldminimumCharge) + " newminimumCharge" + str(newminimumCharge))
        try:
            f = open(localFilePath + 'mdms-mgramseva/data/pb/'+str(uniqueVillageName)+'/ws-services-calculation/WCBillingSlab.json','r')
            # print("file location"+f.toString())
            data=json.load(f)
            for i in data['WCBillingSlab']: 
                if ((i['buildingType'] == 'RESIDENTIAL') and (i['connectionType']=='Non_Metered') and (i['calculationAttribute'] == 'Flat')): 
                    if(i['minimumCharge'] == oldminimumCharge): 
                        print(i['minimumCharge'])
                        i['minimumCharge'] =   newminimumCharge 
                        f.close()
                        print(data)
                        with open(localFilePath + 'mdms-mgramseva/data/pb/'+str(uniqueVillageName).lower()+'/ws-services-calculation/WCBillingSlab.json', "w") as jsonFile:
                            json.dump(data, jsonFile, indent = 4)   
                        r= ['VillageName:'+str(uniqueVillageName)+',Oldtariff:'+str(oldminimumCharge)+',NewTariff:'+str(newminimumCharge) +',Success: DONE,fileExist:YES;' ]
                        line=r      
                        col.writerow(line)    
                    else:
                        print("Didn't match")   
                        r= ['VillageName:'+str(uniqueVillageName)+',Oldtariff:'+str(oldminimumCharge)+',NewTariff:'+str(newminimumCharge) +',Success: NOT DONE!Old Tariff didnotMatch,fileExist:YES;']
                        line=r  
                        col.writerow(line)      
                f.close()   
        except FileNotFoundError:
            print("file not found for village:" + str(uniqueVillageName))  
            r=['VillageName:'+str(uniqueVillageName)+',Oldtariff:'+str(oldminimumCharge)+',NewTariff:'+str(newminimumCharge) +',Success: NOT DONE,fileExist:NO;']
            line=r  
            col.writerow(line)     