import streamlit as st

ROLES = ["HR Manager", "Project Manager", "Marketing & Sales", "Finance Manager"]

QUESTIONS = [
    {
        "pertanyaan": "Di grup lagi rame dan tiba-tiba ada yang mulai beda pendapat, kamu biasanya...",
        "pilihan": [
            "Dengerin pendapat semua orang satu-satu",
            "Fokus ke inti masalah: 'yuk fokus ges, biar cepet kelar'",
            "Nenangin suasana sambil nyari cara biar semua bisa setuju",
            "Mantau situasi buat tau setiap keputusan bakal ngarah kemana"
        ]
    },
    {
        "pertanyaan": "Kalau ada rencana jalan bareng, kamu tipe yang...",
        "pilihan": [
            "Mastiin semua orang nyaman: 'semua oke kan? ada yang keberatan gak?",
            "Langsung spam: 'jam berapa? ketemu dimana? pake baju apa?",
            "Bujukin temen-temen biar semua pada ikut",
            "Ngatur budget biar semua sesuai rencana"
        ]
    },
    {
        "pertanyaan": "Lagi nongkrong, tiba-tiba mantan temen datang dan suasana jadi canggung, kamu bakal...",
        "pilihan": [
            "Nyapa duluan sambil liat situasi biar ga making canggung",
            "Langsung alihin pembicaraan ke topik lain (cepet-cepet cari distraksi😣)",
            "Reflek ngejokes biar ga tegang-tegang amat",
            "Main aman aja, gak usah banyak interaksi biar ga ribet"
        ]
    },
     {
        "pertanyaan": "Lagi akan rame-rame di restoran, tiba-tiba ada temen yang komplain kalau makanannya gak enak. Kamu bakal...",
        "pilihan": [
            "Refleks mikir 'eh karyawannya denger gak ya tadi?'",
            "Tetep lanjut makan",
            "Bercanda buat nyairin suasana",
            "Fokus biar situasinya gak melebar"
        ]
    },
    {
        "pertanyaan": "Kamu datang ke tempat baru dan nggak kenal siapa siapa. Apa hal pertama yang kamu pikirin?",
        "pilihan": [
            "'Siapa ya yang kelihatan paling approachable?'",
            "'Gue harus mulai ngapain dulu nih?'",
            "Otomatis cari topik buat mulai ngobrol",
            "Mengamati sekitar dulu sebelum bertindak"
        ]
    },
     {
        "pertanyaan": "Kalau lihat orang panik karena hal sepele, reaksi kamu biasanya...",
        "pilihan": [
            "Pengen nenangin dulu",
            "Pengen nyelesein biar cepet kelar",
            "Reflek ngeyakinin kalau semua bakal baik baik aja (ngejokes dikit biar ga panik)",
            "Langsung ngecek masalahnya memang bisa jadi besar gak"
        ]
    },
     {
        "pertanyaan": "Kamu lagi antre panjang dan tiba-tiba ada drama. Kamu bakal...",
        "pilihan": [
            "Ngerasa kasiahan sama yang kena",
            "Mikirin gimana biar antrian cepet maju",
            "Langsung kepikiran 'wahh seru juga nih' (viralin sih!)",
            "Diem aja biar ga ikut keseret"
        ]
    },
    {
        "pertanyaan": "Rencana kamu tiba tiba berubah tanpa pemberitahuan, kamu bakal...",
        "pilihan": [
            "Mikirin orang-orang yang terlibat gimana",
            "Langsung atur ulang rencana biar tetep jalan",
            "Kepikiran cara ngejelasinnya ke orang lain",
            "Kepikiran efeknya ke semuanya gimana"
        ]
    }
]

def score_quiz(answers):
    scores = {
        "HR Manager": 0,
        "Project Manager": 0,
        "Marketing & Sales": 0,
        "Finance Manager": 0
    }

    for idx, ans in enumerate(answers):
        if ans is not None and idx < len(QUESTIONS) :
            try:
                #Cari jawaban di pilihan
                question = QUESTIONS[idx]

                #Versi jika struktur: QUESTIONS [idx]["pilihan"]
                if "pilihan" in question:
                    pilihan = question["pilihan"]
                else:
                    #Coba format lain
                    pilihan = question.get("options", question.get("choices", []))
                answer_index = QUESTIONS[idx]["pilihan"].index(ans)
                
                #Cari index jawaban
                ans_index = pilihan.index(ans)

                #Tambahkan score sesuai index
                if ans_index == 0:
                    scores["HR Manager"] += 1
                elif ans_index == 1:
                    scores["Project Manager"] += 1
                elif ans_index == 2:
                    scores["Marketing & Sales"] += 1
                elif ans_index == 3:
                    scores["Finance Manager"] += 1
            except (ValueError, IndexError, KeyError):
                #Skip jika ada error
                continue

    return scores

def get_result(scores):
    max_score = max(scores.values())
    top_roles = [role for role, score in scores.items() if score == max_score]
    if len(top_roles) == 1:
        role = top_roles[0]
        if role == "HR Manager":
            return "SELAMAT! KAMU PSIKOLOG GRATIS BUAT SEMUA ORANG. COCOK JADI HR MANAGER"
        elif role == "Project Manager":
            return "SELAMAT! KAMU YANG BIKIN SEMUANYA JALAN MULUS. COCOK JADI PROJECT MANAGER"
        elif role == "Marketing & Sales":
            return "SELAMAT! KAMU JAGO CUAP CUAP. MARKETING ABIEZ NIH BOSS"
        elif role == "Finance Manager":
            return "SELAMAT! KAMU AUTO MIKIR RESIKO DAN PALING PAHAM UANG. COCOK JADI FINANCE MANAGER"
    else:
        return "SELAMAT! KAMU SERBA BISA, COCOK UNTUK SEMUA ROLE!"
        # Jika ada beberapa role dengan skor tertinggi, tampilkan pesan umum

