import streamlit as st
import pandas as pd

# Sample CSV loader (replace with actual file or upload)
@st.cache_data

def load_data():
    df = pd.read_csv("LargeSalesData.csv")
    return df

st.title("📊 다단계 필터 우선순위 지정 툴")
df = load_data()

# User selects filter steps
st.sidebar.header("🔧 필터 설정 (우선순위 순서로 적용)")

step1_col = st.sidebar.selectbox("1단계 필터 열", df.columns, key="step1_col")
step1_val = st.sidebar.multiselect(f"1단계 {step1_col} 필터 값 선택", df[step1_col].unique(), key="step1_val")

step2_col = st.sidebar.selectbox("2단계 필터 열", df.columns, key="step2_col")
step2_val = st.sidebar.multiselect(f"2단계 {step2_col} 필터 값 선택", df[step2_col].unique(), key="step2_val")

# Apply step-by-step filters
filtered_df = df[df[step1_col].isin(step1_val)]
filtered_df = filtered_df[filtered_df[step2_col].isin(step2_val)]

st.markdown(f"### 🔍 필터링 결과 (총 {len(filtered_df)}행)")
st.dataframe(filtered_df.head(100))

# Download option
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 결과 CSV 다운로드", csv, "filtered_result.csv", "text/csv")
