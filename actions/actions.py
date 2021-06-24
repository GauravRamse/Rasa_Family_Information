# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class Action_Recieve_Name(Action):

    def name(self) -> Text:
        return "action_recieve_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Your name will be saved as {text}")

        return [SlotSet("name", text)]

class Action_Say_Name(Action):
    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker:Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]] :
        name = tracker.get_slot("name")

        if not name:
            dispatcher.utter_message(text= "I don't know your name")
        else:
            dispatcher.utter_message(text = f"your name is {name}")

        return []

