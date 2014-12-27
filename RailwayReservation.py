
    
    
# interactive reservation
import shelve
from Person import Person

#All Trains List.Add below in List to incorporate new trains.

lTrList =  {   '2017': { 'name' : 'DEHRADUN SHTBDI','orig' : 'New Delhi', 'dep' : '7:00', 'dest' : 'Dehradun', 'arr' : '12:40' },
               '2018': { 'name' : 'DEHRADUN SHTBDI','orig' : 'Dehradun' , 'dep' : '17:00', 'dest' : 'New Delhi','arr' : '22:40'},
               '3009': { 'name' : 'DOON EXPRESS','orig' : 'Howrah Jn' , 'dep' : '19:15', 'dest' : 'Dehradun','arr' : '06:45'},
               '3010': { 'name' : 'DOON EXPRESS','orig' : 'Dehradun' , 'dep' : '20:20', 'dest' : 'Howrah Jn','arr' : '07:00'},
               '3013': { 'name' : 'UPASANA EXPRESS','orig' : 'Howrah Jn' , 'dep' : '13:10', 'dest' : 'Dehradun','arr' : '19:00'},
               '3014': { 'name' : 'UPASANA EXPRESS','orig' : 'Dehradun' , 'dep' : '09:05', 'dest' : 'Howrah Jn','arr' : '15:00'}
           }
			  




fieldnames = ('Name', 'Age','Gender','Address','PhNo','TrID','PNR') 
maxfield = max(len(f) for f in fieldnames)

print('\n\nWelcome to INDIAN Railway Reservation System \n')
print('\n\nPlease select Train Number from following All Trains List :\n\n')

for train in lTrList:
		print('Train No. :[',train, '] =>', lTrList[train]['name'],'| Origin =>', lTrList[train]['orig'],'| Departure =>', lTrList[train]['dep'],'| Destination =>', lTrList[train]['dest'],'| Arrival =>', lTrList[train]['arr'],'|')
prompt = "\n   1.New Reservation        2.Query Reservation by PNR     3.Update Reservation by PNR       4.Cancellation by PNR    5.Exit\n\n\n     Enter your choice : "
NUC = input(prompt)
if NUC == "1":
		db = shelve.open('rail-reserve-shelve')
		while True:
			trid = input('\nEnter Train ID :')
			if not trid: break
			name = input('\nEnter Name :')
			age =  input('\nEnter Age  :')
			gender = input('\nEnter Gender :')
			addr = input('\nEnter Address :')
			phno = input('\nEnter Phone No. :')
			record = Person(Name=name, Age=age,Gender=gender,Address=addr,PhNo=phno,TrID=trid) # eval: quote strings
			db[record.PNR] = record
			print ("\n\nReservation Done.Please note your PNR :",record.PNR);
		db.close()
elif NUC == "2":
		db = shelve.open('rail-reserve-shelve')
		while True:
			PNR = input('\nEnter PNR No. to Search :')
			if not PNR: break
			try:
				record = db[PNR]
			except:
				print('\nNo such PNR exists. :"%s"!' % PNR)
			else:
				for field in fieldnames:
					print(field.ljust(maxfield), '=>', getattr(record, field))
		db.close()
elif NUC == "3":
		db = shelve.open('rail-reserve-shelve')
		while True:
			PNR = input('\nEnter PNR No to Update Reservation Details :')
			if not PNR: break
			if PNR in db:
				record = db[PNR]
			else:
				print('No such PNR exists. "%s"!' % PNR)
				break
			for field in fieldnames:
				if field != 'PNR':
					#print('Field :%s' % field)
					currval = getattr(record, field)
					newtext = input('\t[%s]=%s\n\t\tNew?=>' % (field, currval))
					if newtext:
						setattr(record, field, eval(newtext))
			db[PNR] = record
		db.close()
elif NUC == "4":
		db = shelve.open('rail-reserve-shelve')
		while True:
			PNR = input('\nEnter PNR No to Cancel Reservation Details :')
			if not PNR: break
			if PNR in db:
				record = db[PNR]
			else:
				print('No such PNR exists. "%s"!' % PNR)
				break
			del db[PNR]
		db.close()
elif NUC == "5":
		print ("\n\nThank you for choosing INDIAN RAILWAYS.\n\nAapki YATRA Mangalmaaye Ho");
		pass

