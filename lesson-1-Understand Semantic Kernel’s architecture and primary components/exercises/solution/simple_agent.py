import os
import asyncio
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatPromptExecutionSettings
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.functions import KernelArguments

# -----------------
# Load Environmental Variables
# -----------------
load_dotenv()

api_key = os.getenv("AZURE_OPENAI_KEY")
url = os.getenv("URL")
api_version = "2024-12-01-preview"

# -----------------
# Initialize the kernel
# -----------------
kernel = Kernel()

# -----------------
# Define a chat service
# -----------------
deployment = "gpt-4.1-mini"

chat_service = AzureChatCompletion(
    deployment_name=deployment,
    api_key=api_key,
    base_url=f"{url}{deployment}",
    api_version=api_version
)

# -----------------
# Register the chat service in the kernel
# -----------------
kernel.add_service(chat_service)

# -----------------
# Create agent using registered service
# -----------------
agent_instructions = """
    You are an expert in data analysis.
    You can answer any questions about how to analyse data, giving explanations on complex statistical analysis.
    You can not answer questions about any other subject
"""

settings = OpenAIChatPromptExecutionSettings()
settings.temperature = 1.0
settings.max_tokens = 300

agent = ChatCompletionAgent(
    service=chat_service,
    name="SK-Assistant",
    instructions=agent_instructions,
    arguments=KernelArguments(settings)
)

# -----------------
# Main
# -----------------
async def main():
    
    prompts = [
        "What is the average of 11,22,33",
        "Summarize the plot of Romeo and Juliet",
        "List the first 5 prime numbers",
        "Translate 'Good morning' into Spanish",
        "Give me a statistical summary for this data: 233,555,9866,2345,77"
    ]

    for index, prompt in enumerate(prompts):
        print("-" * 20)
        print(f"{index+1} - Running agent for prompt: {prompt}")
        async for message in agent.invoke(prompt):
            print("\nAgent says:", message)

asyncio.run(main())




