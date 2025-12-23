import cv2
import numpy as np
import random

# Warna Bounding Box (Format BGR untuk OpenCV)
COLOR_CRITICAL = (0, 0, 255) # Merah
COLOR_MINOR = (0, 255, 255)  # Kuning
COLOR_GOOD = (0, 255, 0)     # Hijau

def simulate_ai_detection(frame):
    """
    Fungsi ini mensimulasikan model AI (YOLO/CNN) yang mendeteksi objek
    pada setiap frame video.
    """
    # Ambil dimensi frame
    height, width = frame.shape[:2]
    
    # --- SIMULASI MODEL PREDICTION ---
    # Di sini nanti Anda ganti dengan: results = model(frame)
    
    # Kita buat simulasi deteksi random agar terlihat seolah-olah AI bekerja
    # Probabilitas muncul deteksi
    if random.random() < 0.3: 
        # Koordinat Box Random (Simulasi lokasi kerusakan)
        x1 = random.randint(50, width - 150)
        y1 = random.randint(50, height - 150)
        x2 = x1 + random.randint(50, 200)
        y2 = y1 + random.randint(50, 200)
        
        # Tentukan jenis kerusakan random
        damage_type = random.choice(["Retak (Crack)", "Noda (Stain)", "Goresan", "Cat Kelupas"])
        confidence = random.randint(75, 99)
        
        # 1. Gambar Kotak (Bounding Box)
        cv2.rectangle(frame, (x1, y1), (x2, y2), COLOR_CRITICAL, 2)
        
        # 2. Tambahkan Label & Confidence
        label = f"{damage_type} {confidence}%"
        
        # Background label agar terbaca
        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w, y1), COLOR_CRITICAL, -1)
        
        # Teks Putih
        cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    return frame