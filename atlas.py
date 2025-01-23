from atlas.model import ChatModel, ChatRequest, ChatResponse

def main():
    # Create a chat model
    model = ChatModel(model="hermes-3-llama-3.2-3b")
    # model = ChatModel(model="qwen2-vl-7b-instruct")

    # Run the base chat model
    model.run()



if __name__ == "__main__":
    main()
