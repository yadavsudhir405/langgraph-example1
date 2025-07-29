from chat_bot import AgenticTool, ToolIntegration
from package_experiment import GREETING_MESSAGE

if __name__ == "__main__":
   print(f"{GREETING_MESSAGE}")
   AgenticTool().run()
   # ToolIntegration().run()
