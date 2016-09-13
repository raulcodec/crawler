import urllib2
from bs4 import BeautifulSoup

file_parsd_cont =open("parsed_content.txt","w")
file_op = open("gas_station_stats.txt","w")


def data_extract(tr_list):
    i=0
    #Reading all the tabular data in a loop function and writing it to gas station statistics file
    while ( i < len(tr_list)):
        file_op.write(tr_list[i].text.replace('\n','\t'))
        file_op.write('\n')
        i=i+1



def main():

    resp =  urllib2.urlopen("http://www.statisticbrain.com/gas-station-statistics/")
    #Using html parser ,parsing the html content using Beautiful Soup module
    parsed_content = BeautifulSoup(resp,'html.parser')
    #print parsed_content.prettify().encode('utf-8')
    #writing the initial parsed content in parsed_content.txt
    file_parsd_cont.write(parsed_content.prettify().encode('utf-8'))

    #finding all the tabular records from the parsed content and sending to extract function
    tr_list= parsed_content.find_all('tr')
    #print tr_list
    data_extract(tr_list)


    file_op.close()
    file_parsd_cont.close()

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it