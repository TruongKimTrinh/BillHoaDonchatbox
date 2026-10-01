import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================
st.set_page_config(
    page_title="KimChin Tea & Coffee",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# CSS - GIAO DIỆN XANH TRẮNG
# =========================================================
st.markdown("""
<style>
    .stApp {
        background-color: #f5fbff;
    }

    .title {
        text-align: center;
        color: #168acb;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0px;
    }

    .subtitle {
        text-align: center;
        color: #5c7180;
        font-size: 16px;
        margin-bottom: 25px;
    }

    .bill-box {
        background-color: white;
        padding: 18px;
        border-radius: 15px;
        border: 1px solid #d7edf9;
        margin-bottom: 12px;
    }

    .total {
        background-color: #e5f6ff;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        color: #0878b5;
        font-size: 25px;
        font-weight: bold;
    }

    .chat-title {
        color: #168acb;
        font-size: 25px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# TIÊU ĐỀ
# =========================================================
st.markdown(
    '<div class="title">🧋 KimChin</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">TEA & COFFEE • BILL CALCULATOR</div>',
    unsafe_allow_html=True
)

# =========================================================
# MENU
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
# GIÁ SIZE
# =========================================================
size_menu = {
    "M": 0,
    "L": 5000,
    "XL": 10000
}

# =========================================================
# TOPPING
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
# SESSION STATE
# =========================================================
if "bill" not in st.session_state:
    st.session_state.bill = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================
st.subheader("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

st.divider()

# =========================================================
# ĐẶT MÓN
# =========================================================
st.subheader("🛒 Đặt món")

# Loại đồ uống
loai_mon = st.selectbox(
    "1️⃣ Loại đồ uống",
    ["Trà sữa", "Coffee"]
)

# Chọn món
mon = st.selectbox(
    "2️⃣ Chọn món",
    list(menu[loai_mon].keys())
)

gia_mon = menu[loai_mon][mon]

# Chọn size
size = st.selectbox(
    "3️⃣ Chọn size",
    ["M", "L", "XL"]
)

gia_size = size_menu[size]

# Số lượng
so_luong = st.number_input(
    "4️⃣ Số lượng",
    min_value=1,
    max_value=50,
    value=1,
    step=1
)

# Đường
duong = st.selectbox(
    "5️⃣ Mức độ đường",
    ["100%", "70%", "0%"]
)

# Topping
toppings_chon = st.multiselect(
    "6️⃣ Chọn topping",
    list(topping_menu.keys())
)

# =========================================================
# TÍNH TIỀN
# =========================================================
tong_tien_topping = sum(
    topping_menu[topping]
    for topping in toppings_chon
)

don_gia = gia_mon + gia_size + tong_tien_topping

thanh_tien = don_gia * so_luong

# Hiển thị tạm tính
st.info(
    f"💰 Đơn giá: **{don_gia:,} VNĐ/ly**  |  "
    f"Thành tiền: **{thanh_tien:,} VNĐ**"
)

# =========================================================
# THÊM MÓN VÀO ĐƠN
# =========================================================
if st.button(
    "➕ THÊM MÓN NÀY VÀO ĐƠN",
    use_container_width=True
):

    item = {
        "loai": loai_mon,
        "mon": mon,
        "size": size,
        "so_luong": so_luong,
        "topping": toppings_chon.copy(),
        "duong": duong,
        "gia_mon": gia_mon,
        "gia_size": gia_size,
        "gia_topping": tong_tien_topping,
        "don_gia": don_gia,
        "thanh_tien": thanh_tien
    }

    st.session_state.bill.append(item)

    st.success(
        f"✅ Đã thêm {so_luong} x {mon} size {size} vào đơn!"
    )

# =========================================================
# HIỂN THỊ BILL
# =========================================================
st.divider()

st.subheader("🧾 HÓA ĐƠN")

if len(st.session_state.bill) == 0:

    st.info("Chưa có món nào trong đơn.")

else:

    tong_bill = 0

    for i, item in enumerate(st.session_state.bill, start=1):

        tong_bill += item["thanh_tien"]

        topping_text = (
            ", ".join(item["topping"])
            if item["topping"]
            else "Không có"
        )

        st.markdown(
            f"""
            <div class="bill-box">

            <b>🥤 Món {i}: {item["mon"]}</b><br>

            📌 Loại: {item["loai"]}<br>

            📏 Size: <b>{item["size"]}</b>
            (+{item["gia_size"]:,} VNĐ)<br>

            🔢 Số lượng: {item["so_luong"]}<br>

            🍬 Đường: {item["duong"]}<br>

            🧋 Topping: {topping_text}<br>

            💵 Giá món: {item["gia_mon"]:,} VNĐ<br>

            ➕ Giá size: {item["gia_size"]:,} VNĐ<br>

            ➕ Giá topping: {item["gia_topping"]:,} VNĐ/ly<br>

            💰 Thành tiền:
            <b>{item["thanh_tien"]:,} VNĐ</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="total">
        💰 TỔNG THANH TOÁN<br>
        {tong_bill:,} VNĐ
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

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
            "💳 THANH TOÁN",
            use_container_width=True
        ):

            thoi_gian = datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )

            ten = ten_khach if ten_khach else "Khách hàng"

            st.success(
                f"🎉 Cảm ơn {ten} đã mua hàng tại KimChin!"
            )

            st.write(
                f"🕐 Thời gian: {thoi_gian}"
            )

            st.write(
                f"💰 Số tiền cần thanh toán: "
                f"**{tong_bill:,} VNĐ**"
            )

