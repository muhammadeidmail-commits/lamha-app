import streamlit as st
import time

# --- إعدادات الصفحة والهوية البصرية ---
st.set_page_config(
    page_title="لَمحة - Lamha",
    page_icon="👁️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- تصميم الواجهة باستخدام CSS (Dark Theme, Purple & Cyan Glow) ---
st.markdown("""
    <style>
    /* الخلفية العامة للتطبيق */
    .stApp {
        background-color: #0A0A0A;
        color: #FFFFFF;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* الهيدر الزجاجي */
    .glass-header {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 30px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }
    
    .logo-text {
        background: linear-gradient(45deg, #A855F7, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
    }
    
    /* تخصيص منطقة الرفع */
    .stUploader {
        border: 2px dashed #A855F7 !important;
        border-radius: 15px !important;
        background-color: #121212 !important;
        padding: 20px !important;
        transition: all 0.3s ease;
    }
    .stUploader:hover {
        border-color: #06B6D4 !important;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.3);
    }
    
    /* بطاقة النتائج الشفافة */
    .result-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(168, 85, 247, 0.2);
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.1);
    }
    
    /* الأزرار المخصصة */
    .stButton>button {
        background: linear-gradient(90deg, #A855F7, #06B6D4) !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: bold !important;
        width: 100%;
        transition: transform 0.2s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.4);
    }
    </style>
""", unsafe_allow_html=True)

# --- محاكاة محرك الذكاء الاصطناعي لاستخراج البرومبت ---
def analyze_content(uploaded_file):
    time.sleep(3) # أنيميشن الانتظار
    prompt_output = (
        "Cinematic shot, highly detailed cyberpunk street, neon glowing signs in purple and cyan, "
        "rainy night with reflections on the asphalt, shot on 35mm lens, anamorphic style, depth of field, --ar 16:9 --v 6.0"
    )
    return prompt_output

# --- الهيدر الرئيسي (Header) ---
st.markdown("""
    <div class="glass-header">
        <div class="logo-text">👁️ لَمحة - Lamha</div>
        <p style="color: #9CA3AF; margin-top: 10px;">أداتك السحرية لفك شفرة الإبداع وتحويل البصريات إلى نصوص (Prompts)</p>
    </div>
""", unsafe_allow_html=True)

# --- نظام التبويبات (Tabs) ---
tab1, tab2, tab3 = st.tabs(["🚀 الرئيسية", "🖼️ المعرض والاستكشاف", "⚙️ الإعدادات"])

# ==================== التبويب الأول: الرئيسية ====================
with tab1:
    st.write("")
    uploaded_file = st.file_uploader("ارمي الصورة أو الفيديو هنا لفك التشفير...", type=["jpg", "jpeg", "png", "mp4"])
    
    if uploaded_file is not None:
        if uploaded_file.type.startswith('image'):
            st.image(uploaded_file, caption='المحتوى المرفوع', use_container_width=True)
        elif uploaded_file.type.startswith('video'):
            st.video(uploaded_file)
            
        st.write("")
        if st.button("✨ ابدأ التحليل العكسي"):
            with st.spinner("🔮 لَمحة تقوم بتحليل العناصر، الإضاءة، وحركة العدسة الآن..."):
                final_prompt = analyze_content(uploaded_file)
            
            st.markdown(f"""
                <div class="result-card">
                    <h4 style="color: #06B6D4; margin-bottom: 10px;">📋 البرومبت المستخرج الجاهز:</h4>
                    <p style="font-family: monospace; background-color: #000000; padding: 15px; border-radius: 8px; border: 1px solid #333; color: #00FFCC;">
                        {final_prompt}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.button("🔗 تجربة مباشرة في Midjourney")
            with col2:
                st.success("تم التجهيز بنجاح! انسخ النص البرمجي واستمتع بالإبداع.")

# ==================== التبويب الثاني: المعرض ====================
with tab2:
    st.markdown("<h3 style='color: #A855F7;'>🔥 إبداعات مجتمع لَمحة</h3>", unsafe_allow_html=True)
    st.text_input("🔍 ابحث عن تصاميم أو برومبتس معينة...", placeholder="أكتب مثلاً: سينمائي، أنمي، طبيعة...")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500", caption="نمط: تجريدي ثلاثي الأبعاد")
        st.code("Abstract 3D flowing ribbons, neon purple accents --v 6.0")
        
    with col2:
        st.image("https://images.unsplash.com/photo-1579783900882-c0d3dad7b119?w=500", caption="نمط: لوحة زيتية كلاسيكية")
        st.code("Classical oil painting, dramatic chiaroscuro lighting, renaissance style")

# ==================== التبويب الثالث: الإعدادات ====================
with tab3:
    st.markdown("<h3 style='color: #06B6D4;'>⚙️ التفضيلات والملف الشخصي</h3>", unsafe_allow_html=True)
    st.write("**نوع الحساب:** 👑 باقة المحترفين (Lamha Pro)")
    engine = st.selectbox("المحرك الافتراضي المفضل لتخصيص النصوص:", ["Midjourney", "Sora (OpenAI)", "Runway Gen-2", "Stable Diffusion"])
    st.toggle("تحسين البرومبت تلقائياً (Smart Enhancer)", value=True)
    st.toggle("تحليل حركة الكاميرا التلقائي للفيديوهات", value=True)
    st.write("---")
    st.button("💳 إدارة اشتراكك وترقية الباقة")
