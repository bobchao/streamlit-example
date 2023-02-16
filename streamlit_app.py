import streamlit as st
# import spacy
import openai
import os

# Setups
openai.api_key = os.environ["OPENAI_API_KEY"]
# nlp = spacy.load("en_core_web_sm")

# 顯示 textarea 用於輸入 OKR
o_input = st.text_input("請輸入 Objective：")
kr_input = st.text_area("請輸入 KRs，建議每個 KR 一行")

def aihelp(prompt_template):
    # Use OpenAI GPT to analyze the OKR and provide suggestions
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= prompt_template + "\n\n Objective: " + o_input + "\nKRs:\n\n" + kr_input,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    ).get("choices")[0].get("text")

    return response

# if st.button("分析 O"):
#    o_a = aihelp("這組 OKR 裡的 O 是好的 O 嗎，為什麼？")
#    st.write(o_a)

# if st.button("分析 KR"):
#    doc = nlp(okr_input)
#    st.write("您輸入的 KR 包括：")
#    for sent in doc.sents:
#        if "KR" in sent.text:
#            st.write(sent.text.strip())

#    o_a = aihelp("這組 OKR 裡的 KR 有什麼缺點")
#    suggestion_a = aihelp("請為這組 OKR 提供三組改寫建議")
#    st.write(o_a)
#    st.write("改寫建議")
#    st.write(suggestion_a)

col1, col2 = st.columns(2)

with col1:
    reviewO = st.button("改善 O")
    suggestKRs = st.button("建議備選 KR")
    improveO = st.button("以更積極的態度改寫 O")

with col2:
    reviewKR = st.button("改善 KR")
    


if reviewO:
    suggestion_a = aihelp("以 OKR 的理論來說，這個 Objective 可能有哪些缺點，可能該怎麼改善？")
    st.write(suggestion_a)

if suggestKRs:
    suggestion_a = aihelp("請為這個 Objective 建議 10 組可能的 Key results")
    st.write(suggestion_a)

if improveO:
    suggestion_a = aihelp("請將這個 Objective 以更積極的態度提供 5 種改寫版本")
    st.write(suggestion_a)

if reviewKR:
    suggestion_a = aihelp("以 OKR 的理論來說，這些 KR 可能有哪些缺點，可能該怎麼改善？（只要列出缺點與改善方式，不要額外解釋或衍生新 KR）")
    st.write(suggestion_a)