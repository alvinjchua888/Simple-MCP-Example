#!/usr/bin/env python3
"""Streamlit Frontend for Math MCP Client."""

import streamlit as st
from client import perform_operation

# Page configuration
st.set_page_config(
    page_title="Math MCP Client",
    page_icon="🔢",
    layout="centered"
)

# Title and description
st.title("🔢 Math MCP Client")
st.markdown("""
This is a Streamlit frontend for the Math MCP Server. 
Select an operation and enter the values to perform calculations.
""")

# Sidebar for operation selection
st.sidebar.header("Operation Selection")
operation = st.sidebar.selectbox(
    "Choose a math operation:",
    ["add", "subtract", "multiply", "divide", "sqrt", "to_integer"]
)

# Main content area
st.header(f"Operation: {operation.upper()}")

# Input fields based on operation
if operation in ["add", "subtract", "multiply", "divide"]:
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("First Number (a)", value=0.0, format="%.2f")
    with col2:
        b = st.number_input("Second Number (b)", value=0.0, format="%.2f")
    
    # Operation description
    descriptions = {
        "add": "Adds two numbers together",
        "subtract": "Subtracts the second number from the first",
        "multiply": "Multiplies two numbers together",
        "divide": "Divides the first number by the second"
    }
    st.info(descriptions[operation])
    
elif operation in ["sqrt", "to_integer"]:
    a = st.number_input("Number (a)", value=0.0, format="%.2f")
    b = None
    
    # Operation description
    descriptions = {
        "sqrt": "Calculates the square root of a number",
        "to_integer": "Converts a number to an integer"
    }
    st.info(descriptions[operation])

# Calculate button
if st.button("Calculate", type="primary", use_container_width=True):
    try:
        with st.spinner("Calculating..."):
            result = perform_operation(operation, a, b)
        
        # Display result
        st.success("✅ Calculation Complete!")
        st.markdown(f"### Result:")
        st.code(result, language=None)
        
    except ValueError as e:
        st.error(f"❌ Error: {str(e)}")
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
### About
This application uses the Model Context Protocol (MCP) to communicate with a math server.
The backend client connects to the MCP server via STDIO and calls the appropriate tools.
""")

# Additional information in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Available Operations")
st.sidebar.markdown("""
- **Add**: a + b
- **Subtract**: a - b
- **Multiply**: a × b
- **Divide**: a ÷ b
- **Square Root**: √a
- **To Integer**: int(a)
""")
