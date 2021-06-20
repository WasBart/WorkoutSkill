from adapt.intent import IntentBuilder
from chatterbox.skills.core import ChatterboxSkill, intent_handler

class WorkoutSkill(ChatterboxSkill):
    def __init__(self):
        super().__init__()
        self.pushups = ""
        self.situps = ""
        self.exercises = {}

    #@intent_handler('workout.intent')
    #def handle_workout_intent(self, message):
    #    self.speak('Tell me about your workout')
    #    self.pushups = self.get_response('How many pushups did you do?')
    #    self.situps = self.get_response('How many situps did you do?')
    #    self.speak('Thanks for recording your workout')
    @intent_handler('workout.intent')
    def handle_workout_intent(self, message):
        more_exercises = True
        self.speak('Tell me about your workout')
        while more_exercises:
            exercise = self.get_response('What was the exercise?')
            reps = self.get_response('How many repititions did you do?')
            done = self.get_response('Is that all?')
            if done == 'Yes':
                more_exercises = False

    @intent_handler('recap.intent')
    def handle_recap_intent(self, message):
        self.speak('This is how many pushups you did')
        self.speak('%s pushups' %self.pushups)
        self.speak('This is how many situps you did')
        self.speak('%s situps' %self.situps)

    def stop(self):
        pass

def create_skill():
    return WorkoutSkill()

