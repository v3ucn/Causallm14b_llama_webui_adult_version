from llama_cpp import Llama
llm = Llama(
      model_path="./mymodel/causallm_14b-dpo-alpha.Q3_K_M.gguf",
      chat_format="llama-2"
)
res = llm.create_chat_completion(
      messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {
              "role": "user",
              "content": "来一段金瓶梅风格的情色小说，100字"
          }
      ],stream=True
)

for chunk in res:
    try:
        print(chunk['choices'][0]["delta"]['content'])
    except Exception as e:
        print(str(e))
        pass


# print(res['choices'][0]['message']['content'])