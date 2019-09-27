#!/usr/bin/python3
import os
import sys
import textract
from wand.image import Image as Img
import json
import re
from datetime import datetime
import shutil
import socket
import time

print("script Initialized")
time.sleep(2)
def extract(pdffile):
	hostname = socket.gethostname()
	try:
		print("creating script files")
		time.sleep(2)
		os.mkdir("images")
		time.sleep(2)
	except FileExistsError:
		pass
	except:
		sys.exit("Permission denied: User {} has no privilages to create files".format(hostname))
	print("reading {}".format(pdffile))
	with Img(filename=pdffile, resolution=300) as img:
	    img.compression_quality = 99
	    img.save(filename='images/image_name.jpg')
	alljson = []
	jdondata = {"Billed by":[{"Name": "", "Address":"", "Vat No":"", "Tel No":""}], "Billed To":[{"Address":"", "Account No":"", "Name":""}], "Invoice":[{"Billed Items":"", "Date Invoiced":"", "Invoice Total":"", "Vat Percentage":""}]}

	print("extracting text from {}".format(pdffile))
	for image in os.listdir("images"):
		with open(image+".txt", "w") as f:
			text = textract.process("images/"+image, encoding='ascii', method='tesseract')
			text = text.decode('utf-8')
			f.write(text)
			f.close()
		with open(image+".txt", "r") as f2:
			text = f2.read()

		jdondata = {"Billed by":[{"Name": "", "Address":"", "Vat No":"", "Tel No":""}], "Billed To":[{"Address":"", "Account No":"", "Name":""}], "Invoice":[{"Billed Items":"", "Date Invoiced":"", "Invoice Total":"", "Vat Percentage":""}]}
		for i in text.split("\n"):
			try:
				#print(i)
				if "@" in i:
					jdondata["Billed by"][0]["Name"] = (i.split()[0])
					jdondata["Billed by"][0]["Address"] = (i.split()[1])
				if "Vat No" in i:
					jdondata["Billed by"][0]["Vat No"] = (i.split()[2])
				if "Tel No" in i:
					jdondata["Billed by"][0]["Tel No"] = (i.split(":")[-1].strip())
				if "Billed To" in i:
					jdondata["Billed To"][0]["Account No"] = (i.split()[2])
				if "Client Name" in i:
					jdondata["Billed To"][0]["Name"] = " ".join(i.split()[2:-2])
				#if "Street Address" in i:
					#pass#print(i)
					#jdondata["Billed To"][0]["Address"] = (i.split()[2])
				if "Total" in i and len(i.split()) == 2:
					jdondata["Invoice"][0]["Invoice Total"] = (i.split()[-1])
				if "Tax" in i:
					jdondata["Invoice"][0]["Vat Percentage"] = (i.split()[-1])
					
					#print(i.split())
				jdondata["Invoice"][0]["Date Invoiced"] = str(datetime.strptime(i,("%d/%m/%Y"))).split()[0]

				#print(i)
			except IndexError:
				pass
			except ValueError:
				pass


		#result = re.search('Description;(.*)Subtotal', text)
		#print(result)
		billedstring=text[text.find("Description")+len("Subtotal"):text.find("Subtotal")]
		billedstringlist = (billedstring.split("\n")[1:])
		billeditems = []
		for item in billedstringlist:
			if item != '':
				billeditems.append(" ".join(item.split()[:-3]))

		streetstring=text[text.find("Street Address")+len("Date Of Issue"):text.find("Date Of Issue")]
		streetstring = (streetstring.split("\n")[-1])
		jdondata["Billed To"][0]["Address"] = streetstring
		
				#print(" ".join(item.split()[:-3]))
		jdondata["Invoice"][0]["Billed Items"] = billeditems

		
		#jdondata = json.dumps(jdondata, indent=4)
		alljson.append(jdondata)
	#print(json.dumps(alljson, sort_keys=True, indent=4))
	print("feeding output to output.json")
	time.sleep(2)
	with open("output.json", "w") as output:
		json.dump(alljson, output, sort_keys=True, indent=4)
		#with open(image + ".txt", "w") as f:
	print("cleaning up script files")
	time.sleep(2)
	shutil.rmtree("images")
	for file in os.listdir("."):
		if file.endswith(".txt"):
			os.remove(file)
	print("successfully extracted data from {} to output.json".format(pdffile))
	print(os.listdir("."))
	time.sleep(2)

if __name__ == "__main__":
	extract(sys.argv[1])