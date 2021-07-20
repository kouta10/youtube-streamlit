import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プログレスバー')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

for j in range(4):
    expander = st.beta_expander('問い合わせ')
    for i in range(4):   
        expander.write('問い合わせ内容を書く')


