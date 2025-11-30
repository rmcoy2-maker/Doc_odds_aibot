# ---- FORCE real project root on sys.path ----
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from datetime import datetime
import importlib

def load_page(modname: str):
    try:
        return importlib.import_module(modname)
    except Exception as e:
        st.error(f"❌ Failed to load `{modname}`: {e}")
        return None

def draw_sidebar():
    st.sidebar.title("📊 Edge Finder Navigation")

    pages = {
        "🏠 Home": "00_Home",
        "📈 Edge Scanner": "10_Edge_Scanner",
        "📊 Markets Explorer": "30_Markets_Explorer",
        "🧮 Micro Calculations": "12_Micro_Calculations",
        "📚 Reports": "21_Reports",
        "📉 Settled": "20_Settled",
        "📖 Your Log": "13_Your_Log",
        "📜 History": "14_Your_History",
        "🧪 Diagnostics": "98_Diagnostics",
        "🧪 Settle Diagnostics": "97_Settle_Diagnostics",
        "🧠 Models Browser": "95_Models_Browser",
        "🧮 Hedge Finder": "11_Hedge_Finder",
        "📈 Parlay Builder": "05_Parlay_Builder",
        "🧩 Ghost Parlay Calculator": "06_Ghost_Parlay_Calc",
        "🏦 Bankroll Tracker": "04_Bankroll_Tracker",
        "⚙️ All Picks Explorer": "09_All_Picks_Explorer",
        "📉 Lines Explorer": "09_Lines_Explorer",
        "📊 Analytics Hub": "09_Analytics_Hub",
        "🗃️ Reports Hub": "22_Reports_Hub",
        "📡 Doc Odds Live Board": "23_Doc_Odds_Live_Board",
        "🔐 Login": "00_Login",
        "📘 User Manual": "02_User_Manual",
        "⚖️ Legal / Privacy": "94_Legal_Terms_Privacy",
    }

    choice = st.sidebar.radio("Pages:", list(pages.keys()))
    return pages[choice]

def run_selected_page(module_name: str):
    if module_name in ("00_Home", __name__):
        draw_homepage()
    else:
        mod = load_page(module_name)
        if mod and hasattr(mod, "app"):
            mod.app()
        else:
            st.write("⚠️ No app() function found in this module.")

def draw_homepage():
    st.title("🏆 **DOC ODDS • EDGE FINDER**")
    st.markdown(
        "### Your Home Base for All CR Tools
"
        "Powered by Calculated Risk™ — accuracy, discipline, and clarity."
    )

    st.info(
        "Use the left sidebar to explore markets, run reports, build parlays, "
        "scan edges, or analyze historical performance."
    )

    st.markdown("---")

    st.header("🚀 Quick Launch")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📈 Edge Scanner"):
            switch_page("10_Edge_Scanner")

    with col2:
        if st.button("🏦 Bankroll Tracker"):
            switch_page("04_Bankroll_Tracker")

    with col3:
        if st.button("🧩 Parlay Builder"):
            switch_page("05_Parlay_Builder")

    st.markdown("---")
    st.caption(f"© {datetime.now().year} Doc Odds • Calculated Risk")

def app():
    module = draw_sidebar()
    run_selected_page(module)

if __name__ == "__main__":
    try:
        app()
    except:
        st.set_page_config(page_title="Doc Odds • Home", layout="wide")
        def _dummy(): pass
