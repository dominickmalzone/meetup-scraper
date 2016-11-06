from bs4 import BeautifulSoup
import urllib2
import csv


topic_to_scrape = raw_input("Keyword to search to search for: ")
url = "http://api.meetup.com/2/groups.xml/?&topic=" + topic_to_scrape +"&order=members&key=f4243746215f7de1a57433b3e56"
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content,'xml')

#choose output file name
resultFile = open(topic_to_scrape + ".csv", 'wb')
wr = csv.writer(resultFile, dialect='excel')

#Getting info from BeautifulSoup
members = soup.find_all("members")
length = len(members)
urlname = soup.find_all("urlname")
organizer = soup.find_all("organizer")
city = soup.find_all("city")

RESULT = ['Number of Members','Group Name','Location','Meetup Link','Organizer ID','Organizer Image']
wr.writerow(RESULT)

for i in range(length):
	print "Getting Data: " + str(i)
	#Getting the members
	temp_members = members[i].contents  						
	for child in (temp_members):
		child_members = child.encode('utf-8')
	#Getting the url name
	temp_url = urlname[i].contents
	for child in (temp_url):
		child_url = child.encode('utf-8')
		child_link = 'https://www.meetup.com/' + child_url + '/'
	#Getting the city
	temp_city = city[i].contents
	for tag in soup.find_all("organizer"):
		for child in (temp_city):
			child_city = child.encode('utf-8')
	#Getting the organizer and the Organizer ID
	temp_organizer = organizer[i].contents
	organizer_contents = temp_organizer
	temp_organizer = organizer_contents[0].contents
	for child in temp_organizer:
		child_id = child.encode('utf-8')
	temp_organizer = organizer_contents[1].contents
	
	for child in temp_organizer:
		child = str(child)
		child_str = child.replace('<photo_link>','')
		child_str1 = child_str.replace('</photo_link>','')
		child_name = child_str1.encode('utf-8')

	excelList = [child_members,child_url,child_city,child_link,child_id,child_name]
	wr.writerow(excelList)

