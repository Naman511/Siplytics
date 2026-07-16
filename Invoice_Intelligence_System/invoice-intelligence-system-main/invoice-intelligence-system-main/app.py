import streamlit as st
import time
from inference.predict_freight import predict_freight_cost
from inference.predict_invoice_flag import predict_invoice_flag

# -----------------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Vendor Intelligence Portal",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* Main Background & Padding */
    .stApp {
        background-color: #0E1117;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Header Styling */
    h1, h2, h3 {
        color: #1E90FF !important;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0A192F !important;
        border-right: 1px solid #1E90FF;
    }

    /* Primary Buttons */
    div.stButton > button:first-child {
        background-color: #1E90FF;
        color: white;
        border-radius: 8px;
        border: none;
        box-shadow: 0 4px 14px 0 rgba(30,144,255,0.39);
        transition: all 0.3s ease;
        width: 100%;
        height: 3em;
        font-weight: 600;
        letter-spacing: 0.5px;
    }

    div.stButton > button:hover {
        background-color: #2b65ec;
        color: white;
        box-shadow: 0 6px 20px rgba(30,144,255,0.6);
        transform: translateY(-2px);
    }

    /* Metric Value Focus */
    [data-testid="stMetricValue"] {
        color: #1E90FF;
        font-weight: 800;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚙️ Control Panel")
    
    app_mode = st.radio(
        "Navigation",
        ["Freight Prediction", "Risk Analysis"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.info(
        """
        **Intelligence Metrics**
        - 🚀 Logistics Optimization
        - 🛡️ Fraud Guard AI
        - 📊 Financial Precision
        """
    )

# -----------------------------------------------------------------------------
# MAIN HEADER
# -----------------------------------------------------------------------------
st.title("🏢 Vendor Intelligence Portal")
st.markdown("#### *AI-powered decision support for finance and logistics.*")
st.divider()

# =============================================================================
# FREIGHT PREDICTION
# =============================================================================
if app_mode == "Freight Prediction":

    st.subheader("📦 Forecast Freight Expenditure")
    
    # Input Card
    with st.container(border=True):
        st.markdown("**Input Parameters**")
        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "Item Quantity",
                min_value=1,
                value=10,
                help="Total number of items being shipped."
            )

        with col2:
            dollars = st.number_input(
                "Invoice Total ($)",
                min_value=1.0,
                value=500.0,
                step=10.0,
                help="The total monetary value of the invoice."
            )

    st.write("") # Spacer

    if st.button("✨ Calculate Expected Freight"):
        
        input_data = {
            "Quantity": [quantity],
            "Dollars": [dollars],
        }

        with st.spinner("Analyzing shipping patterns..."):
            try:
                result_df = predict_freight_cost(input_data)

                if result_df is not None and not result_df.empty:
                    prediction = result_df["Predicted_Freight"].iloc[0]

                    # Results Card
                    with st.container(border=True):
                        st.metric(
                            label="Calculated Freight Cost",
                            value=f"${prediction:,.2f}",
                            delta="Optimal route selected"
                        )
                    st.success("Prediction completed successfully.")

                else:
                    st.error("No prediction was returned. Please check the model backend.")

            except Exception as e:
                st.error(f"Prediction failed.\n\nError details: `{e}`")

# =============================================================================
# RISK ANALYSIS
# =============================================================================
elif app_mode == "Risk Analysis":

    st.subheader("🚩 Invoice Risk Profiler")

    # Input Card
    with st.container(border=True):
        st.markdown("**Invoice Details**")
        col1, col2 = st.columns(2)

        with col1:
            inv_qty = st.number_input(
                "Invoice Quantity",
                min_value=1,
                value=50,
                help="Total quantity claimed on the invoice."
            )

            inv_dollars = st.number_input(
                "Invoice Dollars ($)",
                min_value=1.0,
                value=1200.0,
                step=50.0,
                help="Total amount claimed on the invoice."
            )

            freight = st.number_input(
                "Freight Component ($)",
                min_value=0.0,
                value=45.0,
                step=5.0,
                help="Amount allocated specifically to freight."
            )

        with col2:
            item_qty = st.number_input(
                "Total Item Quantity",
                min_value=1,
                value=50,
                help="Actual item quantity received/documented."
            )

            item_dollars = st.number_input(
                "Total Item Dollars ($)",
                min_value=1.0,
                value=1195.0,
                step=50.0,
                help="Actual documented value of the items."
            )

    st.write("") # Spacer

    if st.button("🔍 Run AI Risk Assessment"):

        input_data = {
            "invoice_quantity": [inv_qty],
            "invoice_dollars": [inv_dollars],
            "Freight": [freight],
            "total_item_quantity": [item_qty],
            "total_item_dollars": [item_dollars],
        }

        with st.spinner("Scanning for anomalies..."):
            try:
                result_df = predict_invoice_flag(input_data)

                if result_df is not None and not result_df.empty:
                    prediction = result_df["Predicted_Flag"].iloc[0]

                    # Results Card
                    with st.container(border=True):
                        if prediction == 1:
                            st.error("### 🚨 HIGH RISK\nManual review required before processing. Significant discrepancies detected.")
                        else:
                            st.success("### ✅ LOW RISK\nInvoice cleared for automated processing. No major anomalies found.")

                else:
                    st.error("No prediction was returned. Please check the model backend.")

            except Exception as e:
                st.error(f"Risk assessment failed.\n\nError details: `{e}`")