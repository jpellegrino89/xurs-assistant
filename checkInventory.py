import requests, smtplib, json, httplib

#smtplib configuration
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '{email}', '{password}' )

#Parse 1
def parseSubmit(xurLocation, exoticType, exoticName):
	connection = httplib.HTTPSConnection('api.parse.com', 443)
	connection.connect()
	connection.request('POST', '/1/classes/inventory', json.dumps({
      	 "xurLocation": xurLocation,
       	 "exoticType": exoticType,
       	 "exoticName": exoticName
     	}), {
       	"X-Parse-Application-Id": "{AppID}",
       	"X-Parse-REST-API-Key": "{API-Key}",
       	"Content-Type": "application/json"
     	})
	results = json.loads(connection.getresponse().read())
	print results
	return;

#dictionary to hold extra headers
HEADERS = {"X-API-Key":'{Bungie API Key}'}
 
#make request for Xur Inventory
r = requests.get("https://www.bungie.net/Platform/Destiny/Advisors/Xur/", headers=HEADERS);

#make request for Item Detail Example
d = requests.get("https://www.bungie.net/Platform/Destiny/Manifest/6/591060261/", headers=HEADERS);
 
#convert the json object we received into a Python dictionary object
#and print the name of the items
inventoryItem = r.json()
itemDefinition = d.json()
weaponsArray = list()

#Collect only Exotic Gear
#if str(inventoryItem['Response']['data']['saleItemCategories'][2]['categoryTitle']) == "Exotic Gear":
#	print ("Found Exotic Gear: ")
	
#print ("Before Function")
#print (inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'])
#try: itemHash0 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][0]['item']['itemHash']
#except: pass

#try: itemHash1 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][1]['item']['itemHash']
#except: pass

#try: itemHash2 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][2]['item']['itemHash']
#except: pass

#try: itemHash3 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][3]['item']['itemHash']
#except: pass

#try: itemHash4 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][4]['item']['itemHash']
#except: pass

#try: itemHash5 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][5]['item']['itemHash']
#except: pass

#try: itemHash6 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][6]['item']['itemHash']
#except: pass

#try:itemHash7 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][7]['item']['itemHash']
#except: pass

#try: itemHash8 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][8]['item']['itemHash']
#except:pass

#try: itemHash9 = inventoryItem['Response']['data']['saleItemCategories'][2]['saleItems'][9]['item']['itemHash']
#except: pass



def lookupItem(itemHash):
	print ("Performing Function")
	print ("")
	requestString = "https://www.bungie.net/Platform/Destiny/Manifest/6/" + str(itemHash) + "/"
	print (requestString)
	
	d = requests.get(requestString, headers=HEADERS);
	itemDefinition = d.json()
	itemResult=(itemDefinition['Response']['data']['inventoryItem']['itemName'])
	itemType=(itemDefinition['Response']['data']['inventoryItem']['itemTypeName'])
	itemResult.replace("u", " ")
	print (itemResult)
	itemResultandType=itemType + ": " + itemResult
	#if (itemType == "Auto Rifle" or itemType == "Scout Rifle"):
	weaponsArray.append(itemResultandType)
	parseSubmit("The Tower", itemType, itemResult)
	return;

#Lookup sample item for testing during days where Xur has no Inventory
try: lookupItem("591060261")
except: pass

#try: lookupItem(itemHash1)
#except: pass

#try: lookupItem(itemHash2)
#except: pass

#try: lookupItem(itemHash3)
#except: pass

#try: lookupItem(itemHash4)
#except: pass

#try: lookupItem(itemHash5)
#except: pass

#try: lookupItem(itemHash6)
#except: pass

#try: lookupItem(itemHash7)
#except: pass

#try: lookupItem(itemHash8)
#except: pass

#try: lookupItem(itemHash9)
#except: pass

#try: lookupItem(itemHash10)
#except: pass

#print (weaponsArray)

#textString = "Xur has " + str(weaponsArray).replace("u'","'").replace("u\"","\"")
textString = "Xur has [Zhalo Supercell]"

print (textString)
server.sendmail( 'Xur', '{Receiving SMS number}', textString)
	
#print (itemDefinition['Response']['data']['inventoryItem']['itemName'])
#print(inventoryItem)
#print (itemDefinition)