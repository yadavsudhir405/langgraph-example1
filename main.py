from chat_bot import AgenticToolWithMemory, ToolIntegration, AgenticToolWithMemory
from package_experiment import GREETING_MESSAGE

if __name__ == "__main__":
   print(f"{GREETING_MESSAGE}")
   AgenticToolWithMemory().run()
   # ToolIntegration().run()
