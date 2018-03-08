import pyaudio
import speech_recognition as sr
from pygame import mixer
import os
from  random import randint
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule
import mysql.connector
from mysql.connector import errorcode
import time

doss = os.getcwd()
i=0
n=0

while (i<1):

    try:
         n=n+1
         throw=['Do you take prescription medications?','Do you take prescription medications?']
         speekmodule.speek(throw,n,mixer)
         print('Do you take prescription medications')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message :
            a=1
         else:
            a=0; 
         print (message)

         throw=['Do you take vitamins?','Do you take vitamins?']
         speekmodule.speek(throw,n,mixer)
         print('Do you take vitamins')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            b=1
         else:
            b=0
         print (message)

         throw=['Do you take supplements?','Do you take supplements?']
         speekmodule.speek(throw,n,mixer)
         print('Do you take supplements')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            c=1
         else:
            c=0
         print (message)



         throw=['Do you have any allergy?','Do you have any allergy?']
         speekmodule.speek(throw,n,mixer)
         print('Do you have any allergy')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            d=1
         else:
            d=0
         print (message)
         f=0
         g=0
         h=0
         i=0
         j=0
         k=0
         l=0

         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            throw=['Are you allergic to any medications?','Are you allergic to any medications?']
            speekmodule.speek(throw,n,mixer)
            print('Are you allergic to any medications')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                 audio = r.adjust_for_ambient_noise(source)
                 r.energy_threshold += 280
                 audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                e=1
            print (message)

            throw=['Are you allergic to iodine?','Are you allergic to iodine?']
            speekmodule.speek(throw,n,mixer)
            print('Are you allergic to iodine')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                 f=1
            print (message)

            throw=['Are you allergic to latex?','Are you allergic to latex?']
            speekmodule.speek(throw,n,mixer)
            print('Are you allergic to latex')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                 g=1
            print (message)

            throw=['Are you allergic to adhesive or tape?','Are you allergic to adhesive or tape?']
            speekmodule.speek(throw,n,mixer)
            print('Are you allergic to adhesive or tape')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                h=1
            print (message)

            throw=['Are you allergic to any metals?','Are you allergic to any metals?']
            speekmodule.speek(throw,n,mixer)
            print('Are you allergic to any metals')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                 i=1
            print (message)

            throw=['Do you have any food allergies?','Do you have any food allergies?']
            speekmodule.speek(throw,n,mixer)
            print('Do you have any food allergies?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                 j=1
            print (message)

            throw=['Do you have any environmental allergies?','Do you have any environmental allergies?']
            speekmodule.speek(throw,n,mixer)
            print('Do you have any environmental allergies')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                k=1
            print (message)

            throw=['Do you have any seasonal allergies?','Do you have any seasonal allergies?']
            speekmodule.speek(throw,n,mixer)
            print('Do you have any seasonal allergies?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.adjust_for_ambient_noise(source)
                r.energy_threshold += 280
                audio = r.listen(source)
    
         
            s = (r.recognize_google(audio))
            message = (s.lower())
            if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
                l=1
            print (message)

         throw=['Have you had any past surgeries?','Have you had any past surgeries?']
         speekmodule.speek(throw,n,mixer)
         print('Have you had any past surgeries?')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
             m=1
         else:
             m=0
         print (message)

         throw=['Do you have any implanted devices?','Do you have any implanted devices?']
         speekmodule.speek(throw,n,mixer)
         print('Do you have any implanted devices')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
              n=1
         else:
              n=0
         print (message)
         
         throw=['In your family,any one have Cancer?','In your family,any one have Cancer?']
         speekmodule.speek(throw,n,mixer)
         print('In your family,any one have Cancer')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
             o=1
         else:
             o=0
         print (message)
         
         throw=['In your family,any one have Heart disease?','In your family,any one have Heart disease?']
         speekmodule.speek(throw,n,mixer)
         print('In your family,any one have Heart disease')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            p=1
         else:
            p=0
         print (message)
         
         throw=['In your family,any one have Diabetes?','In your family,any one have Diabetes?']
         speekmodule.speek(throw,n,mixer)
         print('In your family,any one have Diabetes?')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
             q=1
         else:
             q=0
         print (message)

         throw=['In your family,any one have Bleeding disorders?','In your family,any one have Bleeding disorders?']
         speekmodule.speek(throw,n,mixer)
         print('In your family,any one have Bleeding disorders')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            t=1
         else:
            t=0
         print (message)

         throw=['In your family,any one have Other chronic conditions?','In your family,any one have Other chronic conditions?']
         speekmodule.speek(throw,n,mixer)
         print('In your family,any one have Other chronic conditions')
         r = sr.Recognizer()
         with sr.Microphone() as source:
             audio = r.adjust_for_ambient_noise(source)
             r.energy_threshold += 280
             audio = r.listen(source)
    
         
         s = (r.recognize_google(audio))
         message = (s.lower())
         if ('yes') in message or ('ya') in message or ('es') in message or ('s') in message or ('yeah') in message:
            u=1
         else:
            u=0
         print (message)
         i=2
         '''
         cnx = mysql.connector.connect(user='root',
                                database='patientInformation')
         cursor = cnx.cursor()
  
  
         cursor.execute ("select uid, age,state from patientInformation.login")
         # fetch all of the rows from the query
         data = cursor.fetchall ()
         # print the rows
         for row in data :
              print row[0], row[1]
         
         id=randint(1000,1100)
         
         ag=row[1]
         no=1
         v=row[2]
         # cursor.execute("INSERT INTO patientInformation.patientHealthSummary VALUES(&id,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,'hars',2,1)")
         cursor.execute("INSERT INTO patientInformation.patientHealthSummary VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(id,a,b,c,d,g,h,i,j,k,l,m,n,o,q,t,u,f,v,ag,p))
         cnx.commit()
         cursor.close()
         cnx.close()
         '''
         throw=['Thanks for your time','Thanks for your time']
         speekmodule.speek(throw,n,mixer)


        
    except sr.UnknownValueError:
         print("$could not understand audio")
    except sr.RequestError as e:
         print("Could not request results$; {0}".format(e))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
             print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
             print("Database does not exist")
        else:
          print(err)
    else:
        cnx.close()