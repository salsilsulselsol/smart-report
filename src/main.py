import streamlit as st
from streamlit_option_menu import option_menu
from views import home, scanner, history
import database as db

# --- CONFIG HALAMAN ---
st.set_page_config(
    page_title="FPMIPA AI",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="expanded"  # Sidebar terbuka otomatis di Desktop
)

# --- CSS SETUP ---
st.markdown("""
    <style>
        /* Mengubah warna sidebar agar sesuai tema malam */
        section[data-testid="stSidebar"] {
            background-color: #0f172a;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* PENTING: Jangan menyembunyikan header secara total agar tombol Hamburger (☰) tetap ada */
        /* Kita hanya menyembunyikan tombol 'Deploy' dan footer bawaan Streamlit */
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        /* Mengatur padding atas agar konten tidak tertutup header */
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    # Logo / Header Sidebar
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="color: #29B5E8; margin:0; font-weight: 800;">FPMIPA AI</h2>
            <p style="color: #64748b; font-size: 0.8rem;">Facility Audit System</p>
        </div>
    """, unsafe_allow_html=True)

    # Menu Pilihan
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Scanner AI", "Data Laporan", "Pengaturan"],
        icons=["grid-fill", "camera-video-fill", "file-earmark-text-fill", "gear-fill"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#29B5E8", "font-size": "16px"}, 
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "color": "#94a3b8",
            },
            "nav-link-selected": {
                "background-color": "rgba(41, 181, 232, 0.15)", 
                "color": "#29B5E8",
                "border-left": "3px solid #29B5E8",
                "font-weight": "bold"
            },
        }
    )
    
    st.markdown("---")
    st.caption("© 2025 FPMIPA System")

# --- PAGE ROUTING ---
if selected == "Dashboard":
    home.show()

elif selected == "Scanner AI":
    scanner.show()

elif selected == "Data Laporan":
    # Debugging error database jika ada
    try:
        history.show()
    except Exception as e:
        st.error(f"Terjadi kesalahan memuat database: {e}")
        # Tombol darurat untuk reset DB jika rusak
        if st.button("Reset Database"):
            db.init_db()
            st.rerun()

elif selected == "Pengaturan":
    st.title("⚙️ Pengaturan")
    st.info("Menu konfigurasi user.")