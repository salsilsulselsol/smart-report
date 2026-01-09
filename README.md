# FPMIPA SmartReport

**Platform Audit Fasilitas Kampus Berbasis Artificial Intelligence**

FPMIPA SmartReport adalah sistem cerdas yang dirancang untuk mengotomatisasi proses pelaporan kerusakan inventaris kampus, khususnya kursi kuliah.

Sistem ini memanfaatkan kekuatan **Roboflow** untuk manajemen dataset dan proses *inference* model Computer Vision (YOLOv11), yang kemudian diintegrasikan dengan **Streamlit** sebagai antarmuka pengguna. Aplikasi ini memungkinkan pengguna memindai kondisi fasilitas secara real-time untuk mendapatkan penilaian kondisi otomatis (*scoring*) dan pencatatan digital ke database.

Proyek ini dikembangkan untuk memenuhi tugas akhir mata kuliah Sistem Cerdas.

## Fitur Utama

* **🔍 AI Scanner (Powered by Roboflow):** Mendeteksi kerusakan spesifik (dudukan rusak, kursi sobek, meja hilang) menggunakan model YOLOv11 yang di-hosting via Roboflow Inference.
* **📹 Dual Input Method:** Mendukung pemindaian langsung via kamera HP (Real-time WebRTC) atau unggah file video.
* **📊 Automated Scoring:** Algoritma penilaian otomatis dengan logika *Critical Failure* (skor turun drastis jika kursi tidak bisa digunakan).
* **📂 Database Terpusat:** Riwayat laporan tersimpan otomatis menggunakan SQLite dan dapat difilter berdasarkan status kerusakan.
* **🎨 Modern UI:** Antarmuka responsif dengan gaya *Glassmorphism* dan dukungan *Dark Mode*.

## Teknologi yang Digunakan

* **Bahasa:** Python 3.11+
* **Framework Web:** Streamlit
* **Computer Vision & AI:**
* **Roboflow:** Digunakan untuk *Dataset Management*, *Annotation*, dan *Hosted Inference API*.
* 🔗 **Lihat Dataset & Model:** [universe.roboflow.com/zzzidan/my-first-project-pa6fg](https://www.google.com/search?q=https://universe.roboflow.com/zzzidan/my-first-project-pa6fg)
* **YOLOv11:** Model deteksi objek.
* **OpenCV:** Pemrosesan frame video.
* **Database:** SQLite (SQLAlchemy)
* **Data Processing:** Pandas, NumPy

## ⚙️ Cara Instalasi & Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi di komputer lokal Anda:

### 1. Clone Repository
```
git clone [https://github.com/username-anda/smart-report.git](https://www.google.com/search?q=https://github.com/username-anda/smart-report.git)
cd smart-report
```
### 2. Setup Virtual Environment (Disarankan)
```
python -m venv venv
```
# Untuk Windows:
```
venv\Scripts\activate
```
# Untuk Mac/Linux:
```
source venv/bin/activate
```
### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Konfigurasi API Key Roboflow (PENTING)

Aplikasi ini memerlukan API Key dari **Roboflow** agar fitur AI berjalan. Buat file baru bernama `.streamlit/secrets.toml` di dalam folder proyek, lalu isi dengan kredensial Anda:

# File: `.streamlit/secrets.toml`

ROBOFLOW_API_KEY = "masukkan_api_key_roboflow_anda"
ROBOFLOW_WORKSPACE = "nama_workspace_roboflow"
ROBOFLOW_WORKFLOW = "id_workflow_atau_model"

*(Catatan: Pastikan Anda sudah memiliki workspace di Roboflow dan model yang sudah dilatih/deploy)*

### 5. Jalankan Aplikasi
```
streamlit run src/main.py
```
## 📝 Struktur Laporan & Penilaian

Sistem menggunakan logika penilaian sebagai berikut:

* **Rusak Berat (Critical):** Jika terdeteksi *dudukan_rusak* atau *tanpa_meja*. Skor otomatis turun drastis (< 50%).
* **Perlu Perbaikan:** Jika terdeteksi kerusakan ringan seperti *sobek*.
* **Layak Pakai:** Jika tidak ada kerusakan signifikan (Skor > 85%).

## 👥 Tim Pengembang (Original Author)

Aplikasi ini awalnya dikembangkan oleh **Kelompok 5 - Sistem Cerdas**:

1. Muhammad Daffa Ma'arif
2. Datuk Daneswara Raditya Samsura
3. Faisal Nur Qolbi
4. Mochamad Zidan Rusdhiana

---

*Dikembangkan dengan ❤️ untuk FPMIPA UPI.*
