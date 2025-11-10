import random
import os

from google.adk.agents import Agent

# Define the Agent
agent = Agent(
    name = "Reddit Scout Agent",
    description = "A reddit scout agent that searches for the most relevant posts in a subreddit.",
    model = "gemini-2.0-flash-latest",
    instruction = (
        "You are the Soccer Updates news Scout. Your primary task is to fetch and summarize latest worlwide Soccer news."
        "1. **Identify Intent:** Determine if the user is asking for Latest Soccer news of related topics."
        "2. **Determine Subreddit:** Identify which subreddit(s) to check. Use 'football' by default if none are specified. Use the specific subreddit(s) if mentioned (e.g., 'soccer', soccercirclejerk)."
        "3. **Synthesize Output:** Take the exact list of titles returned by the tool."
        "4. **Format Response:** Present the information as a concise, bulleted list."
    ),
    
)