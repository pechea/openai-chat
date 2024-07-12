import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

def create_assistant():
    """Create and return the assistant."""
    return client.beta.assistants.create(
        name="Financial Analyst Assistant",
        instructions="You are an expert financial analyst. Use your knowledge base to answer questions about audited financial statements.",
        model="gpt-4o",
        tools=[{"type": "file_search"}],
    )

def create_vector_store():
    """Create and return the vector store."""
    return client.beta.vector_stores.create(name="Financial Statements")

def get_file_streams(directory):
    """Get file streams for all files in the given directory."""
    print([filename for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename)) and not filename.startswith('.')])
    return [open(os.path.join(directory, filename), "rb") for filename in os.listdir(directory) if os.path.isfile(os.path.join(directory, filename)) and not filename.startswith('.')]

def upload_files_to_vector_store(vector_store_id, file_streams):
    """Upload files to the vector store."""
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store_id, files=file_streams
    )

def update_assistant_with_vector_store(assistant_id, vector_store_id):
    """Update the assistant with the vector store ID."""
    return client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
    )

def setup_assistant_and_vector_store(directory):
    """Setup the assistant and vector store."""
    assistant = create_assistant()
    vector_store = create_vector_store()
    file_streams = get_file_streams(directory)
    upload_files_to_vector_store(vector_store.id, file_streams)
    updated_assistant = update_assistant_with_vector_store(assistant.id, vector_store.id)
    return updated_assistant, vector_store

# if __name__ == "__main__":
#     setup_assistant_and_vector_store("docs")
