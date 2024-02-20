#Create variable email and store your email information to variable.
email= "Kimberleyr7@nycstudents.net"  #similar mjordan@nba.com
#b) Use slicing to print the email address.
print(email[:])
#c) Use slicing and string methods to print only the user name all in lowercase.
username=email[0:11]
print(username.lower())
#d) Use slicing and string methods to print only the company name all in uppercase.
companyName=(email[11:23])
print(companyName.upper())