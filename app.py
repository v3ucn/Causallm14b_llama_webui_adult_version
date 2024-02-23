import argparse
import os
import gradio as gr
# import requests
from llama_cpp import Llama
from config import model_path

llm = Llama(
      model_path = model_path,
      chat_format = "llama-2",
      n_gpu_layers = 30
)


url = 'http://localhost:8000/v1/chat/completions'
headers = {
	'accept': 'application/json',
	'Content-Type': 'application/json'
}


def do_ask(text):

    res = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {
              "role": "user",
              "content": f"{text}"
          }
      ],
      stream = True
)
    all_text = ""
    for chunk in res:
        try:
            res = chunk['choices'][0]["delta"]['content']
            all_text += res
            yield all_text
        except Exception as e:
            print(str(e))
            pass

    

# def do_ask(text):

#     data = {
# 	'messages': [
# 		{
# 		'content': 'You are a helpful assistant.',
# 		'role': 'system'
# 		},
# 		{
# 		'content': f'{text}',
# 		'role': 'user'
# 		}
# 	]
#     }

#     response = requests.post(url, headers=headers, json=data)
#     print(response.json())
#     print(response.json()['choices'][0]['message']['content'])

#     return response.json()['choices'][0]['message']['content']


initial_md = """


webui作者：刘悦的技术博客  https://space.bilibili.com/3031494
模型作者：https://huggingface.co/tastypear/CausalLM-14B-DPO-alpha-GGUF

"""


with gr.Blocks() as app:
    gr.Markdown(initial_md)

    with gr.Accordion("对话输入"):
        with gr.Row():

            ori_video = gr.Textbox(label="请输入对话")
        
            speech_button = gr.Button("发送")

    
    
    
    with gr.Accordion("文本生成"):
        with gr.Row():
            with gr.Column():
                
                text = gr.Textbox()

    speech_button.click(do_ask,inputs=[ori_video],outputs=[text])

                
        

parser = argparse.ArgumentParser()
parser.add_argument(
    "--server-name",
    type=str,
    default=None,
    help="Server name for Gradio app",
)
parser.add_argument(
    "--no-autolaunch",
    action="store_true",
    default=False,
    help="Do not launch app automatically",
)
args = parser.parse_args()

app.launch(inbrowser=not args.no_autolaunch, server_name=args.server_name)
