import re
def isPhoneNumber(text):
	return re.match(r'(\d{3}-\d{3}-\d{4})',text)!=None

print("415-555-4242 is a phone number: ", end="") 
print(isPhoneNumber("415-555-4242")) 
print("415-5553-4242 is a phone number: ", end="") 
print(isPhoneNumber("415-5553-4242")) 
print("Dhaka is a phone number: ", end="") 
print(isPhoneNumber("Dhaka"))
