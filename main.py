from chat_bot import ToolIntegration
from package_experiment import GREETING_MESSAGE
from package_experiment.greeting import GoodMorning, GOOD_MORNING_GREETING

if __name__ == "__main__":
   print(f"{GREETING_MESSAGE}")
   GoodMorning.greet(GOOD_MORNING_GREETING)
   tool_integration = ToolIntegration()
   tool_integration.run()