# --- Streamlit UI ---
st.title("PERAN BISNIS APA YANG PAS BUAT KAMU?💼💰")
from streamlit_extras.colored_header import colored_header
colored_header(
    label="Mini Quiz",
    description="Jawab jujur aja...ini bukan tes HR kok😉",
    color_name="blue-70",
)
from streamlit_extras.let_it_rain import rain
rain(
    emoji="💸",
    font_size=35,
    falling_speed=5,
    animation_length="infinite",
)

if "p_index" not in st.session_state:
    st.session_state.p_index = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = [None] * len(QUESTIONS)
if "submitted" not in st.session_state:
    st.session_state.submitted = False

index = st.session_state.p_index
q = QUESTIONS[index]

st.subheader(f"Pertanyaan ke-{index+1} dari {len(QUESTIONS)}")
jawaban = st.radio(
    q["pertanyaan"],
    q["pilihan"],
    index=q["pilihan"].index(st.session_state.jawaban_user[index]) if st.session_state.jawaban_user[index] in q["pilihan"] else 0,
    key=f"radio_{index}"
)
st.session_state.jawaban_user[index] = jawaban

col1, col2 = st.columns([1, 1])
with col1:
    st.button("Back", on_click=lambda: st.session_state.update(p_index=max(0, st.session_state.p_index-1)))
with col2:
    if index == len(QUESTIONS) - 1:
        if st.button("Cek Hasilnya!", icon="😉"):
            if None in st.session_state.jawaban_user:
                st.warning("Eits ada yang belum kejawab tuh!😉")
            else:
                st.session_state.submitted = True
    else:
        st.button("Next", on_click=lambda: st.session_state.update(p_index=min(len(QUESTIONS)-1, st.session_state.p_index+1)))

if st.session_state.submitted:
    scores = score_quiz(st.session_state.jawaban_user)
    result = get_result(scores)
    st.subheader(result)
    if result.startswith("SELAMAT! KAMU PSIKOLOG GRATIS"):
        st.text("Kamu peka sama suasana dan cepat nangkep perasaan orang.\nTanpa sadar, kamu sering jadi penenang, penengah, dan pendengar setia.\nKalau ada drama, kamu bukan nonton—kamu langsung mikir, “ini gimana biar semua baik-baik aja?”\n✨ Tim jalan lebih enak karena kamu peduli sama manusianya, bukan cuma urusannya.")
        st.balloons()
        st.image("https://media4.giphy.com/media/3yvUtiQJwqjUaRj5zS/giphy.gif")
    if result.startswith("SELAMAT! KAMU YANG BIKIN SEMUANYA"):
        st.text("Kepalamu otomatis mikir alur, urutan, dan “abis ini ngapain”.\nKamu bikin hal ribet jadi lebih kebayang dan bisa dijalanin.\nSaat orang lain masih debat, kamu sudah siap bilang, “oke, next step-nya gini ya.”\n✨Kamu bukan paling ribut, tapi paling bikin semuanya kejadian.")
        st.balloons()
        st.image("https://media4.giphy.com/media/maNB0qAiRVAty/giphy.gif")
    if result.startswith("SELAMAT! KAMU JAGO CUAP CUAP"):
        st.text("Kamu jago baca situasi dan tahu cara ngomong yang bikin orang keikut.\nIde yang tadinya biasa aja, di tangan kamu jadi kedengeran menarik.\nKalau suasana mulai hambar, kamu refleks pengen bikin hidup lagi.\n✨Kamu bukan cuma jago ngomong, tapi bikin orang lain pengen dengerin juga.\n✨ Kamu bikin orang mau bergerak—tanpa merasa disuruh.")
        st.balloons()
        st.image("https://media4.giphy.com/media/Fpxqv7Tyg37a0e6ohl/giphy.gif")
    if result.startswith("SELAMAT! KAMU AUTO MIKIR RESIKO"):
        st.text("Kamu mikir untung-rugi di kepala sambil senyum.\nKelihatannya santai, padahal otak lagi buka kalkulator.\nKalau kamu bilang “tunggu dulu”, biasanya dompet selamat.\n✨ Kamu bukan yang paling gas, tapi paling bikin semuanya aman.")
        st.balloons()
        st.image("https://media3.giphy.com/media/WRQBXSCnEFJIuxktnw/giphy.gif")
    if result.startswith("SELAMAT! KAMU SERBA BISA"):
        st.text("Sedikit-sedikit kamu ambil peran.\nNgatur iya, nenangin iya, ngejual ide juga iya.\nCapek? Iya. Tapi kalau kamu nggak gerak, rasanya semua gak jalan.\n✨ Kamu keren banget sih! mau kamu satu dong.")
        st.balloons()
        st.image("https://media1.giphy.com/media/G8rcbSPfCgs3VDrWi5/giphy.gif")
    if st.button("Reset"):
        st.session_state.p_index = 0
        st.session_state.jawaban_user = [None] * len(QUESTIONS)
        st.session_state.submitted = False