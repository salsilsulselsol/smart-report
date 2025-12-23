import streamlit as st

def load_css():
    st.markdown("""
        <style>
            /* --- 1. IMPORT FONT MODERN (Inter) --- */
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
            
            html, body, [class*="css"]  {
                font-family: 'Inter', sans-serif;
            }

            /* --- 2. BACKGROUND BERGRADASI (MENGGANTI HITAM POLOS) --- */
            /* Ini menargetkan container utama Streamlit */
            .stApp {
                background: radial-gradient(circle at 50% 10%, #1e293b 10%, #0f172a 40%, #020617 100%);
                background-attachment: fixed;
            }

            /* --- 3. MENYEMBUNYIKAN ELEMEN BAWAAN --- */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            /* --- 4. GLASSMORPHISM CARD (KEREN!) --- */
            .glass-card {
                background: rgba(30, 41, 59, 0.4); /* Transparan */
                backdrop-filter: blur(12px);       /* Efek Buram */
                -webkit-backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 24px;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
                transition: transform 0.2s ease-in-out, box-shadow 0.2s;
                margin-bottom: 20px;
            }

            /* Efek Hover (Card Melayang Sedikit) */
            .glass-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 40px rgba(41, 181, 232, 0.2); /* Glow Biru */
                border: 1px solid rgba(41, 181, 232, 0.3);
            }

            /* --- 5. TYPOGRAPHY & HERO TEXT --- */
            .hero-title {
                font-size: 3.5rem;
                font-weight: 800;
                background: linear-gradient(90deg, #29B5E8, #3b82f6);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0;
                text-align: center;
            }
            
            .hero-subtitle {
                font-size: 1.2rem;
                color: #94a3b8;
                text-align: center;
                margin-bottom: 40px;
            }

            /* --- 6. CUSTOM METRIC VALUE --- */
            .metric-value {
                font-size: 2.5rem;
                font-weight: 700;
                color: #f1f5f9;
                margin-top: 5px;
            }
            
            .metric-label {
                font-size: 0.9rem;
                text-transform: uppercase;
                letter-spacing: 1.5px;
                color: #64748b;
                font-weight: 600;
            }

            /* --- 7. BUTTON MODERN --- */
            div.stButton > button {
                background: linear-gradient(90deg, #29B5E8 0%, #2563eb 100%);
                color: white;
                border: none;
                padding: 0.6rem 1.2rem;
                border-radius: 8px;
                font-weight: 600;
                transition: all 0.3s ease;
            }
            div.stButton > button:hover {
                box-shadow: 0 0 15px rgba(41, 181, 232, 0.6);
            }
        </style>
    """, unsafe_allow_html=True)

def render_glass_metric(label, value, delta=None, color="white"):
    """
    Render kartu metrik dengan gaya Glassmorphism
    """
    delta_html = f"<span style='color: #4ade80; background: rgba(74, 222, 128, 0.1); padding: 2px 8px; border-radius: 12px; font-size: 0.8rem; margin-left: 10px;'>▲ {delta}</span>" if delta else ""
    
    st.markdown(f"""
        <div class="glass-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">
                {value} {delta_html}
            </div>
        </div>
    """, unsafe_allow_html=True)