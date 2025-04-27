import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go

@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    return fund_model, tech_model

def main():
    st.title("🤖 Model & Rating Explanation")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    fund_weight = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight = 100 - fund_weight
    st.write(f"**Fundamental:** {fund_weight}%   |   **Technical:** {tech_weight}%")

    if st.button("Explain Models & Rating"):
        st.info("Running models and extracting explanations…")

        fund_model, tech_model = load_models()

        # use same feature simulation as page1
        # (or pull real data exactly as above)
        # For brevity, we’ll just simulate here:
        fund_num_cols = [ ... ]    # same list as in page1
        tech_num_cols = [ ... ]    # same list as in page1
        df_f = pd.DataFrame([np.random.rand(len(fund_num_cols))], columns=fund_num_cols)
        df_f['gics_sector_x'] = 'Information Technology'
        df_t = pd.DataFrame([np.random.rand(len(tech_num_cols))], columns=tech_num_cols)
        df_t['gics_sector_x'] = 'Information Technology'

        fund_score = fund_model.predict(df_f)[0]
        tech_score = tech_model.predict(df_t)[0]
        final_score = (fund_score * fund_weight/100) + (tech_score * tech_weight/100)
        final_score = np.clip(final_score, 0, 10)

        st.subheader("📈 Rating Breakdown")
        st.write(f"- Fundamental Score: **{fund_score:.2f}**")
        st.write(f"- Technical Score: **{tech_score:.2f}**")
        st.write(f"- **Combined Investment Rating: {final_score:.2f} / 10** (higher = safer)")

        # Feature importances (if available)
        st.subheader("🔎 Feature Importances")
        if hasattr(fund_model, "feature_importances_"):
            imp = fund_model.feature_importances_
            df_imp = pd.DataFrame({
                "feature": fund_num_cols,
                "importance": imp[:len(fund_num_cols)]
            }).sort_values("importance", ascending=False)
            fig = go.Figure(go.Bar(
                x=df_imp["importance"],
                y=df_imp["feature"],
                orientation="h",
                text=df_imp["importance"].map(lambda v: f"{v:.3f}"),
                textposition="auto"
            ))
            fig.update_layout(
                title="Fundamental Model Importances",
                yaxis_title="",
                margin=dict(l=150)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Fundamental model does not expose `feature_importances_`.")

        if hasattr(tech_model, "feature_importances_"):
            imp = tech_model.feature_importances_
            df_imp = pd.DataFrame({
                "feature": tech_num_cols,
                "importance": imp[:len(tech_num_cols)]
            }).sort_values("importance", ascending=False)
            fig = go.Figure(go.Bar(
                x=df_imp["importance"],
                y=df_imp["feature"],
                orientation="h",
                text=df_imp["importance"].map(lambda v: f"{v:.3f}"),
                textposition="auto"
            ))
            fig.update_layout(
                title="Technical Model Importances",
                yaxis_title="",
                margin=dict(l=150)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Technical model does not expose `feature_importances_`.")

if __name__ == "__main__":
    main()
