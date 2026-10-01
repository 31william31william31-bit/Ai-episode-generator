import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="AI Episode Generator", page_icon="🎬", layout="centered")

st.title("🎬 AI Episode & Face Swap Generator")
st.write("ဖုန်းဖြင့် အလွယ်တကူ အသုံးပြုနိုင်သော ဇာတ်လမ်း အပိုင်းများ ထုတ်လုပ်သည့် စနစ်")

# Initialize session state so results don't disappear on click
if "generated" not in st.session_state:
    st.session_state.generated = False

# --- 1. User Inputs ---
st.header("1. ဇာတ်လမ်း အချက်အလက်များ ထည့်သွင်းရန်")
prompt = st.text_area("ဇာတ်လမ်း Prompt ထည့်ပါ:", "A dramatic cinematic sequence of a single young woman showing an emotional arc...")

uploaded_file = st.file_uploader("သရုပ်ဆောင်ပုံ (Face Image) တင်ရန်", type=["jpg", "png", "jpeg"])

episode_count = st.number_input("ဘယ်နှစ်ပိုင်း (Episodes) လိုချင်လဲ:", min_value=1, max_value=20, value=10)

# --- 2. Generation Process ---
st.header("2. ဗီဒီယို ထုတ်လုပ်ခြင်း")

if st.button("🚀 အပိုင်းများ စတင်ထုတ်လုပ်မည်") or st.session_state.generated:
    if uploaded_file is not None or st.session_state.generated:
        if not st.session_state.generated:
            # Show progress only on first click
            st.image(uploaded_file, caption="ရွေးချယ်ထားသော ဇာတ်ကောင်ပုံ", width=150)
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i in range(1, episode_count + 1):
                status_text.text(f"အပိုင်း {i} / {episode_count} ကို ဖန်တီးနေသည် (AI Video + Face Swap)...")
                time.sleep(0.5) 
                progress_bar.progress(i / episode_count)
            
            st.session_state.generated = True
            st.balloons()
        
        st.success("🎉 အပိုင်းအားလုံး အောင်မြင်စွာ ပြီးဆုံးပါပြီ!")
        
        # --- Download Section ---
        st.markdown("### 📥 ဖိုင်များ ဒေါင်းလုဒ်ဆွဲရန်")
        st.write("ထုတ်လုပ်ပြီးသော ဗီဒီယို အပိုင်းများကို အောက်ပါခလုတ်များမှတစ်ဆင့် ဒေါင်းလုဒ် ဆွဲနိုင်ပါပြီ -")
        
        for i in range(1, episode_count + 1):
            fake_video_data = f"This is video content for Episode {i}".encode('utf-8')
            st.download_button(
                label=f"⬇️ အပိုင်း {i} (Episode {i}) ဒေါင်းလုဒ်ဆွဲရန်",
                data=fake_video_data,
                file_name=f"Episode_{i}.mp4",
                mime="video/mp4",
                key=f"download_{i}"  # Unique key for each button to prevent state loss
            )
        
    else:
        st.warning("⚠️ ကျေးဇူးပြု၍ ဇာတ်ကောင်မျက်နှာပုံ (Face Image) ကို အရင် တင်ပေးပါ။")
