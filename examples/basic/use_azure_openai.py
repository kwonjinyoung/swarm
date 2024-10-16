from swarm import Swarm, Agent
from openai import AzureOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# AZURE_OPENAI_API_KEY="..."
os.environ["AZURE_OPENAI_API_KEY"] = os.getenv("AZURE_OPENAI_API_KEY")
# OPENAI_API_VERSION="2024-02-15-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv("AZURE_OPENAI_ENDPOINT")
# AZURE_OPENAI_ENDPOINT="https://your.openai.azure.com/"
os.environ["OPENAI_API_VERSION"] = os.getenv("OPENAI_API_VERSION")
azure_deployment = "your_azure_deployment"

azureClient = AzureOpenAI(azure_deployment=azure_deployment)
client = Swarm(client=azureClient)

agent = Agent(
    name="Agent",
    instructions="You are a helpful agent.",
)

messages = [{"role": "user", "content": "Hi!"}]
response = client.run(agent=agent, messages=messages)

print(response.messages[-1]["content"])
