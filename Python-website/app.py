
import streamlit as st

st.set_page_config(
    page_title="Vaseem Salary",
    page_icon="💰"
)

st.title("💰 Worker Salary")
st.write("Employee Salary Management")

if "workers" not in st.session_state:
    st.session_state.workers = []

st.subheader("Add New Worker")

name = st.text_input("Worker Name")
salary = st.number_input(
    "Salary Amount (Rs.)",
    min_value=0,
    step=100
)

if st.button("Add Worker"):
    if name.strip() and salary > 0:
        st.session_state.workers.append({
            "name": name.strip(),
            "salary": salary
        })
        st.success("Worker Added!")
    else:
        st.warning("Enter name and salary")

st.divider()
st.subheader("Worker List")

total = 0

for i, worker in enumerate(st.session_state.workers):
    col1, col2, col3 = st.columns([2, 2, 1])

    col1.write(worker["name"])
    col2.write(f'Rs. {worker["salary"]:,.2f}')
    total += worker["salary"]

    if col3.button("Delete", key=f"delete_{i}"):
        st.session_state.workers.pop(i)
        st.rerun()

st.divider()
st.metric("TOTAL SALARY", f"Rs. {total:,.2f}")
st.caption(f"Total Workers: {len(st.session_state.workers)}")
