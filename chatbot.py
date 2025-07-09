def chatbot():
    print("Chatbot: Hello! Type something to chat (type 'exit' to quit).")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
        elif user_input == "exit":
            print("Chatbot: Chat ended. Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

# Run the chatbot
chatbot()
