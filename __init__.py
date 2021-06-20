from adapt.intent import IntentBuilder
from chatterbox.skills.core import ChatterboxSkill, intent_handler

class WorkoutSkill(ChatterboxSkill):
    def __init__(self):
        super().__init__()
        self.pushups = ""
        self.situps = ""
        self.exercises = {}

    @intent_handler('workout.intent')
    def handle_workout_intent(self, message):
        more_exercises = True
        self.speak('Tell me about your workout')
        while more_exercises:
            exercise = self.get_response('What was the exercise?')
            reps = self.get_response('How many repititions did you do?')
            self.exercises[exercise] = reps
            done = self.get_response('Is that all?')
            if done == 'yes':
                self.speak('Thanks for recording your workout')
                more_exercises = False

    @intent_handler('recap.intent')
    def handle_recap_intent(self, message):
        for key, value in self.exercises.items():
            self.speak('This is how many %s you did' %key)
            self.speak('%s %s' % (value, key))
        self.speak('That was your previous workout')

    def stop(self):
        pass

def create_skill():
    return WorkoutSkill()

