import os
import asyncio
from dotenv import load_dotenv

from semantic_kernel import <TODO> # import the Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, OpenAIChatPromptExecutionSettings
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.<TODO> import KernelArguments # add from where within SK to import the kernel arguments

# -----------------
# Load Environmental Variables
# -----------------
load_dotenv()

api_key = <TODO> # use os.getenv to get the AZURE OPENAI KEY
url = os.getenv("URL")
api_version = "2024-12-01-preview"

# -----------------
# Initialize the kernel
# -----------------
kernel = <TODO> # initialize the Kernel

# -----------------
# Define a chat service
# -----------------
deployment = <TODO> # use the gpt-4.1-mini  deployment

chat_service = AzureChatCompletion(
    deployment_name=deployment,
    api_key=<TODO> # assign the correct api key
    base_url=f"{url}<TODO>", # complete the url using the correct deployment name
    api_version=api_version
)

# -----------------
# Register the chat service in the kernel
# -----------------
kernel.<TODO> # add a chat service to the kernel

# -----------------
# Create agent using registered service
# -----------------
agent_instructions = """
    You are an expert in data analysis.
    You can answer any questions about how to analyse data, giving explanations on complex statistical analysis.
    You can not answer questions about any other subject
"""

settings = OpenAIChatPromptExecutionSettings()
settings.temperature = <TODO> # set the temperature such that the agent is very creative with its answers
settings.max_tokens = 300

agent = ChatCompletionAgent(
    service=<TODO> # and the appropriate service 
    name="SK-Assistant",
    instructions=agent_instructions,
    arguments=<TODO> # assign the corrent arguments
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
        <TODO> for message in agent.invoke(prompt): # run the agent in async mode
            print("\nAgent says:", message)

<TODO>.run(main()) # run the agent in async mode




