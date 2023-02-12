
import streamlit as st
import openai
import os

# 設置 OpenAI API 金鑰
openai.api_key = os.environ["OPENAI_API_KEY"]

MODELS = {
    "text-davinci-003": "davinci",
    "text-curie-001": "curie",
    "text-babbage-001": "babbage",
    "text-ada-001": "ada"
}

# 定義翻譯函數
def translate(model, text):
    response = openai.Completion.create(
        engine=model,
        prompt=f"Translate to English: {text}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text


# 主要的 Streamlit 程式
st.title("OpenAI GPT Translation Example")

text = st.text_input("Enter text to translate:")

if text:
    # 顯示結果的表格
    results = []
    for model_name, model in MODELS.items():
        result = translate(model, text)
        results.append([model_name, result])

    st.table(results, header=["Model Name", "Translation Result"])