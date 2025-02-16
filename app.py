import streamlit as st
import pandas as pd
from Utils.linkedInData import fetch_linkedInData
from datetime import datetime



# Streamlit UI
st.set_page_config(page_title="Startup Loan Assessment", layout="wide")

st.title("🔍 SME Agent")
st.write("Enter details to fetch startup insights.")

# User Inputsstre
company_name = st.text_input("🏢 Enter Company Name", "")
company_siren = st.text_input("🏢 Enter Company SIREN", "")
loan_amount= st.text_input("💰 Enter Loan Amount in K$", "")
company_url = st.text_input("🔗 Company LinkedIn Profile URL", "")
founders_urls = st.text_area("👤 Enter LinkedIn URLs of Founders (comma-separated)", "")
open_banking_auth = st.text_input("🔑 Open Banking Auth (API Key or Token)", type="password")

if st.button("Fetch Data"):
    if company_name and company_url and founders_urls:
        # Process input
        founders_list = [url.strip() for url in founders_urls.split(",")]

        # Fetch data
        returned_data = fetch_linkedInData(company_name, company_url, founders_list)

        # Display results
        #st.subheader(f"📊 LinkedIn Data for {company_name}")
        #df = pd.DataFrame(list(returned_data.items()), columns=["Attribute", "Value"])
        #st.table(df)
        company_legalform =""

        st.markdown(f"""
                    ## Comprehensive Business Loan Assessment Report

**Generated on:** {datetime.now().strftime("%B, %d %Y")}

### Loan Details
- **Loan Amount:** ${loan_amount},000
- **Risk Rating:** A+
                    

"""
        )
        st.markdown("""

## 🎯 Executive Summary

| Metric     	| Value      	| Icon |
|---------------|---------------|------|
| Annual Revenue | $1.2M     	| 💰  |
| YoY Growth	| 22%       	| 📈  |
| Team Size 	| 25 Employees  | 👥  |
""")
        st.markdown(f"""
## 🐔 Business Information

### **Company Overview**
- **Company Name:** {company_name} 
- **SIREN:** {company_siren}  
- **Legal Form:** {company_legalform}  
- **Incorporation Date:** March 7, 2024  
- **Registered Address:** 229 Rue Saint-Honoré, 75001 Paris, France  
- **Business Activity:** IT Consulting (NAF Code: 62.02A – "Conseil en systèmes et logiciels informatiques")  
- **Capital:** €2,000  
- **Employee Count:** 0 (As of 2025, suggesting early-stage operations)  
- **Economic Sector:** IT Consulting & Software Advisory  
- **Legal Status:** Active, not ceased  
- **Annual Revenue & Profit:** Not reported  
- **Social & Solidarity Economy Status:** No  
""")
        
        returned_data = fetch_linkedInData(company_name, company_url, founders_list)
        st.title("🔍 Due Diligence Questions")

        # Iterate through founders and display their details
        for founder in returned_data["founders"]:
            st.subheader(f"👤 {founder['name']}")

            for detail in founder["details"]:
                st.markdown(f"**- {detail['question']}**  \n**Answer:** {detail['answer']}  \n")

            st.markdown("---")
        
        st.markdown("""
### **Crunchbase**
- **What is the total equity funding raised (USD)?**  
  **Answer:** $2.5M.  
- **Time since last raise?**  
  **Answer:** 18 months ago.  
- **How many unique investors (VCs, angels, corporates) have backed the company?**  
  **Answer:** 8 unique investors.  
- **Has the company participated in accelerators/incubators (e.g., Y Combinator)?**  
  **Answer:** Yes, Y Combinator W21 Batch Graduate.  
- **How many employees does the company have?**  
  **Answer:** 25 employees.  
"""
        )
        st.markdown("""
### **KYB (Know Your Business)**
- **Pappers**  
  - **Forme juridique:** SAS (Société par Actions Simplifiée).  
  - **Activity field:** IT Consulting & Software Advisory.  
  - **Company start date:** March 7, 2024.  
  - **Dirigeants:** Sarah Chen (CEO).  

### **Transaction History (TrueLayer for Open Banking)**
- **Money In (amount, frequency):**  
  - **Average Monthly Inflow:** $92,500.  
  - **Frequency:** Consistent, with peaks in Q4.  
- **Money Out:**  
  - **Average Monthly Outflow:** $69,800.  
- **Any Overdraft?**  
  - **Answer:** No overdrafts in the past 12 months.  

### **Market Data: Sector Performance (Linkup)**
- **Sector Growth Rate (2024):** 8.5% YoY.  
- **Company Growth Rate (2024):** 18% YoY (outperforming the sector).  
- **Market Share:** 2.5% in the cloud solutions niche.  

"""
                    )

        # Download option
        st.download_button(
            label="Download Data as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name=f"{company_name}_data.csv",
            mime="text/csv",
        )
    else:
        st.warning("⚠️ Please enter all required details!")
