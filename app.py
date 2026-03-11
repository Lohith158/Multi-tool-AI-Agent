from agent import executer
import gradio as gr


def chat(message, history):
    result = executer.invoke({"input": message})
    return result["output"]

interface = gr.ChatInterface(chat)
interface.launch()