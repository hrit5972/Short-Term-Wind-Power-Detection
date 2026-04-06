import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time
import gdown
import os
import pickle

# -----------------------------------
# MODEL LOADING (CORRECT ORDER)
# -----------------------------------
@st.cache_resource
def load_model():
    MODEL_PATH = "wind_model.pkl"

    # Download if not exists
    if not os.path.exists(MODEL_PATH):
        file_id = "1GgeP15Bp0ncts-7LpMAWyhX8_TiPdjr6"
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        gdown.download(url, MODEL_PATH, quiet=False)

    # Load model AFTER download
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)

    return model

model = load_model()

st.success("✅ Model loaded successfully!")

# -----------------------------------
# BACKGROUND FUNCTION
# -----------------------------------
def set_bg(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("{url}");
            background-size: cover !important;
            background-position: center !important;
            background-attachment: fixed !important;
        }}
        h1 {{
            text-align: center !important;
            width: 100%;
        }}
        h1, h2, h3, p, span, label {{
            color: white !important;
            font-weight: 500 !important;
        }}
        .stButton>button {{
            background-color: #ffffff33 !important;
            color: white !important;
            border: 1px solid white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------------
# IMAGES
# -----------------------------------
IMG_STARTUP = "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?q=80&w=1500"
IMG_NORMAL = "https://images.unsplash.com/photo-1500382017468-9049fed747ef?q=80&w=1500"
IMG_STORM = "https://images.unsplash.com/photo-1605727216801-e27ce1d0cc28?q=80&w=1500"
IMG_CALM = "https://images.unsplash.com/photo-1470770841072-f978cf4d019e?q=80&w=1500"

# -----------------------------------
# HEADER
# -----------------------------------
st.markdown("<h1>🌬️ Wind Power Forecasting System</h1>", unsafe_allow_html=True)

# -----------------------------------
# LAYOUT
# -----------------------------------
col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.header("Input Parameters")
    ws = st.slider("Wind Speed (m/s)", 0.0, 30.0, 12.0)
    wd = st.slider("Wind Direction (°)", 0.0, 360.0, 180.0)
    temp = st.number_input("Temperature (°C)", value=25.0)
    gen_rpm = st.number_input("Generator RPM", value=1200.0)
    rotor_rpm = st.number_input("Rotor RPM", value=15.0)
    predict_btn = st.button("Calculate Prediction")

# -----------------------------------
# INITIAL STATE
# -----------------------------------
if not predict_btn:
    set_bg(IMG_STARTUP)
    with col2:
        st.subheader("Live Prediction Analysis")
        st.info("Adjust parameters and click calculate.")

# -----------------------------------
# PREDICTION LOGIC
# -----------------------------------
with col2:
    if predict_btn:
        with st.spinner('⚡ Calculating...'):
            time.sleep(0.5)

            features = np.array([[ws, wd, temp, gen_rpm, rotor_rpm]])
            prediction = model.predict(features)[0]

            if ws > 25.0:
                set_bg(IMG_STORM)
                st.error("⚠️ **STORM CONDITION DETECTED**")
                bar_color = "red"

            elif ws < 3.0:
                set_bg(IMG_CALM)
                st.info("📉 **LOW WIND CONDITION**")
                prediction = 0.0
                bar_color = "lightgray"

            else:
                set_bg(IMG_NORMAL)
                st.success("✅ **NORMAL OPERATING CONDITIONS**")
                bar_color = "royalblue"
                st.toast('Calculation Success!', icon='⚡')

        # -----------------------------------
        # GAUGE CHART
        # -----------------------------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            gauge={
                'axis': {'range': [None, 3500], 'tickcolor': "white"},
                'bar': {'color': bar_color},
                'bgcolor': "rgba(255,255,255,0.1)"
            },
            title={'text': "Predicted Active Power (kW)", 'font': {'color': "white"}}
        ))

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={'color': "white"}
        )

        st.plotly_chart(fig)