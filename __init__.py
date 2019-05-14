# Copyright 2016 Mycroft AI Inc.

import subprocess
from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
import serial
ser00 = serial.Serial ("/dev/ttyS0", 9600) #Open port with baud rate

# TODO - Localization
LOGGER = getLogger(__name__)

class SpeakmeterSkill(MycroftSkill):
  
    def __init__(self):
        #This method is the constructor, and the key function it has is to define the name of the Skill.
        super(SpeakmeterSkill, self).__init__(name="SpeakmeterSkill")
        
    def initialize(self):
        #MV_F_intent = IntentBuilder("MVFIntent").require("moveKeyword").require("Mydistance").build()
        MV_F_intent = IntentBuilder("MVFIntent").require("moveKeyword").require("Mydistance").build()
        self.register_intent(MV_F_intent ,self.handle_MV_F_intent)
    def convert_meter(Mydistance)
        msg="MVF"
        T = ("1","one","2","two","3","three","4","four","5","five","6","six","7","seven","8","eight","9","nine")
        if (T[0] or T[1]) in Mydistance:
          msg+="1\n"
        elif (T[2] or T[3]) in Mydistance:
          msg+="2\n"
        elif (T[4] or T[5]) in Mydistance:
          msg+="3\n"
        elif (T[6] or T[7]) in Mydistance:
          msg+="4\n"  
        elif (T[8] or T[9]) in Mydistance:
          msg+="5\n"
        elif (T[10] or T[11]) in Mydistance:
          msg+="6\n"  
        elif (T[12] or T[13]) in Mydistance:
          msg+="7\n" 
        elif (T[14] or T[15]) in Mydistance:
          msg+="8\n" 
        elif (T[16] or T[17]) in Mydistance:
          msg+="9\n" 
    return msg      
      
    def handle_MV_F_intent(self, message):
        self.speak_dialog("MV.F")
        ser00.write(bytes(convert_meter(str(message.data.get("Mydistance")), 'utf-8'))  
        #msg="MVF"+str(message.data.get("Mydistance"))+"\n"
        #msg=str(message.data.get("Mydistance"))+"\n"
        #if Mydistance=="one meter"
        #msg="MVF"+"\n"
        #ser00.write(bytes(msg, 'utf-8'))    
        """
    def speak_back(self, message):
    
            Repeat the utterance back to the user.

        # Remove everything up to the speak keyword and repeat that
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['Speak'], '', utterance)
        self.speak(repeat.strip())

        """
    def stop(self):
        pass


def create_skill():
    return SpeakmeterSkill()
