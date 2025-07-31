from chat_bot import AgenticToolWithMemory, ToolIntegration, AgenticToolWithMemory, HumanLoopChatBot
from package_experiment import GREETING_MESSAGE

if __name__ == "__main__":
   print(f"{GREETING_MESSAGE}")
   HumanLoopChatBot().run()
   # ToolIntegration().run()
