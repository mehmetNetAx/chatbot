from dotenv import load_dotenv 
from openai import OpenAI
import streamlit as st



load_dotenv()
client = OpenAI()


def generate_contract(parties, addresses, cost, contract_type, subject, scope,payment_conditions):
    prompt = f"""
    Generate a contract between two parties.

    Party A: {parties[0]} residing at {addresses[0]}
    Party B: {parties[1]} residing at {addresses[1]}

    Contract Details:
    - Type: {contract_type}
    - Subject: {subject}
    - Scope: {scope}
    - Cost: ${cost}
    - Start Date : {startdate}
    - End Date : {enddate}
    

    Payment Conditions: {payment_conditions} prepare a table for the payment
    Termination Condition : {termination_period}  

    Include standard legal terms and conditions such as:
    - Confidentiality
    - Termination
    - Governing Law
    - Dispute Resolution
    - Entire Agreement
    """

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates legal contracts."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000,
        temperature=0.5
    )

    #contract = response.choices[0].message['content'].strip()
    contract = response.choices[0].message.content.strip()
    return contract


st.title("Papir.ai - Contract Generator")

party1_name = st.text_input("Party A Name","Ford Otomotiv")
party1_address = st.text_input("Party A Address","Ford Gebze")
party2_name = st.text_input("Party B Name","NETAX")
party2_address = st.text_input("Party B Address","Altunizade mah. Dadaslar Sok. No:23/7 Üsküdar - İstanbul")
cost = st.number_input("Cost of the Contract",min_value=100000)
payment_conditions = st.text_input("Payment Conditions:","%30 pre payment and the rest monthly payment during contract period")
contract_type = st.selectbox("Type of Contract", ["Service", "Goods", "Employment", "Lease", "Other"])
subject = st.text_input("Subject of the Contract","Gizlilik Sözleşmesi")
scope = st.text_area("Scope of the Contract", "Proje öncesi gizlilik sözleşmesi")
startdate = st.date_input("Contract Start Date : ","today")
enddate = st.date_input("Contract End Date:","today")
termination_period = st.selectbox("Termination Period",["1 week Before","1 Month Before","Na"])
submit_button = st.button("Generate Contract")


if submit_button:
    st.subheader("Thinking...")
    if all([party1_name, party1_address, party2_name, party2_address, cost, contract_type, subject, scope]):
        with st.spinner("Analyzing .."):
            parties = [party1_name, party2_name]
            addresses = [party1_address, party2_address]
            contract = generate_contract(parties, addresses, cost, contract_type, subject, scope,payment_conditions)
            #st.text_area("Generated Contract", contract, height=500)
        
            st.subheader("The Contract..: ")
            st.success(contract)
            st.subheader("Saving Contracts - PDF and Word: ")
           
            st.markdown("Done")    
    else:
        st.error("Please fill in all fields to generate the contract.")
