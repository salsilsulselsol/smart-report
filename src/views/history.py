import streamlit as st
import database as db
import pandas as pd

def show():
    # Pastikan DB init
    db.init_db()
    
    st.title("📂 Database Laporan")
    
    # 1. FETCH DATA DARI SQLITE
    df = db.get_all_laporan_as_df()
    
    # --- [FIX UTAMA ADA DI SINI] ---
    # Konversi kolom 'timestamp' dari String (Text SQLite) ke Datetime Object (Pandas)
    if not df.empty and 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    # -------------------------------
    
    # 2. METRIK RINGKASAN
    if not df.empty:
        total, critical = db.get_summary_stats()
        
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Laporan", total)
        m2.metric("Status Critical", critical)
        
        # Sekarang aman digunakan .strftime() karena sudah jadi datetime object
        try:
            last_update = df['timestamp'].iloc[0].strftime("%d %b %H:%M")
        except Exception:
            last_update = "-"
            
        m3.metric("Laporan Terakhir", last_update)
    
    st.divider()

    # 3. TAMPILKAN TABEL
    if not df.empty:
        # Filter UI
        col_filter, _ = st.columns([1, 2])
        # Gunakan list unique() dari pandas untuk opsi filter
        status_options = df['status'].unique() if 'status' in df.columns else []
        status_filter = col_filter.multiselect("Filter Status", status_options, default=status_options)
        
        # Apply Filter
        if 'status' in df.columns:
            df_filtered = df[df['status'].isin(status_filter)]
        else:
            df_filtered = df
        
        st.dataframe(
            df_filtered,
            width='stretch',
            hide_index=True,
            column_config={
                "id": st.column_config.NumberColumn("ID", width="small"),
                "timestamp": st.column_config.DatetimeColumn("Waktu Lapor", format="D MMM, HH:mm"),
                "confidence_score": st.column_config.ProgressColumn(
                    "AI Confidence", format="%.1f%%", min_value=0, max_value=100
                ),
                "status": st.column_config.TextColumn("Status"),
                "jenis_kerusakan": "Deteksi AI",
                "gedung": "Gedung",
                "ruangan": "Ruangan"
            }
        )
        
        # Download Button
        csv = df_filtered.to_csv(index=False).encode('utf-8')
        st.download_button(
            "⬇️ Export to CSV",
            data=csv,
            file_name='fpmipa_audit_report.csv',
            mime='text/csv',
        )
    else:
        st.info("Database masih kosong. Silakan lakukan scanning di menu 'Scanner AI'.")