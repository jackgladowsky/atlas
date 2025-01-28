from atlas.model import ChatModel
from atlas.agent import BaseAgent

def main():
    # Create a chat model
    model = ChatModel(model="qwen2.5-7b-instruct-1m")
    agent = BaseAgent(model)

    # Run the base chat model
    agent.run()



if __name__ == "__main__":
    main()
