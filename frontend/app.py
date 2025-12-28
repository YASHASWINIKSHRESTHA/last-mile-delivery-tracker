import streamlit as st
import requests
import base64
from pathlib import Path

# ---------------- CONFIG ----------------
API_BASE = "http://localhost:8080/api/shipments"

st.set_page_config(
    page_title="Last Mile Delivery Tracker",
    layout="centered"
)

# ---------------- LOAD BACKGROUND IMAGE ----------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}

        /* Remove white containers */
        [data-testid="stAppViewContainer"] {{
            background: transparent;
        }}

        [data-testid="stHeader"] {{
            background: rgba(0,0,0,0);
        }}

        /* Main Card */
        .card {{
            background: rgba(0, 0, 0, 0.65);
            padding: 35px;
            border-radius: 20px;
            max-width: 520px;
            margin: auto;
            box-shadow: 0 25px 50px rgba(0,0,0,0.6);
        }}

        /* Labels */
        label {{
            color: #ffffff !important;
            font-weight: 600;
        }}

        /* Inputs */
        input {{
            background-color: rgba(255,255,255,0.15) !important;
            color: white !important;
            border-radius: 10px !important;
            border: 1px solid rgba(255,255,255,0.4) !important;
        }}

        input::placeholder {{
            color: #dddddd;
        }}

        /* Buttons */
        button {{
            width: 100%;
            padding: 12px !important;
            border-radius: 14px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
            background: linear-gradient(135deg, #00c6ff, #0072ff) !important;
            color: white !important;
            border: none !important;
            transition: all 0.25s ease;
        }}

        button:hover {{
            transform: scale(1.05);
            background: linear-gradient(135deg, #0072ff, #00c6ff) !important;
        }}

        /* Messages */
        .stSuccess, .stError, .stWarning {{
            border-radius: 12px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ APPLY BACKGROUND
set_bg("bg.jpg")

# ---------------- TITLE ----------------
st.markdown(
    """
    <div style="text-align:center; margin-bottom:30px;">
        <h1>📦 Last Mile Delivery Tracker</h1>
        <p style="color:#eeeeee; font-size:16px;">
            Track and complete deliveries securely using OTP
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CARD ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

shipment_id = st.text_input(
    "Shipment ID",
    placeholder="e.g. SHIP1766914906941"
)

otp = st.text_input(
    "OTP",
    placeholder="Enter delivery OTP",
    type="password"
)

col1, col2 = st.columns(2)

# ---------------- TRACK ----------------
with col1:
    if st.button("🔍 Track Shipment"):
        if not shipment_id:
            st.warning("Please enter Shipment ID")
        else:
            try:
                r = requests.get(f"{API_BASE}/{shipment_id}")
                if r.status_code == 200:
                    data = r.json()
                    st.success("Shipment Found ✅")
                    st.markdown(
                        f"""
                        <div style="background:rgba(255,255,255,0.15);
                                    padding:15px;
                                    border-radius:12px;
                                    margin-top:10px;">
                            <b>Status:</b> {data['status']} <br>
                            <b>Customer:</b> {data['customerName']} <br>
                            <b>Shipment ID:</b> {data['shipmentId']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error("Shipment not found ❌")
            except:
                st.error("Backend not reachable")

# ---------------- DELIVER ----------------
with col2:
    if st.button("✅ Deliver Shipment"):
        if not shipment_id or not otp:
            st.warning("Enter Shipment ID and OTP")
        else:
            try:
                r = requests.post(
                    f"{API_BASE}/{shipment_id}/deliver",
                    params={"otp": otp}
                )
                if r.status_code == 200:
                    data = r.json()
                    st.success("Delivery Completed 🎉")
                    st.markdown(
                        f"""
                        <div style="background:rgba(0,255,150,0.18);
                                    padding:15px;
                                    border-radius:12px;
                                    margin-top:10px;">
                            <b>Status:</b> {data['status']} <br>
                            <b>Delivered At:</b> {data['deliveredAt']}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                else:
                    st.error("Invalid OTP or already delivered ❌")
            except:
                st.error("Backend not reachable")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div style="text-align:center; margin-top:40px; color:#cccccc;">
        Built with Spring Boot + Streamlit 🚀
    </div>
    """,
    unsafe_allow_html=True
)
