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
# 2. GIAO DIỆN
# =========================================================

st.markdown("""
<style>

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
    margin-bottom: 20px;
}

/* Khung */
.box {
    background-color: white;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #C8E8FA;
    margin-bottom: 15px;
}

/* Bill */
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

/* Chat */
.chat-title {
    color: #1683C8;
    font-size: 25px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# 3. TIÊU ĐỀ
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
# 8. CHỌN ĐỒ UỐNG
# =========================================================

st.subheader("🧋 Chọn đồ uống")

loai_mon = st.selectbox(
    "Loại đồ uống",
    ["Trà sữa", "Coffee"]
)

mon = st.selectbox(
    "Tên món",
    list(menu[loai_mon].keys())
)

gia_mon = menu[loai_mon][mon]


# =========================================================
# 9. SỐ LƯỢNG + ĐƯỜNG
# =========================================================

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
# 10. TOPPING
# =========================================================

st.subheader("🥤 Thêm topping")

toppings_chon = st.multiselect(
    "Chọn topping",
    list(topping_menu.keys())
)


# Tính tổng topping
tong_tien_topping = sum(
    topping_menu[topping]
    for topping in toppings_chon
)


# =========================================================
# 11. TÍNH TIỀN MÓN
# =========================================================

don_gia = gia_mon + tong_tien_topping

thanh_tien = don_gia * so_luong


# =========================================================
# 12. HIỂN THỊ TẠM TÍNH
# =========================================================

st.info(
    f"""
💰 **Giá món:** {gia_mon:,} VNĐ

🥤 **Tiền topping:** {tong_tien_topping:,} VNĐ

🔢 **Số lượng:** {so_luong}

💵 **Đơn giá:** {don_gia:,} VNĐ

🧾 **Thành tiền:** {thanh_tien:,} VNĐ
"""
)


# =========================================================
# 13. THÊM MÓN VÀO BILL
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
# 14. HÓA ĐƠN
# =========================================================

st.divider()

st.subheader("🧾 HÓA ĐƠN")

if len(st.session_state.bill) == 0:

    st.info(
        "Chưa có món nào trong hóa đơn."
    )

else:

    tong_bill = 0

    st.markdown(
        f"""
**👤 Khách hàng:** {ten_khach if ten_khach else "Khách lẻ"}

**🕐 Thời gian:** {datetime.now().strftime("%d/%m/%Y %H:%M")}
"""
    )

    st.write("")

    # Hiển thị từng món
    for i, item in enumerate(st.session_state.bill):

        tong_bill += item["thanh_tien"]

        if item["topping"]:

            topping_text = ", ".join(
                item["topping"]
            )

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

🥤 Topping: {topping_text}

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
    # TỔNG THANH TOÁN
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
    # NÚT XÓA + THANH TOÁN
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
# 15. CHATBOX
# =========================================================

st.divider()

st.markdown(
    '<div class="chat-title">💬 Trợ lý KimChin</div>',
    unsafe_allow_html=True
)

st.write(
    "Xin chào! Bạn có thể chọn câu hỏi bên dưới "
    "hoặc nhập câu hỏi trực tiếp."
)


# =========================================================
# 16. CÂU HỎI THƯỜNG GẶP
# =========================================================

col1, col2 = st.columns(2)


with col1:

    q1 = st.button(
        "🧋 Menu có những món gì?",
        use_container_width=True
    )

    q2 = st.button(
        "💰 Giá các món bao nhiêu?",
        use_container_width=True
    )

    q3 = st.button(
        "🥤 Có những topping nào?",
        use_container_width=True
    )

    q4 = st.button(
        "🍬 Có những mức đường nào?",
        use_container_width=True
    )


with col2:

    q5 = st.button(
        "⭐ Món nào được yêu thích?",
        use_container_width=True
    )

    q6 = st.button(
        "🧾 Tính bill như thế nào?",
        use_container_width=True
    )

    q7 = st.button(
        "😊 Xin chào KimChin",
        use_container_width=True
    )

    q8 = st.button(
        "❤️ Cảm ơn",
        use_container_width=True
    )


# =========================================================
# 17. XÁC ĐỊNH CÂU HỎI
# =========================================================

prompt = None


if q1:
    prompt = "Menu có những món gì?"

elif q2:
    prompt = "Giá các món bao nhiêu?"

elif q3:
    prompt = "Có những topping nào?"

elif q4:
    prompt = "Có những mức đường nào?"

elif q5:
    prompt = "Món nào được yêu thích?"

elif q6:
    prompt = "Tính bill như thế nào?"

elif q7:
    prompt = "Xin chào KimChin"

elif q8:
    prompt = "Cảm ơn"


# =========================================================
# 18. Ô CHAT
# =========================================================

chat_input = st.chat_input(
    "Hoặc nhập câu hỏi của bạn..."
)


if chat_input:

    prompt = chat_input


# =========================================================
# 19. LƯU LỊCH SỬ CHAT
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# Hiển thị tin nhắn cũ
for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# =========================================================
# 20. XỬ LÝ CHATBOX
# =========================================================

if prompt:

    # -------------------------
    # Tin nhắn khách
    # -------------------------

    st.session_state.messages.append({

        "role": "user",

        "content": prompt

    })


    with st.chat_message("user"):

        st.markdown(prompt)


    cau_hoi = prompt.lower()


    # =====================================================
    # MENU
    # =====================================================

    if "menu" in cau_hoi or "món" in cau_hoi:

        reply = """
### 🧋 MENU KIMCHIN

**TRÀ SỮA**

• Trà sữa truyền thống — **30.000đ**

• Trà sữa matcha — **35.000đ**

• Trà sữa socola — **35.000đ**

• Trà sữa khoai môn — **35.000đ**

• Trà sữa thái xanh — **32.000đ**

• Trà sữa dâu — **35.000đ**

**COFFEE**

• Cà phê đen — **25.000đ**

• Cà phê sữa — **30.000đ**

• Bạc xỉu — **35.000đ**

• Americano — **30.000đ**

• Latte — **40.000đ**

• Cappuccino — **40.000đ**
"""


    # =====================================================
    # GIÁ
    # =====================================================

    elif "giá" in cau_hoi:

        reply = """
### 💰 BẢNG GIÁ

🧋 Trà sữa: **30.000đ – 35.000đ**

☕ Coffee: **25.000đ – 40.000đ**

🥤 Topping: **5.000đ – 10.000đ**

Bạn có thể chọn món trực tiếp ở phần
**Tính hóa đơn** phía trên nhé 💙
"""


    # =====================================================
    # TOPPING
    # =====================================================

    elif "topping" in cau_hoi:

        reply = """
### 🥤 TOPPING KIMCHIN

• Trân châu đen — **5.000đ**

• Trân châu trắng — **5.000đ**

• Thạch trái cây — **5.000đ**

• Pudding trứng — **7.000đ**

• Thạch phô mai — **7.000đ**

• Kem cheese — **10.000đ**
"""


    # =====================================================
    # ĐƯỜNG
    # =====================================================

    elif "đường" in cau_hoi:

        reply = """
### 🍬 MỨC ĐỘ ĐƯỜNG

**100%** → Ngọt bình thường

**70%** → Ít ngọt

**0%** → Không đường
"""


    # =====================================================
    # MÓN YÊU THÍCH
    # =====================================================

    elif "yêu thích" in cau_hoi:

        reply = """
### ⭐ MÓN ĐƯỢC YÊU THÍCH

🧋 Trà sữa matcha

🧋 Trà sữa truyền thống

☕ Bạc xỉu

☕ Latte

💙 Bạn có thể chọn món trực tiếp trên menu nhé!
"""


    # =====================================================
    # BILL
    # =====================================================

    elif "bill" in cau_hoi:

        reply = """
### 🧾 CÁCH TÍNH BILL

**Bước 1:** Chọn loại đồ uống.

**Bước 2:** Chọn món.

**Bước 3:** Chọn số lượng.

**Bước 4:** Chọn topping.

**Bước 5:** Chọn mức đường.

Sau đó nhấn:

**➕ THÊM MÓN VÀO HÓA ĐƠN**

💰 Hệ thống sẽ tự động tính tổng tiền.
"""


    # =====================================================
    # XIN CHÀO
    # =====================================================

    elif "xin chào" in cau_hoi or "hello" in cau_hoi:

        reply = """
👋 **Xin chào!**

Chào mừng bạn đến với **KimChin Tea & Coffee** 💙

Mình có thể giúp bạn tìm hiểu:

🧋 Menu

💰 Giá món

🥤 Topping

🍬 Mức đường

🧾 Cách tính bill
"""


    # =====================================================
    # CẢM ƠN
    # =====================================================

    elif "cảm ơn" in cau_hoi:

        reply = """
🥰 **KimChin cảm ơn bạn!**

Chúc bạn có một ngày thật vui và thưởng thức
đồ uống thật ngon tại KimChin 💙
"""


    # =====================================================
    # KHÔNG HIỂU
    # =====================================================

    else:

        reply = """
😊 Xin lỗi, KimChin chưa hiểu câu hỏi của bạn.

Bạn có thể hỏi:

🧋 **Menu có những món gì?**

💰 **Giá các món bao nhiêu?**

🥤 **Có những topping nào?**

🍬 **Có những mức đường nào?**

⭐ **Món nào được yêu thích?**

🧾 **Tính bill như thế nào?**
"""


    # =====================================================
    # HIỂN THỊ TRẢ LỜI
    # =====================================================

    st.session_state.messages.append({

        "role": "assistant",

        "content": reply

    })


    with st.chat_message("assistant"):

        st.markdown(reply)


# =========================================================
# 21. FOOTER
# =========================================================

st.divider()

st.markdown(
    """
<div style="text-align:center; color:#6B8FA5;">

☕ 🧋 <b>KimChin Tea & Coffee</b>

<br><br>

Good Coffee • Better Days 💙

</div>
""",
    unsafe_allow_html=True
)
