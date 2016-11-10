


import urllib2 as url
def retrieveCommands(PID):
	
	response=url.urlopen('https://runescapev5-basedtoaster.c9users.io/auto/commands/'+str(PID))
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
print retrieveCommands(1)
