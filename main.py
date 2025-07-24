from chat_bot.tool_integration import ToolIntegration
from package_experiment import GREETING_MESSAGE

if __name__ == "__main__":
   print(f"{GREETING_MESSAGE}")
   ToolIntegration().run()
