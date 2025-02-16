import streamlit as st
import pandas as pd

# Dummy function to simulate data fetching
def fetch_linkedin_data(company_name, company_url, founders_urls):
    return {
        "Company Name": company_name,
        "LinkedIn URL": company_url,
        "Founders": founders_urls,
        "Industry": "Tech",
        "Employees": "50-100",
        "CEO": "John Doe",
        "Founded Year": "2018",
        "Headquarters": "San Francisco, CA",
        "LinkedIn Followers": "10,000",
        "Recent Hiring": "Yes",
        "Public Activity Level": "High",
    }

# Streamlit UI
st.set_page_config(page_title="Startup Loan Assessment", layout="wide")

st.title("🔍 SME Agent")
st.write("Enter details to fetch startup insights.")

# User Inputs
company_name = st.text_input("🏢 Enter Company Name", "")
company_siren = st.text_input("🏢 Enter Company SIREN", "")
company_url = st.text_input("🔗 Company LinkedIn Profile URL", "")
founders_urls = st.text_area("👤 Enter LinkedIn URLs of Founders (comma-separated)", "")
open_banking_auth = st.text_input("🔑 Open Banking Auth (API Key or Token)", type="password")

if st.button("Fetch Data"):
    if company_name and company_url and founders_urls:
        # Process input
        founders_list = [url.strip() for url in founders_urls.split(",")]

        # Fetch data
        linkedin_data = fetch_linkedin_data(company_name, company_url, founders_list)

        # Display results
        st.subheader(f"📊 LinkedIn Data for {company_name}")
        df = pd.DataFrame(list(linkedin_data.items()), columns=["Attribute", "Value"])
        st.table(df)

        # Download option
        st.download_button(
            label="Download Data as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"{company_name}_data.csv",
            mime="text/csv",
        )
    else:
        st.warning("⚠️ Please enter all required details!")
