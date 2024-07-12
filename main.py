from openai import OpenAI
from event_handler import EventHandler
from setup import setup_assistant_and_vector_store

# Initialize OpenAI client
client = OpenAI()

# Run setup tasks only once
assistant, vector_store = setup_assistant_and_vector_store("docs")

#assistant = client.beta.assistants.retrieve('asst_pmk2J0kG1epLqaps3VP3ctoz')

# Create a new thread
thread = client.beta.threads.create()

def main_loop():
    """Main interaction loop."""
    while True:
        thread_message = input("What question did you have? No questions? Enter Q to exit.\n")
        
        if thread_message.lower() == "q":
            break

        message = client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=thread_message
        )
        
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="Please address the user as Jane Doe. The user has a premium account.",
            event_handler=EventHandler(client),
        ) as stream:
            stream.until_done()

if __name__ == "__main__":
    main_loop()