# =========================================================
# CHATBOX KIMCHIN
# =========================================================
st.divider()

st.markdown(
    '<div class="chat-title">🤖 Trợ lý KimChin</div>',
    unsafe_allow_html=True
)

st.write(
    "Xin chào! Bé có thể chọn câu hỏi bên dưới "
    "hoặc tự nhập câu hỏi nha 💙"
)

# =========================================================
# CÂU HỎI NHANH
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

    q5 = st.button(
        "😋 Món nào ngon nhất?",
        use_container_width=True
    )

    q6 = st.button(
        "💎 Món nào giá cao nhất?",
        use_container_width=True
    )

with col2:

    q7 = st.button(
        "💵 Món nào rẻ nhất?",
        use_container_width=True
    )

    q8 = st.button(
        "⭐ Món nào được yêu thích?",
        use_container_width=True
    )

    q9 = st.button(
        "📏 Có những size nào?",
        use_container_width=True
    )

    q10 = st.button(
        "🧋 Topping nào đắt nhất?",
        use_container_width=True
    )

    q11 = st.button(
        "🧾 Tính bill như thế nào?",
        use_container_width=True
    )

    q12 = st.button(
        "👋 Xin chào KimChin",
        use_container_width=True
    )

# =========================================================
# XÁC ĐỊNH CÂU HỎI
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
    prompt = "Món nào ngon nhất?"

elif q6:
    prompt = "Món nào giá cao nhất?"

elif q7:
    prompt = "Món nào rẻ nhất?"

elif q8:
    prompt = "Món nào được yêu thích?"

elif q9:
    prompt = "Có những size nào?"

elif q10:
    prompt = "Topping nào đắt nhất?"

elif q11:
    prompt = "Tính bill như thế nào?"

elif q12:
    prompt = "Xin chào KimChin"

# =========================================================
# NHẬP CÂU HỎI TỰ DO
# =========================================================

chat_input = st.chat_input(
    "Hoặc nhập câu hỏi của bạn..."
)

if chat_input:
    prompt = chat_input

# =========================================================
# HIỂN THỊ LỊCH SỬ CHAT
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# =========================================================
# XỬ LÝ CHATBOX
# =========================================================

