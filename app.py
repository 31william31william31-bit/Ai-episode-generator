import streamlit as st
import os

# Page Configuration
st.set_page_config(page_title="Video Burmese Subtitle Hub", page_icon="🎬", layout="centered")

st.title("🎬 Video to Burmese Subtitle & Editor Hub")
st.write("ဗီဒီယိုဖိုင် တင်လိုက်ရုံဖြင့် မြန်မာဘာသာပြန် စာတန်းထိုးပေးပြီး၊ လိုအပ်ပါက ချက်ချင်း တည်းဖြတ်နိုင်သော စနစ်")

# Initialize session state
if "subtitles_generated" not in st.session_state:
    st.session_state.subtitles_generated = False

# --- 1. Video Upload ---
st.header("1. ဗီဒီယိုဖိုင် တင်ရန်")
uploaded_video = st.file_uploader("ဗီဒီယိုဖိုင် (MP4) တင်ပါ:", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Save uploaded video temporarily
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_video.getbuffer())
    
    st.video("temp_video.mp4")
    st.success("✅ ဗီဒီယို တင်ခြင်း အောင်မြင်ပါသည်။")

    # --- 2. Subtitle Generation & Editing ---
    st.header("2. မြန်မာဘာသာပြန် စာတန်းထိုးများ (Editing Panel)")
    st.info("💡 အောက်ပါ စာတန်းထိုးများကို လိုအပ်သလို ဝင်ရောက် ပြင်ဆင်နိုင်ပါသည်။")

    # Default Burmese subtitles sample for video scenes
    if "subs" not in st.session_state:
        st.session_state.subs = {
            1: "အပိုင်း (၁) - ဆင်းရဲသားလို ဟန်ဆောင်နေသော သူဌေးငယ်",
            2: "အပိုင်း (၂) - မထီမဲ့မြင် ပြုခံရချိန် ငြိမ်သက်နေခြင်း",
            3: "အပိုင်း (၃) - ဘလက်ကတ် ကတ်ပြား ရရှိသွားချိန်",
            4: "အပိုင်း (၄) - ကုမ္ပဏီကြီးထဲသို့ ခမ်းနားစွာ ဝင်ရောက်လာခြင်း",
            5: "အပိုင်း (၅) - ကုမ္ပဏီကို တစ်ခါတည်း ဝယ်ယူလိုက်သည့် အချိန်"
        }

    # Editable text fields for each subtitle line
    edited_subs = {}
    for i in range(1, 6):
        edited_subs[i] = st.text_input(f"စဥ် (Scene {i}) စာတန်းထိုး:", value=st.session_state.subs[i], key=f"sub_edit_{i}")

    # Save button for edits
    if st.button("💾 ပြင်ဆင်ချက်များကို သိမ်းမည်"):
        st.session_state.subs = edited_subs
        st.success("✨ ဘာသာပြန် စာတန်းထိုးများကို အောင်မြင်စွာ သိမ်းဆည်းပြီးပါပြီ!")

    # --- 3. Export & Download ---
    st.header("3. စာတန်းထိုးပါ ဗီဒီယို (သို့မဟုတ် Subtitle ဖိုင်) ထုတ်ယူရန်")
    
    # Generate .SRT file content from current edited subs
    srt_content = ""
    for i in range(1, 6):
        srt_content += f"{i}\n00:0{i}:00,000 --> 00:0{i}:05,000\n{st.session_state.subs[i]}\n\n"

    st.download_button(
        label="⬇️ မြန်မာဘာသာပြန် စာတန်းထိုးဖိုင် (.srt) ဒေါင်းလုဒ်ဆွဲရန်",
        data=srt_content.encode('utf-8'),
        file_name="Burmese_Subtitles.srt",
        mime="text/plain"
    )

else:
    st.info("ℹ️ စတင်ရန် ကျေးဇူးပြု၍ ဗီဒီယိုဖိုင် တစ်ခုကို အထက်ပါ နေရာတွင် တင်ပေးပါ။")
