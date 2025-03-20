import streamlit as st

# Define the menu with symbols
menu = {
    "🍕 Pizza": 160,
    "🍝 Pasta": 120, 
    "🍔 Burger": 100,
    "🥪 Sandwich": 80,
    "🍟 Fries": 70,
    "☕ Hot Coffee": 50,   
    "🥶 Cold Coffee": 40,
    "🫖 Tea": 30,
    "🧀 Cheese Maggie": 20
}

# App Title
st.title("☕ Hotel Management System ☕")
st.subheader("Menu")

# Display the menu in a table format
st.write("### Available Items & Prices:")
st.table([{"Item": item, "Price (₹)": price} for item, price in menu.items()])

# Initialize the session state for order management
if 'order' not in st.session_state:
    st.session_state.order = []

# Order system
selected_item = st.selectbox("Select an item to order", list(menu.keys()))
if st.button("Add to Order"):
    st.session_state.order.append(selected_item)
    st.success(f"{selected_item} added to your order!")

# Display the order
if st.session_state.order:
    st.subheader("### Your Order:")
    order_summary = {item: st.session_state.order.count(item) for item in set(st.session_state.order)}
    total_amount = sum(menu[item] * qty for item, qty in order_summary.items())

    # Display order summary as a table
    st.table([{"Item": item, "Quantity": qty, "Price (₹)": menu[item] * qty} for item, qty in order_summary.items()])
    
    # Display total amount
    st.write(f"### Total Amount: ₹{total_amount}")

    # Order confirmation button
    if st.button("Confirm Order"):
        st.success("Order confirmed! Thank you for ordering. Enjoy your meal! 🍽️")
        st.session_state.order = []  # Reset order after confirmation
