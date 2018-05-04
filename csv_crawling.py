#import csv module to read "csv" libraries, import sys to read "sys" libraries so that error messages can be interpreted

import csv
import sys
import re
#open files using with statement
with open(r'D:\0- Upskill\3- Python\Switches and Hubs Mar 15, 2018 1.09.35 PM.csv',newline='') as fr, open(r'D:\0- Upskill\3- Python\output7.csv','w',newline='') as fw:
	reader = csv.DictReader(fr)
	fieldnames = ['Original Device Name', 'IP Address', 'New Device Name', 'Target']
	writer = csv.DictWriter(fw, fieldnames=fieldnames)
	writer.writeheader()
	try:
		for row in reader:
			devName = row['Device Name']
			ipAddr = row['IP Address']
			if devName.startswith(('G','g','sv','SV','sV','Sv','BH','bh','bH','Bh','CH','ch','cH','Ch')) and not re.findall('UNREACHABLE', row['Reachability'],re.IGNORECASE): 
				print(devName, ipAddr)
				if re.findall('p-', devName,re.IGNORECASE):
					devNameSub = devName[devName.find('-')+1:devName.rfind('-')]
					devNameNew = devName.replace(devNameSub, "cat9300p")
				else:
					devNameSub = devName[devName.find('-')+1:devName.rfind('-')]
					devNameNew = devName.replace(devNameSub, "cat9300t")
				target = devName + '    '+ ipAddr +'-->  ' + devNameNew
				writer.writerow({'Original Device Name': devName, 'IP Address': ipAddr, 'New Device Name': devNameNew, 'Target':target})
	except csv.Error as e:
		sys.exit('file {}, line {}: {}'.format(fr, reader.line_num, e))
		sys.exit('file {}, line {}: {}'.format(fw, reader.line_num, e))
