# グラフの表示
import streamlit as st
import pandas as pd
import numpy as np


def main():
    data ={
        "x":np.random.random(20),
        "y":np.random.random(20)-0.5,
        "z":np.random.random(20)-1
    }
    df = pd.DataFrame(data)
    # 折れ線グラフ
    st.subheader("折れ線グラフ")
    st.line_chart(df)
    # エリアチャート
    st.subheader("エリアチャート")
    st.area_chart(df)
    # バーチャート
    st.subheader("バーチャート")
    st.bar_chart(df)

    st.button("更新")


if __name__ == "__main__":
    main()











