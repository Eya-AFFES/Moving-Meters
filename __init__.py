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
        MV_F_intent = IntentBuilder("MVFIntent").require("moveKeyword").require("Mydistance").build()
        self.register_intent(MV_F_intent ,self.handle_MV_F_intent)
    
    def handle_MV_F_intent(self, message):
        self.speak_dialog("MV.F")
        dist=str(message.data.get("Mydistance"))
        msg="MF"
        T = ("1","one","2","two","3","three","4","four","5","five","6","six","7","seven","8","eight","9","nine")
        if (T[0] in dist) or (T[1] in dist):
          msg+="1\n"
        elif (T[2] in dist) or (T[3] in dist):
          msg+="2\n"
        elif (T[4] in dist) or (T[5] in dist):
          msg+="3\n"
        elif (T[6] in dist) or (T[7] in dist):
          msg+="4\n"  
        elif (T[8] in dist) or (T[9] in dist):
          msg+="5\n"
        elif (T[10] in dist) or (T[11] in dist):
          msg+="6\n"  
        elif (T[12] in dist) or (T[13] in dist):
          msg+="7\n" 
        elif (T[14] in dist) or (T[15] in dist):
          msg+="8\n" 
        elif (T[16] in dist) or (T[17] in dist):
          msg+="9\n" 
        else 
          msg="MVF"
        ser00.write(bytes(msg, 'utf-8'))  
 
    def stop(self):
        pass
 
def create_skill():
    return SpeakmeterSkill()
