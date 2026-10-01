KimChin_Coffee/
│
├── app.py
└── logo1.jpg
import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="KimChin Coffee",
    page_icon="☕",
    layout="centered"
)

# =========================
# CSS GIAO DIỆN
# =========================
st.markdown("""
<style>
    .stApp {
        background-color: #f7fbff;
    }

    .main-title {
        text-align: center;
        color: #2387d9;
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .sub-title {
        text-align: center;
        color: #5f7f99;
        font-size: 18px;
        margin-bottom: 25px;
    }

    .total-box {
        background-color: #dff1ff;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        border: 2px solid #78bdf0;
    }

    .total-text {
        color: #1671b8;
        font-size: 30px;
        font-weight: bold;
    }

    .bill-item {
        background-color: white;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #cce6f7;
        margin-bottom: 10px;
    }

    div.stButton > button {
        border-radius: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# LOGO
# =========================
try:
    st.image("logo1.jpg", use_container_width=True)
except:
    st.markdown(
        '<div class="main-title">☕ KimChin</div>',
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="sub-title">COFFEE & MILK TEA</div>',
    unsafe_allow_html=True
)

# =========================
# MENU
# =========================

menu = {
    "Trà sữa": {
        "Trà sữa truyền thống": 30000,
        "Trà sữa matcha": 35000,
        "Trà sữa socola": 35000,
        "Trà sữa khoai môn": 35000,
        "Trà sữa thái xanh": 32000
    },

    "Coffee": {
        "Cà phê đen": 25000,
        "Cà phê sữa": 30000,
        "Bạc xỉu": 35000,
        "Americano": 30000,
        "Cappuccino": 40000,
        "Latte": 40000
    }
}

topping_menu = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000
}

# =========================
# KHỞI TẠO SESSION
# =========================

if "bill" not in st.session_state:
    st.session_state.bill = []

# =========================
# NHẬP THÔNG TIN MÓN
# =========================

st.subheader("🧋 Chọn món")

loai_mon = st.selectbox(
    "Loại đồ uống",
    list(menu.keys())
)

mon = st.selectbox(
    "Tên món",
    list(menu[loai_mon].keys())
)

gia_mon = menu[loai_mon][mon]

so_luong = st.number_input(
    "Số lượng",
    min_value=1,
    max_value=20,
    value=1,
    step=1
)

topping = st.selectbox(
    "Topping",
    list(topping_menu.keys())
)

gia_topping = topping_menu[topping]

duong = st.radio(
    "Mức độ đường",
    ["100%", "70%", "0%"],
    horizontal=True
)

# =========================
# HIỂN THỊ GIÁ
# =========================

st.info(
    f"💰 Giá món: **{gia_mon:,} VNĐ**  |  "
    f"Topping: **{gia_topping:,} VNĐ**"
)

# =========================
# THÊM MÓN
# =========================

if st.button("➕ Thêm món vào bill", use_container_width=True):

    don_gia = gia_mon + gia_topping
    thanh_tien = don_gia * so_luong

    item = {
        "loai": loai_mon,
        "mon": mon,
        "so_luong": so_luong,
        "topping": topping,
        "duong": duong,
        "don_gia": don_gia,
        "thanh_tien": thanh_tien
    }

    st.session_state.bill.append(item)

    st.success(f"Đã thêm {so_luong} x {mon} vào bill!")

# =========================
# HIỂN THỊ BILL
# =========================

st.divider()

st.subheader("🧾 HÓA ĐƠN")

if len(st.session_state.bill) == 0:

    st.info("Chưa có món nào trong hóa đơn.")

else:

    tong_tien = 0

    for i, item in enumerate(st.session_state.bill):

        tong_tien += item["thanh_tien"]

        st.markdown(
            f"""
            <div class="bill-item">
                <b>#{i + 1} {item["mon"]}</b><br>
                Loại: {item["loai"]}<br>
                Số lượng: {item["so_luong"]}<br>
                Topping: {item["topping"]}<br>
                Đường: {item["duong"]}<br>
                Đơn giá: {item["don_gia"]:,} VNĐ<br>
                <b>Thành tiền: {item["thanh_tien"]:,} VNĐ</b>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =========================
    # TỔNG TIỀN
    # =========================

    st.markdown(
        f"""
        <div class="total-box">
            <div>TỔNG THANH TOÁN</div>
            <div class="total-text">
                {tong_tien:,} VNĐ
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # =========================
    # NÚT XÓA BILL
    # =========================

    if st.button("🗑️ Xóa toàn bộ hóa đơn", use_container_width=True):

        st.session_state.bill = []

        st.rerun()

# =========================
# FOOTER
# =========================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#6c8da5;">
        ☕ <b>KimChin Coffee</b> ☕<br>
        Good Coffee • Better Days 💙
    </div>
    """,
    unsafe_allow_html=True
)
