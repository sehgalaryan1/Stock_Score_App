# Import Streamlit
import streamlit as st

# **** Page layout setup ****
App_page_0 = st.Page(
    "main.py",
    title="🏠 Home",
    default=True
)
App_page_1 = st.Page(
    "pages/2_Stock_Input.py",
    title="🔍 Stock Input & Score"
)
App_page_2 = st.Page(
    "pages/3_Technical_Analysis.py",
    title="📈 Technical Analysis"
)
App_page_3 = st.Page(
    "pages/4_Fundamentals.py",
    title="🧾 Fundamental Metrics"
)
App_page_4 = st.Page(
    "pages/5_Model_Insights.py",
    title="🤖 Model Insights"
)
App_page_5 = st.Page(
    "pages/6_Docs.py",
    title="📚 Documentation"
)

# **** Set up navigation with section headers ****
pg = st.navigation(
    {
        "Start Here":       [App_page_0],
        "Analysis":         [App_page_1, App_page_2, App_page_3],
        "Insights & Scores":[App_page_4],
        "Docs & About":     [App_page_5],
    }
)

# **** text/images shared on all pages ****
st.sidebar.markdown("📋 Use the menu above to jump between pages.")
