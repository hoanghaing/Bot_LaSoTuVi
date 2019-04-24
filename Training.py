from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Interpreter
from rasa_core.actions import Action
from rasa_core.events import SlotSet


def train_horoscopebot(data_json, config_file, model_dir):
    training_data = load_data(data_json)
    trainer = Trainer(config.load(config_file))
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name= 'horoscopebot')

def predict_intent(text):
    interpreter = Interpreter.load('./models/nlu/default/horoscopebot')
    print(interpreter.parse(text))


# train_horoscopebot('./data/data.json', 'config.json', './models/nlu')
# predict_intent("I am looking for my horoscope for today. I am wondering if you can tell me that.")


class GetTodaysHoroscope(Action):
   def name(self):
      return "get_todays_horoscope"
   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
      user_horoscope_sign = tracker.get_slot('horoscope_sign')
      """Write your logic to get today’s horoscope details
         for the given Horoscope sign based on some API calls
         or retrieval from the database"""
        return [SlotSet("horoscope_sign", user_horoscope_sign)]