from webAgent.agent import reply
import chainlit as cl

cl.instrument_openai()

@cl.on_message
async def on_message(message: cl.Message):
    res = await reply(message.content)
    await cl.Message(content=res).send()