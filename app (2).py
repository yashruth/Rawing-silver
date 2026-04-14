st.title("Raw Silver Rate Calculator")

st.write("Enter your shop silver rate per KG")

# 1 KG silver rate
kg_rate = st.number_input("Silver Price per KG (₹)", min_value=0.0)

if kg_rate > 0:

    gram_rate = kg_rate / 1000

    st.success(f"Price per gram: ₹{round(gram_rate,2)}")

    st.subheader("Quick Price Calculator")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("1 g"):
        st.success(f"1 g = ₹{round(1 * gram_rate,2)}")

    if col2.button("5 g"):
        st.success(f"5 g = ₹{round(5 * gram_rate,2)}")

    if col3.button("10 g"):
        st.success(f"10 g = ₹{round(10 * gram_rate,2)}")

    if col4.button("100 g"):
        st.success(f"100 g = ₹{round(100 * gram_rate,2)}")

    st.subheader("Custom Weight")

    weight = st.number_input("Enter weight in grams")

    if weight > 0:

        total = weight * gram_rate

        st.success(f"{weight} g = ₹{round(total,2)}")