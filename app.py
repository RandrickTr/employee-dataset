import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Employee Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load data
df = pd.read_csv('Employee_Cleaned.csv')

# Title and description
st.title("📊 Employee Dataset Dashboard")
st.markdown("Interactive analysis of employee data for insights and decision-making")

# Summary Metrics
st.subheader("📈 Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total Employees", len(df))
    
with col2:
    st.metric("Average Age", f"{df['Age'].astype(int).mean():.1f}")
    
with col3:
    left_count = int(df['LeaveOrNot'].sum())
    st.metric("Employees Left", left_count)
    
with col4:
    attrition = (df['LeaveOrNot'].sum() / len(df) * 100)
    st.metric("Attrition Rate", f"{attrition:.1f}%")
    
with col5:
    benched = (df['EverBenched'] == 'Yes').sum()
    st.metric("Currently Benched", benched)

st.divider()

# Row 1: Education & City
st.subheader("🔍 Demographic Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Education Distribution")
    ed_data = df['Education'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#3498db', '#e74c3c', '#2ecc71']
    ed_data.plot(kind='bar', ax=ax, color=colors)
    ax.set_title("Employees by Education Level", fontsize=12, fontweight='bold')
    ax.set_xlabel("Education")
    ax.set_ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

with col2:
    st.subheader("City Distribution")
    city_data = df['City'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#9b59b6', '#f39c12', '#1abc9c']
    ax.pie(city_data.values, labels=city_data.index, autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Employees by City", fontsize=12, fontweight='bold')
    st.pyplot(fig)

st.divider()

# Row 2: Gender & Payment Tier
st.subheader("💼 Compensation & Demographics")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gender Distribution")
    gender_data = df['Gender'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#3498db', '#e91e63']
    gender_data.plot(kind='bar', ax=ax, color=colors)
    ax.set_title("Employees by Gender", fontsize=12, fontweight='bold')
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    st.pyplot(fig)

with col2:
    st.subheader("Payment Tier Distribution")
    tier_data = df['PaymentTier'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#2ecc71', '#f39c12', '#e74c3c']
    tier_data.plot(kind='bar', ax=ax, color=colors)
    ax.set_title("Employees by Payment Tier", fontsize=12, fontweight='bold')
    ax.set_xlabel("Payment Tier")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    st.pyplot(fig)

st.divider()

# Row 3: Age & Experience
st.subheader("📊 Age & Experience Analysis")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Age Distribution")
    fig, ax = plt.subplots(figsize=(8, 5))
    df['Age'].astype(int).hist(bins=15, ax=ax, color='#3498db', edgecolor='black')
    ax.set_title("Age Distribution", fontsize=12, fontweight='bold')
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    ax.grid(axis='y', alpha=0.3)
    st.pyplot(fig)

with col2:
    st.subheader("Experience Distribution")
    exp_data = df['ExperienceInCurrentDomain'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(8, 5))
    exp_data.plot(kind='bar', ax=ax, color='#e74c3c')
    ax.set_title("Years of Experience in Current Domain", fontsize=12, fontweight='bold')
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    st.pyplot(fig)

st.divider()

# Row 4: Employee Status
st.subheader("🎯 Employee Status")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Retention Status")
    leave_data = df['LeaveOrNot'].value_counts()
    leave_labels = ['Stayed (0)', 'Left (1)']
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#2ecc71', '#e74c3c']
    ax.pie([leave_data.get(0, 0), leave_data.get(1, 0)], labels=leave_labels, 
           autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title("Employee Retention Rate", fontsize=12, fontweight='bold')
    st.pyplot(fig)

with col2:
    st.subheader("Benched Status")
    bench_data = df['EverBenched'].value_counts()
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#2ecc71', '#f39c12']
    bench_data.plot(kind='bar', ax=ax, color=colors)
    ax.set_title("Active vs Benched Employees", fontsize=12, fontweight='bold')
    ax.set_xlabel("Status")
    ax.set_ylabel("Count")
    plt.xticks(rotation=0)
    st.pyplot(fig)

st.divider()

# Joining Year Analysis
st.subheader("📅 Joining Year Analysis")
year_data = df['JoiningYear'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(12, 5))
year_data.plot(kind='bar', ax=ax, color='#9b59b6')
ax.set_title("Employees by Joining Year", fontsize=12, fontweight='bold')
ax.set_xlabel("Year")
ax.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig)

st.divider()

# Data Explorer
st.subheader("🔍 Data Explorer")

if st.checkbox("Show all raw data"):
    st.dataframe(df, use_container_width=True)

# Filter by education
st.subheader("📋 Filter Data by Education")
education = st.selectbox("Select Education Level:", df['Education'].unique())
filtered_df = df[df['Education'] == education]
st.write(f"**Showing {len(filtered_df)} employees with {education} education**")
st.dataframe(filtered_df, use_container_width=True)

# Statistics
st.subheader("📊 Detailed Statistics")
col1, col2 = st.columns(2)

with col1:
    st.write("**Age Statistics:**")
    st.write(df['Age'].astype(int).describe())

with col2:
    st.write("**Experience Statistics:**")
    st.write(df['ExperienceInCurrentDomain'].astype(int).describe())

st.divider()

# Footer
st.markdown("---")
st.markdown("📊 **Dashboard built with Streamlit** | Data: Employee_Cleaned.csv")
