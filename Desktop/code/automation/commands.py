


import urllib2 as u
def retrieveCommands(PID):
	
	response=u.urlopen('https://runescapev5-basedtoaster.c9users.io/auto/commands/'+str(PID))
	html=response.read()
	html=html.split('<div id="body" class="body">')
	commands= html[1].split('</div>')[0]


	print commands
	commands=commands.replace("\n","")
	commands=commands.split(",")
	bs=commands[0]
	itemID=commands[1]
	amt=commands[2]
	price=commands[3]
	return(bs,itemID,amt,price)
#print retrieveCommands(1)


def submitTransaction(PID,bs,itemID,amt,price,currentLiquid):
	url="https://runescapev5-basedtoaster.c9users.io/auto/submit/"
	url+=str(PID)+"/"
	url+=str(bs)+"/"
	url+=str(itemID)+"/"
	url+=str(amt)+"/"
	url+=str(price)+"/"
	url+=str(currentLiquid)
	u.urlopen(url)
#submitTransaction(1,True,440,150,350,10000)
