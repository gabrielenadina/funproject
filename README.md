# Fun Project 1 Ruang Guru Skill Academy
# Personality Quiz with Streamlit App
Mini quiz sederhana yang dibuat menggunakan **Python + Streamlit**.
Di mini quiz ini, user akan menjawab delapan pertanyaan dan mini quiz app akan menentukan profesi bisnis mana yang paling cocok untuk mereka sesuai jawaban yang dipilih.
---
## Tentang Mini Quiz 
**Tidak ada benar atau salah di quiz ini**.
Setiap jawaban akan direkam menjadi **personality role score** dan hasil akhir akan menunjukkan karakter dominan user
### Profesi Bisnis yang Tersedia
- **HR Manager** = people-oriented, empathetic, pendengar yang baik
- **Project Manager** = terorganisir, efisien, execution-focused
- **Marketing & Sales** = persuasif, ekspresif, communication-driven
- **Finance Manager** = numbers-oriented, manajemen resiko, analytical

## How It Works
- Setiap pertanyaan memiliki **empat** pilihan jawaban.
- Setiap pilihan jawaban dipetakan ke **satu peran (role)** tertentu: HR (1st options), PM (2nd options), Marketing (3rd options), Finance (4th options)
- Ketika pengguna memilih sebuah jawaban, peran tersebut akan mendapatkan **+1 poin**
- Setelah seluruh pertanyaan dijawab, skor dari setiap peran akan dibandingkan
- Peran dengan **skor tertinggi** akan menjadi hasil akhir.
- Jika terjadi skor seri, apapun itu, user akan mendapat hasil **ALL ROLES**

## How to Run It
Install & Run:
- pip install streamlit
- pip install streamlit-extras
