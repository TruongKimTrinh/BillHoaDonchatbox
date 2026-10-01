import streamlit as st
from datetime import datetime

# =========================================================
# 1. CẤU HÌNH TRANG
# =========================================================

st.set_page_config(
    page_title="KimChin Tea & Coffee",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# 2. GIAO DIỆN CSS
# =========================================================

st.markdown("""
<style>

    /* Nền */
    .stApp {
        background-color: #F5FBFF;
    }

    /* Tiêu đề */
    .title {
        text-align: center;
        color: #1683C8;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #6B8FA5;
        font-size: 18px;
        margin-bottom: 25px;
    }

    /* Khung thông tin */
    .box {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #C8E8FA;
        margin-bottom: 15px;
    }

    /* Món trong bill */
    .bill-item {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #45A9E8;
        margin-bottom: 10px;
    }

    /* Tổng tiền */
    .total-box {
        background-color: #DDF3FF;
        border: 2px solid #45A9E8;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        margin-top: 15px;
    }

    .total-title {
        color: #4F7185;
        font-size: 18px;
    }

    .total-money {
        color: #0876B8;
        font-size: 32px;
        font-weight: bold;
    }

    /* Nút */
    div.stButton > button {
        border-radius: 10px;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. TIÊU ĐỀ APP
# =========================================================

st.markdown(
    '<div class="title">🧋 KimChin</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">TEA & COFFEE • BILL CALCULATOR</div>',
    unsafe_allow_html=True
)

st.divider()


# =========================================================
# 4. MENU
# =========================================================

menu = {

    "Trà sữa": {
        "Trà sữa truyền thống": 30000,
        "Trà sữa matcha": 35000,
        "Trà sữa socola": 35000,
        "Trà sữa khoai môn": 35000,
        "Trà sữa thái xanh": 32000,
        "Trà sữa dâu": 35000
    },

    "Coffee": {
        "Cà phê đen": 25000,
        "Cà phê sữa": 30000,
        "Bạc xỉu": 35000,
        "Americano": 30000,
        "Latte": 40000,
        "Cappuccino": 40000
    }
}


# =========================================================
# 5. TOPPING
# =========================================================

topping_menu = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Thạch phô mai": 7000,
    "Kem cheese": 10000
}


# =========================================================
# 6. KHỞI TẠO BILL
# =========================================================

if "bill" not in st.session_state:
    st.session_state.bill = []


# =========================================================
# 7. THÔNG TIN KHÁCH HÀNG
# =========================================================

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================================================
# 8. CHỌN MÓN
# =========================================================

st.subheader("🧋 Chọn món")

loai_mon = st.selectbox(
    "Loại đồ uống",
    ["Trà sữa", "Coffee"]
)

mon = st.selectbox(
    "Tên món",
    list(menu[loai_mon].keys())
)

gia_mon = menu[loai_mon][mon]

col1, col2 = st.columns(2)

with col1:
    so_luong = st.number_input(
        "🔢 Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

with col2:
    duong = st.selectbox(
        "🍬 Mức độ đường",
        ["100%", "70%", "0%"]
    )


# =========================================================
# 9. CHỌN TOPPING
# =========================================================

st.subheader("🧋 Thêm topping")

toppings_chon = st.multiselect(
    "Chọn topping",
    list(topping_menu.keys())
)

# Tính tiền topping
tong_tien_topping = sum(
    topping_menu[topping]
    for topping in toppings_chon
)


# =========================================================
# 10. HIỂN THỊ GIÁ TẠM TÍNH
# =========================================================

don_gia = gia_mon + tong_tien_topping

thanh_tien = don_gia * so_luong

st.info(
    f"""
    **Món:** {mon}  
    **Giá:** {gia_mon:,} VNĐ  
    **Topping:** {tong_tien_topping:,} VNĐ  
    **Đơn giá:** {don_gia:,} VNĐ  
    **Số lượng:** {so_luong}  
    **Thành tiền:** {thanh_tien:,} VNĐ
    """
)


# =========================================================
# 11. NÚT THÊM MÓN
# =========================================================

if st.button(
    "➕ THÊM MÓN VÀO HÓA ĐƠN",
    use_container_width=True
):

    item = {
        "loai": loai_mon,
        "mon": mon,
        "so_luong": so_luong,
        "topping": toppings_chon.copy(),
        "duong": duong,
        "gia_mon": gia_mon,
        "gia_topping": tong_tien_topping,
        "don_gia": don_gia,
        "thanh_tien": thanh_tien
    }

    st.session_state.bill.append(item)

    st.success(
        f"Đã thêm {so_luong} x {mon} vào hóa đơn!"
    )


# =========================================================
# 12. HIỂN THỊ HÓA ĐƠN
# =========================================================

st.divider()

st.subheader("🧾 HÓA ĐƠN")

if len(st.session_state.bill) == 0:

    st.info(
        "Chưa có món nào trong hóa đơn. "
        "Hãy chọn món và nhấn 'Thêm món vào hóa đơn'."
    )

else:

    tong_bill = 0

    # Thông tin hóa đơn
    st.markdown(
        f"""
        **Khách hàng:** {ten_khach if ten_khach else "Khách lẻ"}  
        **Thời gian:** {datetime.now().strftime("%d/%m/%Y %H:%M")}
        """
    )

    st.write("")

    # -----------------------------------------------------
    # HIỂN THỊ TỪNG MÓN
    # -----------------------------------------------------

    for i, item in enumerate(st.session_state.bill):

        tong_bill += item["thanh_tien"]

        # Topping
        if item["topping"]:
            topping_text = ", ".join(item["topping"])
        else:
            topping_text = "Không topping"

        st.markdown(
            f"""
            <div class="bill-item">

            <b>#{i + 1} 🧋 {item["mon"]}</b>

            <br><br>

            📌 Loại: {item["loai"]}

            <br>

            🔢 Số lượng: {item["so_luong"]}

            <br>

            🍬 Đường: {item["duong"]}

            <br>

            🧋 Topping: {topping_text}

            <br>

            💰 Giá món: {item["gia_mon"]:,} VNĐ

            <br>

            ➕ Tiền topping: {item["gia_topping"]:,} VNĐ

            <br>

            <b>💵 Thành tiền: {item["thanh_tien"]:,} VNĐ</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # TỔNG TIỀN
    # =====================================================

    st.markdown(
        f"""
        <div class="total-box">

            <div class="total-title">
                💰 TỔNG SỐ TIỀN CẦN THANH TOÁN
            </div>

            <div class="total-money">
                {tong_bill:,} VNĐ
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =====================================================
    # CÁC NÚT XỬ LÝ BILL
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🗑️ XÓA HÓA ĐƠN",
            use_container_width=True
        ):

            st.session_state.bill = []

            st.rerun()

    with col2:

        if st.button(
            "✅ THANH TOÁN",
            use_container_width=True
        ):

            st.success(
                f"Thanh toán thành công! "
                f"Tổng tiền: {tong_bill:,} VNĐ"
            )


# =========================================================
# 13. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#6B8FA5;">

    ☕ 🧋 <b>KimChin Tea & Coffee</b>

    <br>

    Good Coffee • Better Days 💙

    </div>
    """,
    unsafe_allow_html=True
)
