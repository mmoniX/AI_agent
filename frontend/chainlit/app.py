import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    cl.user_session.set("message_history", [])
    await cl.Message(
        content="Welcome to Deep Research Agent. I can search the web, scrape pages, and synthesize research on any topic."
    ).send()


async def get_agent_response(content: str, message_history: list) -> str:
    # TODO: wire in agent (Pydantic AI / LangChain / custom)
    return f"Echo: {content}"


@cl.on_message
async def on_message(message: cl.Message):
    history: list = cl.user_session.get("message_history")
    response = await get_agent_response(message.content, history)
    history.append({"role": "user", "content": message.content})
    history.append({"role": "assistant", "content": response})
    cl.user_session.set("message_history", history)
    await cl.Message(content=response).send()
