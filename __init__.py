from adapt.intent import IntentBuilder
from chatterbox.skills.core import ChatterboxSkill, intent_handler

class WorkoutSkill(ChatterboxSkill):
    def __init__(self):
        super().__init__()
        self.pushups = ""
        self.situps = ""

    @intent_handler('workout.intent')
    def handle_workout_intent(self, message):
        self.speak('Tell me about your workout')
        pushups = self.get_response('How many pushups did you do?')
        situps = self.get_response('How many situps did you do?')
        self.speak('Thanks for recording your workout')

    @intent_handler('recap.intent')
    def handle_recap_intent(self, message):
        self.speak('This is how many pushups you did')
        self.speak(pushups)
        self.speak('This is how many situps you did')
        self.speak(situps)

    def stop(self):
        pass

def create_skill():
    return WorkoutSkill()

