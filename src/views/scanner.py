import streamlit as st
import database as db  # Import database controller
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import utils # Pastikan utils.py ada untuk simulasi deteksi
import cv2
import tempfile
import time

# --- LOGIKA VIDEO PROCESSING (TETAP SAMA) ---
class VideoProcessor(VideoTransformerBase):
    def transform(self, frame):
        img = frame.to_ndarray(format="bgr24")
        annotated_img = utils.simulate_ai_detection(img) # Menggunakan fungsi utils Anda
        return annotated_img

def show():
    # 1. Inisialisasi DB saat halaman dibuka
    db.init_db()

    st.title("📹 Live AI Inspector")
    
    # --- A. METADATA LOKASI (WAJIB) ---
    with st.container():
        st.info("ℹ️ Tentukan lokasi sebelum memulai pemindaian.")
        c1, c2 = st.columns(2)
        lokasi_gedung = c1.selectbox("Gedung", ["FPMIPA A", "FPMIPA B", "Lab Fisika", "Gedung JICA"])
        lokasi_ruang = c2.text_input("Ruangan / Lantai", placeholder="Contoh: R. 304")

    st.divider()

    # --- B. VIDEO STREAM INPUT ---
    mode = st.radio("Metode Input:", ["Live Camera (Real-time)", "Upload Video Rekaman"], horizontal=True)

    if mode == "Live Camera (Real-time)":
        col_vid, col_stat = st.columns([2, 1])
        with col_vid:
            webrtc_streamer(
                key="facility-scanner",
                video_processor_factory=VideoProcessor,
                rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
                media_stream_constraints={"video": True, "audio": False},
            )
        with col_stat:
            st.warning("📡 AI Model Active")
            st.metric("Latency", "24ms", "-2ms")
            st.caption("Deteksi objek berjalan secara real-time pada frame video.")

    elif mode == "Upload Video Rekaman":
        uploaded_video = st.file_uploader("Upload video audit (.mp4)", type=["mp4", "avi"])
        if uploaded_video:
            tfile = tempfile.NamedTemporaryFile(delete=False) 
            tfile.write(uploaded_video.read())
            vf = cv2.VideoCapture(tfile.name)
            
            stframe = st.empty()
            while vf.isOpened():
                ret, frame = vf.read()
                if not ret: break
                processed_frame = utils.simulate_ai_detection(frame)
                stframe.image(cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB), width='stretch')
                time.sleep(0.01)
            vf.release()

    # --- C. FORM VALIDASI & COMMIT DATABASE ---
    st.divider()
    st.subheader("📝 Verifikasi Hasil & Simpan")

    with st.form("save_form"):
        # Form ini ceritanya terisi otomatis oleh hasil deteksi video terakhir
        c_res1, c_res2 = st.columns(2)
        deteksi_ai = c_res1.selectbox("Objek Terdeteksi (Hasil AI)", ["Retak (Crack)", "Noda Dinding", "Plafond Bocor", "Ubin Pecah"])
        score_ai = c_res2.slider("Confidence Score", 0, 100, 88)
        
        catatan = st.text_area("Catatan Auditor (Opsional)")
        
        submitted = st.form_submit_button("💾 SIMPAN KE DATABASE", width='stretch', type="primary")
        
        if submitted:
            if not lokasi_ruang:
                st.error("⚠️ Harap isi Lokasi Ruangan di bagian atas!")
            else:
                # Logic penentuan status
                status_final = "Critical" if score_ai < 60 else "Minor"
                if score_ai > 90: status_final = "Good"

                # PANGGIL FUNGSI INSERT DATABASE
                success = db.create_laporan(
                    gedung=lokasi_gedung,
                    ruangan=lokasi_ruang,
                    jenis=deteksi_ai,
                    confidence=score_ai,
                    status=status_final,
                    deskripsi=catatan
                )
                
                if success:
                    st.success("✅ Data berhasil disimpan ke Database!")
                else:
                    st.error("❌ Gagal menyimpan ke database.")