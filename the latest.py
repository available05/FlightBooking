#THE LOGIN/SIGN UP
print('1:Sign up\n2.Log in')
ls=int(input("enter your choice"))
if ls==1:
    import csv
    def add_person(email, password):
        with open("people.csv", "a", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([email, password])
    def display_people(email):
        with open("people.csv", "r") as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                if len(row) >= 2 and row[0] == email:
                    return
            else:
                print("You have signed up. \nKindly continue with the log in step")
    email_input = input("Enter the email: ")
    chec=".com"not in email_input
    while chec:
        email_input=input("Kindly enter a valid email:")
    password_input = input("Enter the password: ")
    display_people(email_input)
    add_person(email_input, password_input)
else:
    import csv
    while True:
        file = open("people.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        file.close()

        email_input = input("Enter your email:")
        password = input("Enter your password:")
        login_successful = False

        for row in rows:
            if email_input == row[0] and password == row[1]:
                login_successful = True
                break

        if login_successful:
            print("You have successfully logged in.")
            break
        else:
            print("Invalid email or password. Please try again.")
    

import random
import smtplib
otp= random.randint(99999,999999)
print('LOGIN PAGE')
import smtplib
a=str(otp)
content= 'Thank you for visiting Akshayanam. \nPlease find your OTP for login.'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
password='vxjb bgbx zebu ukuk'
sender='akashayanam@gmail.com'
reciever=email_input
mail.login('akashayanam@gmail.com', password)
header='To:'+reciever+'\nsubject:OTP for login\n'
content=header+content+str(otp)
mail.sendmail(sender,reciever,content)
mail.close()
print('The email has successfully been sent to your registered Email address')
print('please enter the OTP sent to your email')
s=int(input('enter the OTP from the email here:'))
if s==otp:
    print('You have successfully logged in!')
while s!=otp:
    s=int(input('kindly enter the right otp'))    
#THE CITIES AND TIME
while True:
    sea={1:"Economy class",2:"Business class"}
    print(sea)
    qwerty=int(input("Enter the class in which you wish to travel:"))
    pl={'Agartala':'IXA','Agra':'AGR','Ahemdabad':'AMD','Aizawl':'AJL','Amritsar':'ATQ','Aurangabad':'IXU','Bagdogra':'IXB','Bareilly':'BEK','Belagavi':'IXG','Bengaluru':'BLR','Bhopal':'BHO','Bhubaneswar':'BBI','Chandigarh':'IXC',
        'Chennai':'MAA','Coimbatore':'CJB','Darbhanga':'DBR','Dehradun':'DED','Delhi':'DEL','Deoghar':'DGH','Dibrugarh':'DIB','Dimapur':'DMU',
        'Durgapur':'RDP','Gaya':'GAY','Goa':'GOI','Gorakhpur':'GOP','Guwahati':'GAU','Gwalior':'GWL','Hubli':'HBX','Hyderabad':'HYD','Imphal':'IMF',
        'Indore':'IDR','Itanagar':'HGI','Jabalpur':'JLR','Jaipur':'JAI','Jammu':'IXJ','Jodhpur':'JDH','Jorhat':'JRH','Kadapa':'CDP','Kannur':'CNN',
        'Kanpur':'KNU','Kochi':'COK','Kolhapur':'KLH','Kolkata':'CCU','Kozhikode':'CCJ','Kurnool':'KJB','Leh':'IXL','Lucknow':'LKO','Madurai':'IXM',
        'Mangaluru':'IXE','Mumbai':'BOM','Mysuru':'MYQ','Nagpur':'NAG','North Goa':'GOX','Pantnagar':'PGH','Patna':'PAT','Port Blair':'IXZ','Prayagraj':'IXD'
        ,'Pune':'PNQ','Raipur':'RPR','Rajahmundry':'RJA','Rajkot':'RAJ','Ranchi':'IXR','Shillong':'SHL','Shirdi':'SAG','Silchar':'IXS','Srinagar':'SXR',
        'Surat':'STV','Thiruvananthapuram':'TRV','Thiruchirappalli':'TRZ','Tirupati':'TIR','Tuticorin':'TCR','Udaipur':'UDR','Vadodara':'BDQ','Varnasi':'VNS',
        'Vijayawada':'VGA','Vishakapatnam':'VTZ', }
    price={'Agartala':8500,'Agra':1600,'Ahemdabad':3405,'Aizawl':7789,'Amritsar':7474,'Aurangabad':4320,'Bagdogra':8765,'Bareilly':5353,'Belagavi':7433,'Bengaluru':1466,'Bhopal':3457,'Bhubaneswar':9086,'Chandigarh':5890,'Chennai':4333,'Coimbatore':7860,'Darbhanga':9559,'Dehradun':7200,'Delhi':5504,'Deoghar':5978,'Dibrugarh':9873,'Dimapur':3971,'Durgapur':3067,'Gaya':6780,'Goa':4599,'Gorakhpur':5689,'Guwahati':4491,'Gwalior':4531,'Hubli':9857,'Hyderabad':3333,'Imphal':8888,'Indore':6666,'Itanagar':5646,'Jabalpur':9367,'Jaipur':7839,'Jammu':5126,'Jodhpur':6512,'Jorhat':1256,'Kadapa':4444,'Kannur':6430,'Kanpur':5100,'Kochi':6758,'Kolhapur':1289,'Kolkata':8000,'Kozhikode':9841,'Kurnool':7539,'Leh':4532,'Lucknow':2288,'Madurai':4311,'Mangaluru':7770,'Mumbai':6890,'Mysuru':1100,'Nagpur':4328,'North Goa':9000,'Pantnagar':5000,'Patna':1000,'Port Blair':8976,'Prayagraj':5550,'Pune':2222,'Raipur':6660,'Rajahmundry':7776,'Rajkot':2220,'Ranchi':1190,'Shillong':2230,'Shirdi':3879,'Silchar':5555,'Srinagar':9999,'Surat':1110,'Thiruvananthapuram':5660,'Thiruchirappalli':6650,'Tirupati':6888,'Tuticorin':1111,'Udaipur':6777,'Vadodara':3330,'Varnasi':7634,'Vijayawada':4600,'Vishakapatnam':3100}
    print(' 1. one-way travel \n 2. two-way travel \n 3. multicity travel')
    sumtot=0
    addition=[]
    multi=[]
    l=int(input('Enter the number of the type of travel:'))
    if l==1:
        cls=input('Enter your city of departure:')
        while cls.title() not in pl:
             cls=input('Your city is not found enter it again:')
        sumtot+=price[cls.title()]
        r1=input('Enter your city of arrival:')
        while r1.title() not in pl:
            r1=input('Your city is not found enter it again:')
        import datetime
        member_count=int(input('Enter the number of people travelling:'))
        for i in range(member_count):
            r={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
            y=int(input("Enter the year in which you wish to travel:"))
            while y<2024:
                        y=int(input("Enter valid year:"))
            m=input("Enter the month (in words) in which you wish to travel:")
            while m not in r:
                m=input("Enter a valid month:")
            for q in r:
                if m==q:
                    z=r[q]
            import calendar
            cal=calendar.TextCalendar()
            cal.prmonth(y,z)
            d=int(input("Enter the date of departure:"))
            if y%4==0:
                if r[m]==2:
                    while d>29:
                        d=int(input("Enter a correct date:"))
            if r[m]%2==0:
                if r[m]==2:
                    while d>28:
                        d=int(input("Enter a correct date:"))
                while d>30:
                    d=int(input("Enter a correct date:"))
            else:
                while d>31:
                    d=int(input("Enter a correct date:"))

            print("1.12:00am - 7:59am \n2.8:00am - 15:59pm \n3.16:00pm -  23:59pm")
            h=int(input("Choose your time slot:"))
            while h>3:
                print('Enter a valid slot:')
                h=int(input("Choose your time slot:"))
            if h==1:
                speci=datetime.datetime(y,z,d,4,30)
                time="4:30"
            if h==2:
                speci=datetime.datetime(y,z,d,11,00)
                time="11:00"
            if h==3:
                speci=datetime.datetime(y,z,d,18,45)
                time="18:45"
            
            
            print(speci)
                   
        sumtot+=price[r1.title()]
        if qwerty==2:
            sumtot=sumtot+10000
        addition.append(cls.title())
        addition.append(r1.title())
        print('The List of places which u are travelling are:',addition)
        
        break

    elif l==2:
        cls=input('Enter your city of departure:')
        while cls.title() not in pl:
             cls=input('Your city is not found enter it again:')
        sumtot+=price[cls.title()]
        r1=input('Enter yor city of arrival:')
        while r1.title() not in pl:
            r1=input('Your city is not found enetr it again:')
        import datetime
        member_count=int(input('Enter the number of people travelling:'))
        for i in range(member_count):
            r={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
            y=int(input("Enter the year in which you wish to travel:"))
            while y<2024:
                        y=int(input("Enter valid year:"))
            m=input("Enter the month (in words) in which you wish to travel:")
            while m not in r:
                m=input("Enter a valid month:")
            for q in r:
                if m==q:
                    z=r[q]
            import calendar
            cal=calendar.TextCalendar()
            cal.prmonth(y,z)
            d=int(input("Enter the date of departure:"))
            if y%4==0:
                if r[m]==2:
                    while d>29:
                        d=int(input("Enter a correct date:"))
            if r[m]%2==0:
                if r[m]==2:
                    while d>28:
                        d=int(input("Enter a correct date:"))
                while d>30:
                    d=int(input("Enter a correct date:"))
            else:
                while d>31:
                    d=int(input("Enter a correct date:"))

            print("1.12:00am - 7:59am \n2.8:00am - 15:59pm \n3.16:00pm -  23:59pm")
            h=int(input("Choose your time slot:"))
            while h>3:
                print('Enter a valid slot:')
                h=int(input("Choose your time slot:"))
            if h==1:
                speci=datetime.datetime(y,z,d,4,30)
                time="4:30"
            if h==2:
                speci=datetime.datetime(y,z,d,11,00)
                time="11:00"
            if h==3:
                speci=datetime.datetime(y,z,d,18,45)
                time="18:45"
            
            
            print(speci)
                    
        sumtot+=price[r1.title()]
        sumtot*=2
        if qwerty==2:
            sumtot=sumtot+10000
        addition.append(cls.title())
        addition.append(r1.title())
        print('The List of places which u are travelling to and from are:',addition)
        
        break
    
    elif l==3:
         go=int(input('Enter the number of places going to travel:'))
         cls=input('Enter your city of departure:')
         multi.append(cls)
         for ace in range(1,go+1):
             r1=input('Enter your city of arrival:')
             while r1.title() not in pl:
                 r1=input('Enter a valid city:')
             multi.append(r1)    
             import datetime
             member_count=int(input('Enter the number of people travelling:'))
             for i in range(member_count):
                    r={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
                    y=int(input("Enter the year in which you wish to travel:"))
                    while y<2024:
                        y=int(input("Enter valid year:"))
                        
                    m=input("Enter the month (in words) in which you wish to travel:")
                    while m not in r:
                        m=input("Enter a valid month")
               
                    for q in r:
                        if m==q:
                            z=r[q]
                    import calendar
                    cal=calendar.TextCalendar()
                    cal.prmonth(y,z)
                    d=int(input("Enter the date of departure:"))
                    if y%4==0:
                        if r[m]==2:
                            while d>29:
                                d=int(input("Enter a correct date:"))
                    if r[m]%2==0:
                        if r[m]==2:
                            while d>28:
                                d=int(input("Enter a correct date:"))
                            while d>30:
                                d=int(input("Enter a correct date:"))
                    else:
                        while d>31:
                            d=int(input("Enter a correct date:"))

                    
                    print("1.12:00am - 7:59am \n2.8:00am - 15:59pm \n3.16:00pm -  23:59pm")
                    h=int(input("Choose your time slot:"))
                    while h>3:
                        print('Enter a valid slot:')
                        h=int(input("Choose your time slot:"))
                    if h==1:
                        speci=datetime.datetime(y,z,d,4,30)
                        time="4:30"
                    if h==2:
                        speci=datetime.datetime(y,z,d,11,00)
                        time="11:00"
                    if h==3:
                        speci=datetime.datetime(y,z,d,18,45)
                        time="18:45"
                    
                    
                    print(speci)
                            
         addition.append(r1)
         addition.append(cls)
         sumtot+=price[r1.title()]
         if qwerty==2:
            sumtot=sumtot+10000
         print('The List of places you are travelling to are:',multi)
         print('Your total amount is:',sumtot, "rupees")
         
         break

    else:
        print("Invalid input. Please enter a valid option")
#THE BILL
import random
member_amount=member_count*sumtot
arl={1:'Air Asia India',  2:'Air India', 3:'Air India Express', 4:'Go First', 5:'IndiGo', 6:'SpiceJet', 7:'Vistara',8:'AIX Connect',9:'Akasa Air'}
print(arl)
ar=int(input('Enter the airline with which u are travelling:'))
while ar not in arl:
    ar=int(input('Enter a valid airline:'))

member_amount=member_count*sumtot
count_age=[]
list3=[]
if member_count==1:
    print('The total ticket airfare for',member_count,'person is:',sumtot)
for i in range(0,member_count):
    age=int(input('Enter your age:'))
    count_age.append(age)
print('50% discount for people aged less than or equal to 2 years or older than 60 years')
for i in count_age:
    if  i<=2 or i>60:
            sumtot1=50/100*sumtot
            sumtot2=sumtot-sumtot1
            list3.append(sumtot2)
    else:
        list3.append(sumtot)
tot_val=sum(list3)
print('The amount per person is:',sumtot)
print('The total ticket airfare for',member_count,'people is/are:',tot_val, "rupees")
print('Please proceed with further ticket details')
print(' 1.UPI\n 2.Credit\n 3.Debit')
ch1=int(input('Enter your choice'))
if ch1==1:
  
    mob=input('Enter your mobile number:')
    while len(mob)!=10:
        mob=input('Enter your mobile number correctly:')
    import random
    import smtplib
    otp= random.randint(999,9999)
    import smtplib
    a=str(otp)
    content= 'Please find your OTP for verification.'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    password='vxjb bgbx zebu ukuk'
    sender='akashayanam@gmail.com'
    reciever=email_input
    mail.login('akashayanam@gmail.com', password)
    header='To:'+reciever+'\nsubject:OTP for payment\n'
    content=header+content+str(otp)
    mail.sendmail(sender,reciever,content)
    mail.close()
    print('An email has successfully been sent to your registered Email address')
    print('Please enter the OTP sent to your email')
    s=int(input('Enter the OTP from the email here:'))
    if s==otp:
        print('Payment has been done successfully!')
    while s!=otp:
        s=int(input('Kindly enter the right otp'))

    
if ch1==2:
    print('---credit card details---')
    nme=input("Enter you name on the card:")
    cvv=input('Enter your cvv number:')
    while len(cvv)!=3:
        cvv=input('Enter the correct cvv no.:')
   
    from datetime import datetime
    currentYear = datetime.now().year
    y1=int(input("Enter the year in which your credit card expires :"))
    while y1<currentYear:
        print("Seems like your credit card has expired.Kindly proceed with UPI")
        mob=input('Enter your mobile number:')
        while len(mob)!=10:
            mob=input('Enter your mobile number correctly:')
        break

    
        
    import random
    import smtplib
    otp= random.randint(999,9999)
    import smtplib
    a=str(otp)
    content= 'Please find your OTP for verification.'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    password='vxjb bgbx zebu ukuk'
    sender='akashayanam@gmail.com'
    reciever=email_input
    mail.login('akashayanam@gmail.com', password)
    header='To:'+reciever+'\nsubject:OTP for payment\n'
    content=header+content+str(otp)
    mail.sendmail(sender,reciever,content)
    mail.close()
    print('A mail has successfully been sent to your registered Email address')
    print('Please enter the OTP sent to your email')
    s=int(input('enter the OTP from the email here:'))
    if s==otp:
        print('Payment has been done successfully!')
    while s!=otp:
        s=int(input('kindly enter the right otp'))
    
if ch1==3:
    print('debit card details')
    nme=input("Enter you name on the card:")
    cvv=input('Enter your cvv number:')
    while len(cvv)!=3:
        cvv=input('Enter the correct cvv no.:')
   
    from datetime import datetime
    currentYear = datetime.now().year
    y1=int(input("Enter the year in which your debit card expires :"))
    while y1<currentYear:
        print("Seems like your debitt card has expired.Kindly proceed with UPI")
        mob=input('Enter your mobile number:')
        while len(mob)!=10:
            mob=input('Enter your mobile number correctly:')
        break
                  
        
    import random
    import smtplib
    otp= random.randint(999,9999)
    import smtplib
    a=str(otp)
    content= 'Please find your OTP for verification.'
    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    password='vxjb bgbx zebu ukuk'
    sender='akashayanam@gmail.com'
    reciever=email_input
    mail.login('akashayanam@gmail.com', password)
    header='To:'+reciever+'\nsubject:OTP for payment\n'
    content=header+content+str(otp)
    mail.sendmail(sender,reciever,content)
    mail.close()
    print('An email has successfully been sent to your registered Email address')
    print('Please enter the OTP sent to your email')
    s=int(input('Enter the OTP from the email here:'))
    if s==otp:
        print('Payment has been done successfully!')
    while s!=otp:
        s=int(input('Kindly enter the right otp'))
        



    
import smtplib
from email.mime.text import MIMEText
email1=reciever
import random
fnno=random.randint(100,999)
fnalpha1=random.randint(65,90)
fnalpha2=random.randint(65,90)
fnalpha3=random.randint(65,90)
flightno=chr(fnalpha1)+ chr(fnalpha2)+chr(fnalpha3)+str(fnno)
for i in range(1,member_count+1):
    print('Person',i)
    fn=input("Enter your first name:")
    ln=input("Enter your last name:")
    def send_flight_ticket(email, flight_details): 
        subject = "Your Flight Ticket"
        body = f"Dear {fn} {ln},\n\nHere are your flight details:\n\n{flight_details}"
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = "akashayanam@gmail.com"         
        msg['To'] = email1
        smtp_server = "smtp.gmail.com"  
        smtp_port = 587
        smtp_username = "akashayanam@gmail.com"  
        smtp_password = "vxjb bgbx zebu ukuk"  
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, email, msg.as_string())
    if l==1:
        flight_details = 'Flight Number:', flightno ,'through airline',arl[ar],'in' ,sea[qwerty], 'Departure:',cls,  'Arrival:', r1, 'Date:',str(d)+'-'+str(z)+'-'+str(y), 'at',time
        send_flight_ticket( email1, flight_details)
    if l==2:
        flight_details = 'Flight Number:', flightno ,'through airline',arl[ar],'in' ,sea[qwerty], 'Departure:',cls,  'Arrival:', r1,'and back to',cls,'Date:',str(d)+'-'+str(z)+'-'+str(y), 'at',time
        send_flight_ticket( email1, flight_details)
    if l==3:
        flight_details = 'Flight Number:', flightno ,'through airline',arl[ar],'in' ,sea[qwerty], 'Departure:',cls,  'Arrival destinations:', multi, 'Date:',str(d)+'-'+str(z)+'-'+str(y), 'at',time
        send_flight_ticket( email1, flight_details)
        
print("The email has successfully been sent to your email.Enjoy your flight!")

