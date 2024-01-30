# import opencage
import phonenumbers
# from opencage.geocoder import OpenCageGeocode
from phonenumbers import carrier, geocoder

pepnumber = phonenumbers.parse("+91 XXXXXXXXXX")
location = geocoder.description_for_number(pepnumber,"en")
print(location)

print(carrier.name_for_number(pepnumber,"en"))