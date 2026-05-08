import streamlit as st

# Page title
st.set_page_config(page_title="Raw Silver Rate Calculator")

st.title("Raw Silver Rate Calculator")

st.write("Enter your shop silver rate per KG")

# Enter 1KG silver price
kg_rate = st.number_input(
    "Silver Price per KG (₹)",
    min_value=0.0
)

if kg_rate > 0:

    # Raw silver price per gram
    raw_gram_rate = kg_rate / 1000

    # 92.5 Silver with 13% wastage
    wastage_percent = 13

    silver_925_rate = raw_gram_rate + (
        raw_gram_rate * wastage_percent / 100
    )

    # Show prices
    st.success(f"Price per gram: ₹{round(raw_gram_rate,2)}")

    st.info(
        f"92.5 Silver + {wastage_percent}% Wastage = ₹{round(silver_925_rate,2)} per gram"
    )

    st.subheader("Quick Price Buttons")

    col1, col2, col3, col4, col5 = st.columns(5)

    if col1.button("1 g"):
        st.success(f"1 g = ₹{round(1 * raw_gram_rate,2)}")
        st.info(f"1 g 92.5 = ₹{round(1 * silver_925_rate,2)}")

    if col2.button("2 g"):
        st.success(f"2 g = ₹{round(2 * raw_gram_rate,2)}")
        st.info(f"2 g 92.5 = ₹{round(2 * silver_925_rate,2)}")

    if col3.button("5 g"):
        st.success(f"5 g = ₹{round(5 * raw_gram_rate,2)}")
        st.info(f"5 g 92.5 = ₹{round(5 * silver_925_rate,2)}")

    if col4.button("10 g"):
        st.success(f"10 g = ₹{round(10 * raw_gram_rate,2)}")
        st.info(f"10 g 92.5 = ₹{round(10 * silver_925_rate,2)}")

    if col5.button("100 g"):
        st.success(f"100 g = ₹{round(100 * raw_gram_rate,2)}")
        st.info(f"100 g 92.5 = ₹{round(100 * silver_925_rate,2)}")

    st.subheader("Custom Weight Calculator")

    weight = st.number_input(
        "Enter weight in grams",
        min_value=0.0
    )

    if weight > 0:

        total = weight * raw_gram_rate
        silver_925_total = weight * silver_925_rate

        st.success(f"{weight} g = ₹{round(total,2)}")

        st.info(
            f"{weight} g 92.5 Silver + Wastage = ₹{round(silver_925_total,2)}"
        )