if prompt:

    # Lưu câu hỏi người dùng
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # -----------------------------------------------------
    # MENU
    # -----------------------------------------------------

    if "menu" in prompt.lower():

        answer = "🧋 **Menu KimChin hiện có:**\n\n"

        answer += "**Trà sữa:**\n"

        for name, price in menu["Trà sữa"].items():
            answer += f"- {name}: {price:,} VNĐ\n"

        answer += "\n**Coffee:**\n"

        for name, price in menu["Coffee"].items():
            answer += f"- {name}: {price:,} VNĐ\n"

    # -----------------------------------------------------
    # GIÁ
    # -----------------------------------------------------

    elif "giá các món" in prompt.lower():

        answer = """
💰 **Giá đồ uống KimChin:**

🧋 Trà sữa: từ **30.000 - 35.000 VNĐ**

☕ Coffee: từ **25.000 - 40.000 VNĐ**

📏 **Size:**
- M: +0 VNĐ
- L: +5.000 VNĐ
- XL: +10.000 VNĐ

🧋 Topping: từ **5.000 - 10.000 VNĐ**
"""

    # -----------------------------------------------------
    # TOPPING
    # -----------------------------------------------------

    elif "topping" in prompt.lower():

        max_topping = max(topping_menu, key=topping_menu.get)

        if "đắt nhất" in prompt.lower():

            answer = (
                f"💎 Topping có giá cao nhất là "
                f"**{max_topping}** — "
                f"{topping_menu[max_topping]:,} VNĐ."
            )

        else:

            answer = "🥤 **Các topping KimChin:**\n\n"

            for name, price in topping_menu.items():
                answer += f"- {name}: {price:,} VNĐ\n"

    # -----------------------------------------------------
    # MỨC ĐƯỜNG
    # -----------------------------------------------------

    elif "đường" in prompt.lower():

        answer = """
🍬 KimChin có 3 mức đường:

- **100%** – ngọt bình thường
- **70%** – ít ngọt
- **0%** – không đường
"""

    # -----------------------------------------------------
    # SIZE
    # -----------------------------------------------------

    elif "size" in prompt.lower():

        answer = """
📏 **KimChin có 3 size:**

🥤 **M:** Giá gốc

🥤 **L:** +5.000 VNĐ

🥤 **XL:** +10.000 VNĐ

Bé có thể chọn size phù hợp khi order nha 💙
"""

    # -----------------------------------------------------
    # MÓN NGON NHẤT
    # -----------------------------------------------------

    elif "ngon nhất" in prompt.lower():

        answer = """
😋 **Món được KimChin gợi ý:**

🧋 Trà sữa matcha  
🧋 Trà sữa truyền thống  
☕ Bạc xỉu  
☕ Latte  

Đây là những món KimChin có thể giới thiệu cho khách thử. 
Bé có thể chọn theo khẩu vị mình thích nha 💙
"""

    # -----------------------------------------------------
    # MÓN GIÁ CAO NHẤT
    # -----------------------------------------------------

    elif "giá cao nhất" in prompt.lower():

        max_price = 0
        max_items = []

        for loai, drinks in menu.items():

            for name, price in drinks.items():

                if price > max_price:
                    max_price = price
                    max_items = [name]

                elif price == max_price:
                    max_items.append(name)

        answer = (
            f"💎 Món có giá cao nhất hiện tại là:\n\n"
            f"**{', '.join(max_items)}**\n\n"
            f"💰 Giá: **{max_price:,} VNĐ/ly** "
            f"(chưa bao gồm size và topping)."
        )

    # -----------------------------------------------------
    # MÓN RẺ NHẤT
    # -----------------------------------------------------

    elif "rẻ nhất" in prompt.lower():

        min_price = min(
            price
            for drinks in menu.values()
            for price in drinks.values()
        )

        min_items = []

        for loai, drinks in menu.items():

            for name, price in drinks.items():

                if price == min_price:
                    min_items.append(name)

        answer = (
            f"💵 Món có giá thấp nhất là:\n\n"
            f"**{', '.join(min_items)}**\n\n"
            f"Giá: **{min_price:,} VNĐ/ly**."
        )

    # -----------------------------------------------------
    # MÓN YÊU THÍCH
    # -----------------------------------------------------

    elif "yêu thích" in prompt.lower():

        answer = """
⭐ **Một số món KimChin gợi ý:**

🧋 Trà sữa truyền thống  
🧋 Trà sữa matcha  
☕ Bạc xỉu  
☕ Latte  

Bé có thể thử những món này nếu chưa biết chọn món nào nha 💙
"""

    # -----------------------------------------------------
    # TÍNH BILL
    # -----------------------------------------------------

    elif "bill" in prompt.lower():

        answer = """
🧾 **Cách tính bill tại KimChin:**

**Giá món + giá size + giá topping**
× **số lượng**

Nếu order nhiều món thì hệ thống sẽ cộng thành **tổng bill**.

Ví dụ:

🧋 Trà sữa matcha: 35.000 VNĐ  
📏 Size L: +5.000 VNĐ  
🧋 Topping: +5.000 VNĐ  

➡️ Đơn giá = 45.000 VNĐ

Nếu mua 2 ly:

➡️ **45.000 × 2 = 90.000 VNĐ**
"""

    # -----------------------------------------------------
    # XIN CHÀO
    # -----------------------------------------------------

    elif "xin chào" in prompt.lower() or "hello" in prompt.lower():

        answer = """
👋 Xin chào bé!

Chào mừng bé đến với **KimChin Tea & Coffee** 🧋☕

Bé cần chị tư vấn món, size, topping hay tính bill thì cứ hỏi nha 💙
"""

    # -----------------------------------------------------
    # CẢM ƠN
    # -----------------------------------------------------

    elif "cảm ơn" in prompt.lower():

        answer = """
🥰 Không có gì nha bé!

KimChin rất vui được phục vụ bé 💙🧋
"""

    # -----------------------------------------------------
    # CÂU HỎI KHÁC
    # -----------------------------------------------------

    else:

        answer = """
🤖 KimChin chưa hiểu câu hỏi này.

Bé có thể hỏi:

🧋 Menu có những món gì?

😋 Món nào ngon nhất?

💎 Món nào giá cao nhất?

💵 Món nào rẻ nhất?

⭐ Món nào được yêu thích?

📏 Có những size nào?

🥤 Có những topping nào?

🧾 Tính bill như thế nào?
"""

    # -----------------------------------------------------
    # HIỂN THỊ CÂU TRẢ LỜI
    # -----------------------------------------------------

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    st.rerun()
