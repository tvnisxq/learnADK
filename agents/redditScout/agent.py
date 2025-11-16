import random
import os
from dotenv import load_dotenv

from google.adk.agents import Agent

# Load environment variables from .env file
load_dotenv()

# from praw.exceptions import PrawExceptions
def get_mock_reddit_soccer_news(subreddit:str) -> dict[str, list[str]]:
    """
    Simulates fetching top post titles from a soccer reddit 
    
    Args:
        subreddit: The name of the subreddit to fetch news from(e.g., 'soccercirclejerk').
    
    Returns:
        A dictionary with the subreddit name as the key and a list of mock
        psot titles as value. Returns a message if the subreddit is unknown.
    """
    print(f"----Tool called: Simulating fetch from r/{subreddit} ----")
    mock_titles = {

        "football": [
            "Week 10 recap: Underdog team shocks league with last-second field goal",
            "Veteran QB announces retirement: 'This game gave me everything'",
            "Top 5 breakout players halfway through the season",
            "League approves radical new kickoff rule starting next season",
            "Analysts say this could be the most unpredictable playoff race in years",
        ],
        "soccer": [
            "Transfer market update: Premier League club prepares €120M bid for star winger",
            "UCL match ends 4–4 in historic comeback as fans lose their minds",
            "Team announces new manager after sacking coach mid-season",
            "FIFA reveals expanded Club World Cup format for 2025",
            "VAR controversy trends worldwide after disallowed goal sparks outrage",
        ],
        "sports": [
            "Historic night: Triple-header sees three comebacks in three different leagues",
            "Sports scientists claim AI analytics could replace traditional scouting",
            "New CBA deal reached: salary cap increases and rule changes incoming",
            "Documentary series exposes toxic culture inside major sports organization",
            "Fans react as legendary athlete announces comeback after 3-year hiatus",
        ],
        "soccercirclejerk": [
            "BREAKING: Referee consults VAR to check if the vibes were off before calling foul",
            "Club announces 'new era' after losing 7–0... again",
            "Official: Player banned for 'excessively celebrating while being 5–0 down'",
            "Rumors say new FIFA patch will nerf long shots and buff slide tackles",
            "Fans demand apology after team completes 200 backwards passes in a row",
        ],
    }

    # Normalize subreddit name for lookup
    normalized_subreddit = subreddit.lower()

    if normalized_subreddit in mock_titles:
        available_titles = mock_titles[normalized_subreddit]

        # Return a random subset to make it seem dynamic
        num_to_return = min(len(available_titles), 3) # return upto 3 titles
        selected_titles = random.sample(available_titles, num_to_return)
        return {subreddit: selected_titles}
    
    else:
        print(f"---- Tool Warning: Unknown Subreddit: '{subreddit}' requested. ----")
        return {subreddit: f"Sorry! I don't have mock data for r/{subreddit}."}
    

# Define the Agent
root_agent = Agent(
    name = "reddit_scout_agent",
    description = "A reddit scout agent that searches for the most relevant posts in a subreddit.",
    model = "gemini-2.0-flash",
    instruction = (
        "You are the Soccer Updates news Scout. Your primary task is to fetch and summarize latest worlwide Soccer news."
        "1. **Identify Intent:** Determine if the user is asking for Latest Soccer news of related topics."
        "2. **Determine Subreddit:** Identify which subreddit(s) to check. Use 'soccerl' by default if none are specified. Use the specific subreddit(s) if mentioned (e.g., 'football', 'soccer', 'sports', 'soccercirclejerk')."
        "3. **Synthesize Output:** Take the exact list of titles returned by the tool."
        "4. **Format Response:** Present the information as a concise, bulleted list. Clearly state which subreddit(s) the information came from. If the tool indicates an error or an unknown reddit, report that message directly to the user."
        "5. **MUST CALL TOOL:** You must call the 'get_mock_reddit_soccer_news' tool with the identified subreddit(s). Do NOT generate summaries without calling the tool first."
    ),
    tools = [get_mock_reddit_soccer_news],
    
)