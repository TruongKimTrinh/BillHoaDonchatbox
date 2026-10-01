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

.bill-item {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #45A9E8;
    margin-bottom: 10px;
}

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
# 6. KHỞI TẠO SESSION STATE
# =========================================================

if "bill" not in st.session_state:
    st.session_state.bill = []

if "messages" not in st.session_state:
    st.session_state.messages = []


# =========================================================
# 7. THÔNG TIN KHÁCH HÀNG
# =========================================================

st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)


# =========================================================
# 8. THÊM ĐỒ UỐNG
# =========================================================

st.subheader("🧋 Thêm đồ uống vào đơn")

loai_mon = st.selectbox(
    "1️⃣ Loại đồ uống",
    ["Trà sữa", "Coffee"]
)

mon = st.selectbox(
    "2️⃣ Chọn món",
    list(menu[loai_mon].keys())
)

gia_mon = menu[loai_mon][mon]


# =========================================================
# 9. SỐ LƯỢNG + MỨC ĐƯỜNG
# =========================================================

col1, col2 = st.columns(2)

with col1:

    so_luong = st.number_input(
        "3️⃣ Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )

with col2:

    duong = st.selectbox(
        "4️⃣ Mức độ đường",
        ["100%", "70%", "0%"]
    )


# =========================================================
# 10. TOPPING
# =========================================================

toppings_chon = st.multiselect(
    "5️⃣ Chọn topping",
    list(topping_menu.keys())
)


# =========================================================
# 11. TÍNH TIỀN MÓN HIỆN TẠI
# =========================================================

tong_tien_topping = sum(
    topping_menu[topping]
    for topping in toppings_chon
)

don_gia = gia_mon + tong_tien_topping

thanh_tien = don_gia * so_luong


st.info(
    f"""
🧋 **{mon}**

💰 Giá món: **{gia_mon:,} VNĐ**

🥤 Tiền topping / ly: **{tong_tien_topping:,} VNĐ**

🔢 Số lượng: **{so_luong}**

🍬 Đường: **{duong}**

💵 Thành tiền: **{thanh_tien:,} VNĐ**
"""
)


# =========================================================
# 12. NÚT THÊM MÓN
# =========================================================

if st.button(
    "➕ THÊM MÓN NÀY VÀO ĐƠN",
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
        f"✅ Đã thêm {so_luong} x {mon} vào đơn!"
    )


# =========================================================
# 13. HIỂN THỊ ĐƠN HÀNG HIỆN TẠI
# =========================================================

st.divider()

st.subheader("🧾 ĐƠN HÀNG HIỆN TẠI")


if len(st.session_state.bill) == 0:

    st.info(
        "Chưa có món nào. "
        "Hãy chọn món và nhấn 'Thêm món này vào đơn'."
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


    # =====================================================
    # HIỂN THỊ TỪNG MÓN
    # =====================================================

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

➕ Tiền topping: {item["gia_topping"]:,} VNĐ / ly

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
    # NÚT XÓA ĐƠN
    # =====================================================

    col1, col2 = st.columns(2)


    with col1:

        if st.button(
            "🗑️ XÓA TOÀN BỘ ĐƠN",
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
                f"""
                🎉 Thanh toán thành công!

                💰 Tổng tiền:
                **{tong_bill:,} VNĐ**

                Cảm ơn bạn đã sử dụng dịch vụ
                của **KimChin Tea & Coffee** 💙
                """
            )


# =========================================================
# 14. CHATBOX
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
# 15. CÂU HỎI THƯỜNG GẶP
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
# 16. XÁC ĐỊNH CÂU HỎI
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
# 17. Ô CHAT
# =========================================================

chat_input = st.chat_input(
    "Hoặc nhập câu hỏi của bạn..."
)

if chat_input:

    prompt = chat_input


# =========================================================
# 18. HIỂN THỊ LỊCH SỬ CHAT
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(
            message["content"]
        )


# =========================================================
# 19. XỬ LÝ CHATBOX
# =========================================================

if prompt:

    # Tin nhắn khách
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
"""


    # =====================================================
    # TOPPING
    # =====================================================

    elif "topping" in cau_hoi:

        reply = """
### 🥤 TOPPING

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
"""


    # =====================================================
    # BILL
    # =====================================================

    elif "bill" in cau_hoi:

        reply = """
### 🧾 CÁCH ORDER NHIỀU MÓN

Bạn có thể order nhiều món trong cùng một hóa đơn.

Ví dụ:

🧋 2 Trà sữa matcha + trân châu đen

☕ 1 Bạc xỉu

🧋 2 Trà sữa truyền thống + pudding

Chỉ cần chọn từng món → nhấn
**➕ THÊM MÓN NÀY VÀO ĐƠN**.

Sau đó hệ thống sẽ tự động cộng tổng tiền.
"""


    # =====================================================
    # XIN CHÀO
    # =====================================================

    elif "xin chào" in cau_hoi or "hello" in cau_hoi:

        reply = """
👋 **Xin chào!**

Chào mừng bạn đến với
**KimChin Tea & Coffee** 💙

Mình có thể giúp bạn:

🧋 Xem menu

💰 Xem giá

🥤 Xem topping

🍬 Xem mức đường

🧾 Hướng dẫn order
"""


    # =====================================================
    # CẢM ƠN
    # =====================================================

    elif "cảm ơn" in cau_hoi:

        reply = """
🥰 **KimChin cảm ơn bạn!**

Chúc bạn có một ngày thật vui 💙
"""


    # =====================================================
    # KHÔNG HIỂU
    # =====================================================

    else:

        reply = """
😊 Xin lỗi, KimChin chưa hiểu câu hỏi.

Bạn có thể hỏi:

🧋 **Menu có những món gì?**

💰 **Giá các món bao nhiêu?**

🥤 **Có những topping nào?**

🍬 **Có những mức đường nào?**

⭐ **Món nào được yêu thích?**

🧾 **Tính bill như thế nào?**
"""


    # =====================================================
    # TRẢ LỜI
    # =====================================================

    st.session_state.messages.append({

        "role": "assistant",

        "content": reply

    })


    with st.chat_message("assistant"):

        st.markdown(reply)


# =========================================================
# 20. FOOTER
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
