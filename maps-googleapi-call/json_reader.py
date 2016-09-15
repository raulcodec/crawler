import json
import urllib2


person_details = open("/home/vagrant/python_scripts/person_location_details.json","r")
open_file= open("/home/vagrant/python_scripts/referencedaddress_person.json","w")

# function to capture the address obtained from the maps google api based on geo location co-ordinates sent
def addr(lat,long):
    print lat
    print long
    resp = urllib2.urlopen("http://maps.googleapis.com/maps/api/geocode/json?latlng="+str(lat)+","+str(long))
    #print resp.read()
    add_obtained=resp.read()
    add_json= json.loads(add_obtained)
    #print add_json
    #print add_obtained[:6]
    # if no address obtained for co-ordinates ,make refernced address as none
    if (add_json["status"]=="ZERO_RESULTS"):
        address = "none"
    else:
    # if address found for the co ordinates then add it in the key field
        address = add_json["results"][0]["formatted_address"]
    return address


def main():
    i= 0
    parsed_details = json.load(person_details)
    print len(parsed_details)
    #print parsed_detailsl
    # capture the geo location details and pass it to map_addr function
    while i < len(parsed_details):
        lat_param =parsed_details[i]["latitude"]
        long_param=parsed_details[i]["longitude"]
        #open_file.write(str(lat_param)+"|"+str(long_param)+"\n")
        print long_param
        print lat_param
        map_add = addr(lat_param,long_param)
        print map_add
        # add the address obtained in the json document for each person 
        parsed_details[i]['referenced_address'] = str(map_add)
        i=i+1
    json.dump(parsed_details,open_file,indent=3)

if __name__ == '__main__':     # if the function is the main function ...
    main() # ...call it


person_details.close()
open_file.close()
