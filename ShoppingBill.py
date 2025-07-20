#Day 5/50 - AI Python Challenge
#Shopping Bill : Calculate total cost of 3 items including tax percentage.

import streamlit as st

# Set the title of the app
st.title("🛍️ Shopping Bill Calculator")

st.markdown("Calculate your total bill with discount and tax included.")

# Section 1: Input number of items
st.header("🧾 Enter Item Prices")

# Use a number input to specify how many items user wants to enter
num_items = st.number_input("How many items do you want to enter?", min_value=1, step=1)

item_prices = []

# Input fields for each item
for i in range(int(num_items)):
    price = st.number_input(f"Price of Item {i+1} (₹)", min_value=0.0, step=0.01, format="%.2f")
    item_prices.append(price)

# Section 2: Discount and Tax Inputs
st.header("💸 Enter Discount and Tax")

discount_percent = st.number_input("Discount percentage (%)", min_value=0.0, max_value=100.0, step=0.1)
tax_percent = st.number_input("Tax percentage (%)", min_value=0.0, max_value=100.0, step=0.1)

# Section 3: Calculate Button
if st.button("🧮 Calculate Total"):
    total_before_discount = sum(item_prices)
    discount_amount = (discount_percent / 100) * total_before_discount
    total_after_discount = total_before_discount - discount_amount
    tax_amount = (tax_percent / 100) * total_after_discount
    final_total = total_after_discount + tax_amount

    # Section 4: Display Results
    st.success("✅ Calculation Complete!")

    st.markdown("---")
    st.subheader("📋 Bill Summary")

    st.write(f"**Total before discount:** ₹{total_before_discount:.2f}")
    st.write(f"**Discount ({discount_percent}%):** -₹{discount_amount:.2f}")
    st.write(f"**Total after discount:** ₹{total_after_discount:.2f}")
    st.write(f"**Tax ({tax_percent}%):** +₹{tax_amount:.2f}")
    st.write(f"### 🧾 Final Amount to Pay: ₹{final_total:.2f}")

    # Generate plain text content
    bill_text = (
        "===== Shopping Bill =====\n"
        + "\n".join([f"Item {i+1}: ₹{p:.2f}" for i, p in enumerate(item_prices)])
        + f"\n\nTotal before discount: ₹{total_before_discount:.2f}"
        + f"\nDiscount ({discount_percent}%): -₹{discount_amount:.2f}"
        + f"\nTotal after discount: ₹{total_after_discount:.2f}"
        + f"\nTax ({tax_percent}%): +₹{tax_amount:.2f}"
        + f"\nFinal Amount to Pay: ₹{final_total:.2f}"
        + "\n=========================="
    )

    # Provide download button for text file
    st.download_button(
        label="📥 Download Bill as Text",
        data=bill_text,
        file_name="shopping_bill.txt",
        mime="text/plain"
    )
