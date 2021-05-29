from adapt.intent import IntentBuilder
from chatterbox import ChatterboxSkill, intent_handler

class WorkoutSkill(ChatterboxSkill):
    def __init__(self):
        super().__init__()
        self.pushups = ""
        self.situps = ""

    @intent_handler('workout.intent')
    def handle_workout(self, message):
        self.speak('Tell me about your workout')
        pushups = self.get_response('How many pushups did you do?')
        situps = self.get_response('How many situps did you do?')
        self.speak('Thanks for recording your workout')

    @intent_handler('recap.intent')
    def handle_recap(self, message):
        self.speak('This is how many pushups you did')
        self.speak(pushups)
        self.speak('This is how many situps you did')
        self.speak(situps)
        

    def initialize(self):
        my_setting = self.settings.get('my_setting')

    def stop(self):
        pass

def create_skill():
    return WorkoutSkill()

