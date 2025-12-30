from openai import AsyncOpenAI
import os
import logging
from dotenv import load_dotenv
load_dotenv()

logger = logging.getLogger(__name__)
api_key = os.getenv("openrouter")
if not api_key:
    logger.warning("OPENAI_API_KEY not set in environment")
    
client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

async def reply(message: str):
    try:
        response = await client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a helpful bot"},
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        logger.exception("Chat completion failed")
        return f"Error: {e}"


# print(response.output_text)