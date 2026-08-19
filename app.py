import streamlit as st

st.set_page_config(
    page_title="Pro คุ้ม",
    page_icon="🛒",
    layout="centered"
)

# Custom CSS for theme styling
st.markdown("""
    <style>
    .stApp {
        background-color: #f7f3ea;
        color: #2b231d;
    }
    div[data-testid="column"] {
        background-color: #f2ebd9;
        padding: 16px;
        border-radius: 16px;
        border: 1px solid #e3dacd;
    }
    .summary-card {
        background-color: #f2ebd9;
        border-radius: 16px;
        padding: 18px;
        border: 1px solid #e3dacd;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .stButton > button {
        border-radius: 25px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛒 Pro คุ้ม")
st.caption("หน้าผลการคำนวณและเปรียบเทียบ")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='color: #d97736; text-align: center; margin-top:0;'>โปรโมชั่น A</h3>", unsafe_allow_html=True)
    name_a = st.text_input("ชื่อ/รายการ A", "โปรโมชั่น A", key="name_a")
    price_a = st.number_input("ราคาปกติ A (บาท)", min_value=0.0, value=25.0, step=1.0, key="price_a")
    promo_a = st.number_input("ราคาโปรฯ A (บาท)", min_value=0.0, value=15.0, step=1.0, key="promo_a")
    qty_a = st.number_input("ปริมาณ A (มล./กรัม)", min_value=0.01, value=500.0, step=10.0, key="qty_a")

    unit_cost_a = (promo_a / qty_a) * 100 if qty_a > 0 else 0.0
    disc_a = ((price_a - promo_a) / price_a) * 100 if price_a > 0 else 0.0

    st.divider()
    st.write(f"**ราคาปกติ:** ~~{price_a:.2f} บาท~~")
    st.write(f"**ราคาโปร:** :red[{promo_a:.2f} บาท]")
    st.write(f"**ต่อ 100 หน่วย:** **{unit_cost_a:.2f}** บาท")
    st.write(f"**ส่วนลด:** **{disc_a:.0f}%**")

with col2:
    st.markdown("<h3 style='color: #41739c; text-align: center; margin-top:0;'>โปรโมชั่น B</h3>", unsafe_allow_html=True)
    name_b = st.text_input("ชื่อ/รายการ B", "โปรโมชั่น B", key="name_b")
    price_b = st.number_input("ราคาปกติ B (บาท)", min_value=0.0, value=45.0, step=1.0, key="price_b")
    promo_b = st.number_input("ราคาโปรฯ B (บาท)", min_value=0.0, value=35.0, step=1.0, key="promo_b")
    qty_b = st.number_input("ปริมาณ B (มล./กรัม)", min_value=0.01, value=1500.0, step=10.0, key="qty_b")

    unit_cost_b = (promo_b / qty_b) * 100 if qty_b > 0 else 0.0
    disc_b = ((price_b - promo_b) / price_b) * 100 if price_b > 0 else 0.0

    st.divider()
    st.write(f"**ราคาปกติ:** ~~{price_b:.2f} บาท~~")
    st.write(f"**ราคาโปร:** :red[{promo_b:.2f} บาท]")
    st.write(f"**ต่อ 100 หน่วย:** **{unit_cost_b:.2f}** บาท")
    st.write(f"**ส่วนลด:** **{disc_b:.0f}%**")

# Result evaluation
if unit_cost_a < unit_cost_b:
    winner_text = f"🏆 **{name_a} คุ้มกว่า**"
    diff = unit_cost_b - unit_cost_a
elif unit_cost_b < unit_cost_a:
    winner_text = f"🏆 **{name_b} คุ้มกว่า**"
    diff = unit_cost_a - unit_cost_b
else:
    winner_text = "🤝 **คุ้มค่าเท่ากันทั้งคู่**"
    diff = 0.0

st.markdown(
    f"""
    <div class="summary-card">
        <h3 style="margin-top:0;">สรุปผลการเปรียบเทียบ</h3>
        <h4 style="color: #2b231d;">{winner_text}</h4>
        <p><b>ราคาต่อ 100 หน่วย ถูกกว่า:</b> <span style="color: #b91c1c; font-weight: bold; font-size: 18px;">{diff:.2f} บาท</span></p>
    </div>
    """,
    unsafe_allow_html=True
)
