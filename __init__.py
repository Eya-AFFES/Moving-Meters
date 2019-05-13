# Copyright 2016 Mycroft AI Inc.

import re
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
        MV_F_intent = IntentBuilder("MVFIntent").require("MVFKeyword").optionally("words").build()
        self.register_intent(MV_F_intent ,self.handle_MV_F_intent)
    
    def handle_MV_F_intent(self, message):
        self.speak_dialog("MV.F")
        msg="MVF"
        ser00.write(bytes(msg, 'utf-8'))    
    
    def speak_back(self, message):
        """
            Repeat the utterance back to the user.

        """
        # Remove everything up to the speak keyword and repeat that
        utterance = message.data.get('utterance')
        repeat = re.sub('^.*?' + message.data['Speak'], '', utterance)
        self.speak(repeat.strip())

    def stop(self):
        pass


def create_skill():
    return SpeakmeterSkill()
