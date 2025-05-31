import asyncio
import os
import sys
import uuid
import json
import ast
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from dotenv import load_dotenv

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

from browser_use import Agent
from browser_use.browser import BrowserSession

from task_prompt_sample_webapp import task_sample_webapp
# from task_prompt_google_search import task_google_search

# unique_id = uuid.uuid4()
# datetime timestamp based unique id
unique_id = datetime.now().strftime("%Y%m%d-%H%M%S") 
print("Agent Run id: ", unique_id)

browser_session = BrowserSession(
    headless=False,
    slow_mo=1000,
    viewport={'width': 400, 'height': 400},
)

agent = Agent(
	task=task_sample_webapp,
    # task=task_google_search,
	llm=ChatGoogleGenerativeAI(model='gemini-2.0-flash-001', api_key=os.getenv('GEMINI_API_KEY')),
	browser_session=browser_session,
    # controller=custom_controller,  # For custom tool calling
    use_vision=True,              # Enable vision capabilities
    save_conversation_path=f"logs/run_{unique_id}/conversation"  # Save chat logs
)


async def main():
	# await agent.run()
    history = await agent.run()
    history.save_to_file(f"logs/run_{unique_id}/history.json")
    # save history final result to file
    with open(f"logs/run_{unique_id}/result.txt", "w") as f:
        f.write(history.final_result())
    input('Press Enter to close the browser...')
    await browser_session.close()


if __name__ == '__main__':
	asyncio.run(main())