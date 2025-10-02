from google.adk.agents import Agent
from .prompt import VOICE_GENERATOR_DESCRIPTION, VOICE_GENERATOR_PROMPT
from google.adk.models.lite_llm import LiteLlm
from .tools import generate_narrations

MODEL = LiteLlm(model="openai/gpt-5")

voice_generator_agent = Agent(
    name="VoiceGeneratorAgent",
    description=VOICE_GENERATOR_DESCRIPTION,
    instruction=VOICE_GENERATOR_PROMPT,
    model=MODEL,
    tools=[
        generate_narrations,
    ],
)