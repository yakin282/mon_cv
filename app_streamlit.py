import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🌐 Network Tool")

network = st.text_input("Adresse réseau", "192.168.10.0")
cidr = st.number_input("CIDR", 0, 32, 26)

if st.button("Calculer"):
    response = requests.get(
        f"{API_URL}/info",
        params={"network": f"{network}/{cidr}"}
    )

    if response.status_code == 200:
        data = response.json()
        st.subheader("Informations réseau")
        st.write("🌐 Network:", data["network"])
        st.write("📢 Broadcast:", data["broadcast"])
        st.write("🧮 Netmask:", data["netmask"])
        st.write("💻 Total hosts:", data["total_hosts"])
        st.subheader("📋 Hosts")
        st.write(data["hosts"])
    else:
        st.error(f"Erreur API ❌ code: {response.status_code}")
