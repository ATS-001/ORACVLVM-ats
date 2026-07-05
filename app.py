import streamlit as st
import joblib
import numpy as np

# 1. Clear CSS injection: ONLY hides Streamlit branding and updates input/button text cleanly
custom_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            .stAppDeployDropdown {display: none;}
            
            /* Apply Courier New ONLY to form numeric inputs, dropdown selectors, and sliders */
            input, select, button, div[data-testid="stMetricValue"] {
                font-family: 'Courier New', Courier, monospace !important;
            }
            </style>
            """

st.set_page_config(page_title="ORACVLVM: World Cup Forecaster", page_icon="🏆", layout="centered")
st.markdown(custom_style, unsafe_allow_html=True)

# 2. Session State Initialization for the clear buffer functionality
default_values = {
    'is_host': 0,
    'goals_scored': 70,
    'goals_received': 30,
    'participations': 10,
    'fifa_rank': 15,
    'fifa_points': 1600,
    'avg_age': 26.5,
    'market_value': 400000000
}

for key, val in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = val

def reset_inputs():
    for key, val in default_values.items():
        st.session_state[key] = val

try:
    model = joblib.load("world_cup_model.pkl")
except:
    model = None

# Re-styled Titles using inline Courier New to guarantee no widget layout breaks
st.markdown("<h1 style='font-family: \"Courier New\", Courier, monospace;'>🏆 ORACVLVM</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='font-family: \"Courier New\", Courier, monospace;'>FIFA World Cup Performance Forecaster</h3>", unsafe_allow_html=True)
st.markdown("<p style='font-family: \"Courier New\", Courier, monospace;'>Input custom team attributes to predict their statistical probability of reaching the Quarter-Finals.</p>", unsafe_allow_html=True)

# --- SYSTEM CONFIG & CREDITS REGISTRY DROPDOWNS (PLACED BELOW HEADER) ---
meta_col1, meta_col2 = st.columns(2)

with meta_col1:
    with st.expander("ℹ️ System Configuration", expanded=False):
        st.markdown("""
        **Architecture:** Retrieval-Augmented Generation (RAG)
        
        **LLM Hub:** Llama 3.3 70B via Groq pipeline
        
        **Vector Space:** Local FAISS Database
        
        *Note: Model Baseline Accuracy is 69.23%*
        """)

with meta_col2:
    with st.expander("🛠️ Credits Registry", expanded=False):
        st.markdown("""
        **Creator / Engineer:** Aaron Thalakkottor Sooraj
        
        <a href="https://github.com/ATS-001/-ORACVLVM-ats" target="_blank" style="text-decoration: none;">
                <div style='background-color: rgba(255, 255, 255, 0.05); padding: 8px 16px; border-radius: 4px; margin: 8px 0; border: 1px solid rgba(255, 255, 255, 0.1); width: fit-content; color: white; font-family: "Courier New", Courier, monospace; font-weight: bold; transition: 0.3s; cursor: pointer;' onmouseover="this.style.backgroundColor='rgba(255, 255, 255, 0.15)'" onmouseout="this.style.backgroundColor='rgba(255, 255, 255, 0.05)'">
                    📁  ORACVLVM Repo ↗
                </div>
            </a>
        
        **Project Baseline:** Day 6 of Projectathon conducted by μLearn LBSITW, AI x DS (3rd July 2026)
        
        **Presented By:** Aiswarya Jayaprakash, Data Science IG LEAD, µLearn LBSITW
                    
        **Data Attribution:** Historical stats & metrics courtesy of FIFA. Independent research project with no official affiliation.
    
        """, unsafe_allow_html=True)

st.markdown("---")

# 3. Main Form Inputs (Labels styled cleanly using inline Courier New formatting)
col1, col2 = st.columns(2)

with col1:
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Is the Team the Tournament Host?</label>", unsafe_allow_html=True)
    is_host = st.selectbox(
        "", 
        [0, 1], 
        index=[0, 1].index(st.session_state['is_host']),
        format_func=lambda x: "Yes" if x == 1 else "No",
        key='is_host_ui',
        label_visibility="collapsed"
    )
    st.session_state['is_host'] = is_host

    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Goals Scored (Last 4 Years)</label>", unsafe_allow_html=True)
    goals_scored = st.number_input("", min_value=0, max_value=250, value=st.session_state['goals_scored'], key='goals_scored', label_visibility="collapsed")
    
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Goals Conceded (Last 4 Years)</label>", unsafe_allow_html=True)
    goals_received = st.number_input("", min_value=0, max_value=250, value=st.session_state['goals_received'], key='goals_received', label_visibility="collapsed")
    
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Previous WC Participations</label>", unsafe_allow_html=True)
    participations = st.number_input("", min_value=0, max_value=25, value=st.session_state['participations'], key='participations', label_visibility="collapsed")

with col2:
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Current FIFA Rank</label>", unsafe_allow_html=True)
    fifa_rank = st.number_input("", min_value=1, max_value=210, value=st.session_state['fifa_rank'], key='fifa_rank', label_visibility="collapsed")
    
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>FIFA Points</label>", unsafe_allow_html=True)
    fifa_points = st.number_input("", min_value=100, max_value=2200, value=st.session_state['fifa_points'], key='fifa_points', label_visibility="collapsed")
    
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Squad Average Age</label>", unsafe_allow_html=True)
    avg_age = st.slider("", 18.0, 36.0, value=st.session_state['avg_age'], step=0.1, key='avg_age', label_visibility="collapsed")
    
    st.markdown("<label style='font-family: \"Courier New\", Courier, monospace; font-size: 14px; font-weight: bold;'>Total Squad Value (€)</label>", unsafe_allow_html=True)
    market_value = st.number_input("", min_value=0, value=st.session_state['market_value'], step=10000000, key='market_value', label_visibility="collapsed")

st.markdown("---")

# 4. Action Buffer Zone (Two buttons side by side)
btn_col1, btn_col2 = st.columns([3, 1])

with btn_col1:
    predict_clicked = st.button("Run Simulation Forecast", use_container_width=True, type="primary")

with btn_col2:
    if st.button("Clear Inputs", use_container_width=True, on_click=reset_inputs):
        st.rerun()

# Prediction Logic Output
if predict_clicked:
    if model is not None:
        input_data = [[
            st.session_state['is_host'], 
            st.session_state['goals_scored'], 
            st.session_state['goals_received'], 
            st.session_state['market_value'], 
            st.session_state['fifa_rank'], 
            st.session_state['fifa_points'], 
            st.session_state['avg_age'], 
            st.session_state['participations']
        ]]
        
        prob = model.predict_proba(input_data)[0][1] 
        
        st.markdown(f"<p style='font-family: \"Courier New\", Courier, monospace; margin-bottom: 0;'>Probability of Reaching Quarter-Finals</p>", unsafe_allow_html=True)
        st.metric(label="", value=f"{prob:.1%}", label_visibility="collapsed")
        if prob > 0.5:
            st.success("🚀 This national squad profiles as a top tournament contender!")
        else:
            st.warning("⚠️ The model predicts a tougher route through the knockout phase for this setup.")
    else:
        st.error("Model file 'world_cup_model.pkl' not found. Please place it in this directory!")

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 5. Explicit Custom Footer
# 5. Explicit Custom Footer & IP Acknowledgement
st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 11px; font-family: 'Courier New', Courier, monospace; line-height: 1.6;">
        Developed by Aaron Thalakkottor Sooraj | Designed & Developed by ATS_PDZ | © 2026
        <br>
        <span style="font-size: 10px;">
            Disclaimer: This project is an independent research prototype developed for educational purposes. All product names, logos, and brands (including "FIFA", "FIFA World Cup", and national team designations) are property of their respective owners.
        </span>
    </div>
    """, 
    unsafe_allow_html=True
)