#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
from tesla_api import TeslaApiClient

import io

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

class Tesla_app(object):
    """Class used to wrap action code with mqtt connection
        
        Tesla appp
        Dispatch the intents to the corresponding actions
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None

        # start listening to MQTT
        self.start_blocking()
        
    # --> Sub callback function, one per intent

    #===car_name intent action ==========================================
    def car_name(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)
        print self.config

        # if need to speak the execution result by tts
        hermes.publish_start_session_notification(intent_message.site_id, "Action1 has been done", "")


    #===car_location intent action ==========================================
    def car_location(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)


    #===car_location intent action ==========================================
    def car_location(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)


    #===car_odometer intent action ==========================================
    def car_odometer(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)


    #===car_inside_temp intent action ==========================================
    def car_inside_temp(self, hermes, intent_message):
        # terminate the session first if not continue
        hermes.publish_end_session(intent_message.session_id, "")
        
        # action code goes here...
        print '[Received] intent: {}'.format(intent_message.intent.intent_name)


        # car_name
        # car_location
        # car_odometer
        # car_inside_temp
        # car_outside_temp
        # car_estimated_milage
        # car_battery_level
        # car_climate
        # car_info


    # --> Master callback function, triggered everytime an intent is recognized
    def master_intent_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name
        if coming_intent == 'cellerich:tesla:car_name':
            self.car_name(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_location':
            self.car_location(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_odometer':
            self.car_odometer(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_inside_temp':
            self.car_inside_temp(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_outside_temp':
            self.car_outside_temp(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_estimated_milage':
            self.car_estimated_milage(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_battery_level':
            self.car_battery_level(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_climate':
            self.car_climate(hermes, intent_message)
        if coming_intent == 'cellerich:tesla:car_info':
            self.car_info(hermes, intent_message)


    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.master_intent_callback).start()

if __name__ == "__main__":
    Tesla_app()