import streamlit as st
import requests

st.title('じゃんけんゲーム')

user_choice = st.selectbox('あなたの手を選んでください', ['グー', 'チョキ', 'パー'])

if st.button('勝負する'):
    response = requests.post("https://janken-4tcx.onrender.com/janken", json={"user_choice": user_choice})
    if response.status_code == 200:
        result = response.json()
        st.write(f"あなたの選択: {result['user_choice']}")
        st.write(f"コンピュータの選択: {result['computer_choice']}")
        st.write(f"結果: {result['result']}")
    else:
        st.write("エラーが発生しました。もう一度試してください。")
