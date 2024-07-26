import streamlit as st

# ---- Pages
st.write('deneme')
about_page = st.Page(
    page="views/about.py",
    title="About",
    icon=":material/account_circle:",
    default=True,
)
chatbot_page= st.Page(
    page="views/chatbot.py",
    title="Chat wit Contracts",
    icon=":material/smart_toy:"
)
contract_page= st.Page(
    page="views/contract_create.py",
    title="Create Contract",
    icon=":material/smart_toy:"
)

template_page= st.Page(
    page="views/contract_fill.py",
    title="Create Contract from Template",
    icon=":material/smart_toy:"
)

dashboard_page= st.Page(
    page="views/service_dashboard.py",
    icon=":material/bar_chart:",
)

# Page Navigation
# pg = st.navigation(pages=[about_page, chatbot_page, dashboard_page])
pg = st.navigation(
    {
    "info" : [about_page],
    "Services": [contract_page,template_page,chatbot_page, dashboard_page]
    }
)

# Shared on all pages
st.logo("assets/papir_logo.png")
st.sidebar.text("Papir.ai Services")
# Run Navigation
pg.run()
