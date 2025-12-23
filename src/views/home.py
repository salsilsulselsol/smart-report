import streamlit as st
# Jika styles.py Anda masih digunakan, tetap import. 
# Namun kode di bawah ini sudah saya buat self-contained (mandiri) agar desainnya konsisten.
# from styles import render_glass_metric 

def local_css():
    st.markdown("""
        <style>
            /* HERO STYLES */
            .hero-container {
                text-align: center;
                padding: 40px 0;
                animation: fadeIn 1s ease-in;
            }
            .hero-title {
                font-size: 3rem !important;
                font-weight: 800 !important;
                background: -webkit-linear-gradient(45deg, #29B5E8, #4ade80);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                margin-bottom: 0 !important;
            }
            .hero-subtitle {
                color: #94a3b8;
                font-size: 1.2rem;
                margin-top: 10px;
            }

            /* GLASS CARD STYLES */
            .glass-metric {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                transition: transform 0.2s;
            }
            .glass-metric:hover {
                transform: translateY(-5px);
                border-color: #29B5E8;
            }
            .metric-label {
                color: #94a3b8;
                font-size: 0.9rem;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            .metric-value {
                color: white;
                font-size: 2rem;
                font-weight: 700;
                margin: 5px 0;
            }
            .metric-delta {
                font-size: 0.8rem;
                padding: 2px 8px;
                border-radius: 10px;
                display: inline-block;
            }

            /* ACTIVITY ITEM */
            .activity-item {
                background: rgba(255,255,255,0.03);
                border-left: 3px solid #29B5E8;
                padding: 15px;
                border-radius: 0 10px 10px 0;
                margin-bottom: 12px;
                display: flex;
                align-items: center;
            }
        </style>
    """, unsafe_allow_html=True)

def render_metric_card(label, value, delta, delta_color="#4ade80"):
    st.markdown(f"""
        <div class="glass-metric">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-delta" style="background: {delta_color}20; color: {delta_color};">
                {delta}
            </div>
        </div>
    """, unsafe_allow_html=True)

def show():
    # Load CSS Lokal
    local_css()

    # --- HERO SECTION ---
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">FPMIPA SmartReport</h1>
            <p class="hero-subtitle">Platform Audit Fasilitas Kampus Berbasis Artificial Intelligence</p>
        </div>
    """, unsafe_allow_html=True)

    # --- MAIN STATS ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        render_metric_card("Total Laporan", "1,248", "↗ +12 Hari ini", "#29B5E8") # Biru
    with col2:
        render_metric_card("Fasilitas Rusak", "86", "⚠ Perlu Tindakan", "#ef4444") # Merah
    with col3:
        render_metric_card("Efisiensi Perbaikan", "94%", "⚡ High Performance", "#4ade80") # Hijau

    st.markdown("---")

    # --- CONTENT GRID (2 Kolom) ---
    # Menggunakan layout 2 kolom: Kiri (Aktivitas) lebih lebar, Kanan (Info/Tips)
    c_left, c_right = st.columns([2, 1])

    with c_left:
        st.subheader("⚡ Aktivitas Terbaru")
        
        activities = [
            {"user": "Mahasiswa Ilkom", "action": "melaporkan", "item": "Kursi R. W-204", "time": "2 menit lalu", "icon": "📸", "color": "#29B5E8"},
            {"user": "Staff Sarpras", "action": "memperbaiki", "item": "Meja Lab A", "time": "1 jam lalu", "icon": "🛠️", "color": "#4ade80"},
            {"user": "System AI", "action": "mendeteksi", "item": "Retakan Dinding", "time": "3 jam lalu", "icon": "🤖", "color": "#f59e0b"},
        ]

        for act in activities:
            st.markdown(f"""
                <div class="activity-item" style="border-left-color: {act['color']};">
                    <div style="font-size: 1.5rem; margin-right: 15px; width: 40px; text-align: center;">{act['icon']}</div>
                    <div style="flex-grow: 1;">
                        <div style="color: #e2e8f0; font-weight: 500; font-size: 0.95rem;">
                            <span style="color: {act['color']}; font-weight: bold;">{act['user']}</span> 
                            {act['action']} <b>{act['item']}</b>
                        </div>
                        <div style="color: #64748b; font-size: 0.8rem; margin-top: 2px;">⏱ {act['time']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    with c_right:
        st.subheader("💡 Quick Tips")
        
        # Menggunakan st.info native tapi tetap rapi
        st.info("**Scan Kerusakan**\nGunakan menu 'Scanner' untuk deteksi otomatis menggunakan kamera.")
        
        st.warning("**Prioritas Tinggi**\nCek Gedung JICA Lt. 3 karena ada laporan kebocoran atap.")

        st.markdown("""
            <div style="margin-top: 20px; padding: 15px; background: rgba(41, 181, 232, 0.1); border-radius: 10px; border: 1px dashed #29B5E8;">
                <h4 style="margin:0; font-size: 1rem; color: #29B5E8;">Status Server</h4>
                <p style="margin:5px 0 0 0; font-size: 0.8rem; color: #94a3b8;">
                    AI Model: <b>v2.4.1 (Online)</b><br>
                    Latency: <b>24ms</b>
                </p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()