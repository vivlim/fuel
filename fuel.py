import formfill

#currently won't work because form is on an old version that doens't use the same labelling but it's supposed to update eventually? check later

def gallons_to_litres(gallons):
	return gallons # todo: implement
def add_fuel_entry(gallons,dollars,km):
	data = {}
	data['Gas Purchased (Litres)'] = gallons
	data['Amount Paid'] = dollars
	data['Distance(KM)'] = km

	url = "https://spreadsheets.google.com/viewform?formkey=dDZPN1RzdUZYcG5HRFJDeUZ2MGcwOWc6MQ&ifq"


