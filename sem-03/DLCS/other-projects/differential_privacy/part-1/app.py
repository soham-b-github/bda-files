import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import diffprivlib.mechanisms as mechanisms
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(page_title="DP Demo", layout="wide")

# Initialize Faker
fake = Faker()

# --- 1. DATA GENERATION (The Server Storage) ---
@st.cache_data
def generate_data(n_records):
    """
    Simulates the 'Secret Server Data'.
    This creates a raw CSV-style dataset.
    """
    data = []
    for _ in range(n_records):
        data.append({
            'User_ID': fake.uuid4()[:8],
            'Name': fake.name(),
            'Age': np.random.randint(20, 65),
            'Role': np.random.choice(['Engineer', 'HR', 'Manager', 'Intern']),
            'Salary': int(np.random.normal(70000, 15000)) # Sensitive Column
        })
    df = pd.DataFrame(data)
    # Ensure no negative salaries from normal distribution
    df['Salary'] = df['Salary'].apply(lambda x: max(x, 30000))
    return df

# --- 2. THE ATTACK LOGIC ---
def run_differencing_attack(df, target_index):
    """
    Simulates a hacker trying to find a specific person's salary
    by running two queries: Sum(All) and Sum(All - Target).
    """
    target_person = df.iloc[target_index]
    
    # Query 1: Sum of ALL salaries
    sum_all = df['Salary'].sum()
    
    # Query 2: Sum of salaries EXCLUDING the target
    subset_df = df.drop(target_index)
    sum_subset = subset_df['Salary'].sum()
    
    # The Attack
    reconstructed_salary = sum_all - sum_subset
    return target_person, reconstructed_salary

# --- 3. THE IBM DIFFPRIVLIB LOGIC ---
def get_dp_sum(true_sum, epsilon, sensitivity):
    """
    Uses IBM's Differential Privacy Library to add Laplace noise.
    """
    # Initialize the Mechanism
    mech = mechanisms.Laplace(epsilon=epsilon, sensitivity=sensitivity)
    
    # Randomise the value
    noisy_sum = mech.randomise(true_sum)
    return noisy_sum

# --- UI LAYOUT ---

st.title("🔒 Differential Privacy: The Database Reconstruction Attack")
st.markdown("""
This dashboard simulates a **Secure Payroll Server**. 
We will demonstrate how a **Differencing Attack** works on raw data, 
and how **Differential Privacy (IBM Diffprivlib)** prevents it.
""")

# Sidebar Controls
st.sidebar.header("Configuration")
data_size = st.sidebar.slider("Dataset Size", 100, 1000, 500)
epsilon = st.sidebar.slider("Privacy Budget (Epsilon)", 0.01, 5.0, 1.0, 0.01)
st.sidebar.info(f"Low Epsilon ({epsilon}) = High Privacy.\nHigh Epsilon = Low Privacy.")

# Generate Data
if 'df' not in st.session_state:
    st.session_state.df = generate_data(data_size)

# Button to regenerate data
if st.sidebar.button("Regenerate Data"):
    st.session_state.df = generate_data(data_size)
    st.rerun()

df = st.session_state.df

# --- SECTION A: THE SERVER VAULT ---
st.subheader("1. The Secure Server (Raw Data)")
with st.expander("👁️ View Raw Database (Admin Only)"):
    st.dataframe(df)
    st.caption("In a real scenario, this data is encrypted on disk. Analysts never see this view.")

# --- SECTION B: THE ATTACK ---
st.subheader("2. Simulating the Attack")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔴 Without Privacy")
    st.write("A hacker runs two queries to isolate **Row #0** (The Target).")
    
    target, hacked_val = run_differencing_attack(df, 0)
    
    st.metric(label="Target Name", value=target['Name'])
    st.metric(label="True Salary", value=f"${target['Salary']:,.2f}")
    st.metric(label="Hacked Value (Calculated)", value=f"${hacked_val:,.2f}", delta="100% Accuracy")
    
    st.error("⚠️ DATA LEAKED! The math is exact.")

with col2:
    st.markdown(f"### 🟢 With IBM Diffprivlib (ε={epsilon})")
    st.write("The server adds noise from the Laplace Distribution before answering.")
    
    # Calculate Sensitivity (Max theoretical salary someone *could* have)
    # This acts as the bounds for the noise generation
    sensitivity = 150000 
    
    # Get True Sums
    true_sum_all = df['Salary'].sum()
    subset_df = df.drop(0)
    true_sum_subset = subset_df['Salary'].sum()
    
    # Get Noisy Sums using IBM Library
    dp_sum_all = get_dp_sum(true_sum_all, epsilon, sensitivity)
    dp_sum_subset = get_dp_sum(true_sum_subset, epsilon, sensitivity)
    
    # The Attack Calculation on Noisy Data
    dp_hacked_val = dp_sum_all - dp_sum_subset
    
    st.metric(label="Target Name", value=target['Name'])
    st.metric(label="True Salary", value=f"${target['Salary']:,.2f}")
    st.metric(label="Hacked Value (Noisy)", value=f"${dp_hacked_val:,.2f}", 
              delta=f"Error: ${dp_hacked_val - target['Salary']:,.2f}",
              delta_color="inverse")
    
    if abs(dp_hacked_val - target['Salary']) > 5000:
        st.success("✅ ATTACK FAILED. The noise masked the individual.")
    else:
        st.warning("⚠️ ATTACK PARTIALLY SUCCESSFUL. Epsilon is too high!")

# --- SECTION C: VISUALIZATION ---
st.divider()
st.subheader("3. Utility Analysis (Accuracy vs Privacy)")

# Generate plot data on the fly
eps_range = [0.01, 0.1, 0.5, 1.0, 2.0, 5.0]
errors = []

true_mean = df['Salary'].mean()
sensitivity_mean = sensitivity / len(df)

for e in eps_range:
    # Run the mechanism 50 times to get average error
    batch_errors = []
    mech = mechanisms.Laplace(epsilon=e, sensitivity=sensitivity_mean)
    for _ in range(50):
        noisy_mean = mech.randomise(true_mean)
        batch_errors.append(abs(true_mean - noisy_mean))
    errors.append(np.mean(batch_errors))

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(eps_range, errors, marker='o', color='purple', linewidth=2)
ax.set_xscale('log')
ax.set_xlabel('Epsilon (Privacy Budget)')
ax.set_ylabel('Average Error ($)')
ax.set_title('Trade-off: As Privacy Decreases (High Epsilon), Error Drops')
ax.grid(True, which="both", ls="--", alpha=0.5)

st.pyplot(fig)

#streamlit run app.py