import streamlit as st
import random

# --------------------------
# SESSION STATE
# --------------------------
if "index" not in st.session_state:
    st.session_state.index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "wrong" not in st.session_state:
    st.session_state.wrong = False
if "submitted_last" not in st.session_state:
    st.session_state.submitted_last = False
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = []
if "selected" not in st.session_state:
    st.session_state.selected = None

# --------------------------
# TRUE/FALSE QUESTIONS
# (NOW INCLUDING EXPLANATIONS)
# --------------------------
questions = [
    {
        "statement": "Merun kang isang sakong may nakasulat na mga titik na pweding ilarawan bilang <i>set</i> A={K,D,N,I}. Ang D ba ay isang <i>element</i> ng <i>set</i> A? (ang D ∈ A?)",
        "answer": True,
        "image": "https://imgur.com/ATzh7ZE.jpg",
        "image_width": 150,
        "explanation": "Kung ang <i>set</i> A ay naglalaman ng D, kung gayon ang D ay isang <i>element</i> ng <i>set</i> A. Dahil ang D ay nakalista sa <i>set</i> A, ang pahayag ay tama."
    },
    {
        "statement": "Hayaan ang <i>set</i> A={1,3,4,5}. Ang 3 ba ay isang <i>element</i> ng <i>set</i> A? Ibig sabihin, ang 3 ba ay kabilang sa A?",
        "answer": True,
        "image": None,
        "explanation": "Kung ang A ay naglalaman ng 3, kung gayon ang 3 ay isang <i>element</i> ng A. Dahil ang 3 ay nakalista sa A, ang pahayag ay tama."
    },
    {
        "statement": "Ang <i>null set</i> ay isang <i>set</i> na walang laman. Ang <i>null set</i> ay maaaring ilarawan ng ∅.",
        "answer": True,
        "image": None,
        "explanation": "Ang <i>null set</i> ay isang <i>set</i> na walang laman. Ang <i>null set</i> ay maaaring ilarawan ng ∅."
    },
    {
        "statement": "Hayaan ang <i>set</i> A={2,4,6,8,10,12}. Ang 3 ba ay isang <i>element</i> ng <i>set</i> A? (ang 7 ∈ A?)",
        "answer": False,
        "image": None,
        "explanation": "Kung ang A ay naglalaman ng 7, kung gayon ang 7 ay isang <i>element</i> ng A. Dahil ang 7 ay hindi nakalista sa A, ang pahayag ay mali."
    },
    {
        "statement": "Hayaan ang <i>set</i> A={2,3,5,7,11}. Ang 7 ba ay isang <i>element</i> ng <i>set</i> A? (ang 7 ∈ A?)",
        "answer": True,
        "image": None,
        "explanation": "Kung ang A ay naglalaman ng 7, kung gayon ang 7 ay isang <i>element</i> ng A. Dahil ang 7 ay nakalista sa A, ang pahayag ay tama."
    },
    {
        "statement": "Hayaan ang <i>set</i> A={3,4,5,7,10}. Ang 9 ba ay hindi isang <i>element</i> ng <i>set</i> A? (ang 9 ∉ A?)",
        "answer": True,
        "image": None,
        "explanation": "Kung ang A ay hindi naglalaman ng 9, kung gayon ang 9 ay hindi isang <i>element</i> ng A. Dahil ang 9 ay hindi nakalista sa A, ang pahayag ay tama."
    },
    {
        "statement": "Hayaan ang <i>set</i> A={D,X,I,Z}. Ang X ba ay hindi isang <i>element</i> ng <i>set</i> A? (ang X ∉ A?)",
        "answer": False,
        "image": None,
        "explanation": "Kung ang A ay hindi naglalaman ng X, kung gayon ang X ay hindi isang <i>element</i> ng A. Dahil ang X ay nakalista sa A, ang pahayag ay mali."
    },
    {
        "statement": "Si Maria ay naglista ng limang salitang Pilipino sa pisara na maaaring ilarawan bilang <i>set</i> B= {Bukas, Saging, Mangga, Aso, Ubas}. Ang 'Ubas' ba ay isang <i>element</i> ng <i>set</i> B? (ang Ubas ∈ B?)",
        "answer": True,
        "image": "https://imgur.com/M4BI5BA.jpg",
        "image_width": 280,
        "explanation": "Kung ang B ay naglalaman ng 'Ubas', kung gayon ang 'Ubas' ay isang <i>element</i> ng B. Dahil ang 'Ubas' ay nakalista sa B, ang pahayag ay tama."
    },
    
    {
        "statement": "Hayaan <i>sets</i> A={1,2,3} at B={1,2,3,4,5}. Ang <i>set</i> A ba ay isang <i>subset</i> ng B (A ⊆ B)?", 
        "answer": True,
        "image": None,
        "explanation": "Kung lahat ng mga <i>element</i> ng A ay nasa B din, kung gayon ang A ay isang <i>subset</i> ng B. Dahil ang 1, 2, at 3 ay lahat sa B, ang pahayag ay tama."
    },
    {
        "statement": "Hayaan <i>sets</i> A={11,13,14,19} at B={11,12,13,14,18,19,20}. Ang <i>set</i> A ba ay isang <i>subset</i> ng B (A ⊆ B)?", 
        "answer": True,
        "image": None,
        "explanation": "Kung lahat ng mga <i>element</i> ng A ay nasa B din, kung gayon ang A ay isang <i>subset</i> ng B. Dahil ang 11, 13, 14, at 19 ay lahat sa B, ang pahayag ay tama."
    },
    {
        "statement": "Hayaan <i>sets</i> A={1,2,5} at B={1,2,4,6,7}. Ang <i>set</i> A ba ay isang <i>subset</i> ng B (A ⊆ B)?", 
        "answer": False,
        "image": None,
        "explanation": "Dahil hindi lahat ng mga <i>element</i> ng A ay nasa B tulad ng 5 na wala sa B, ang A ay hindi isang <i>subset</i> ng B."
    },
    {
        "statement": "Dalawang sako ay naglalaman ng mga sumusunod na letra na maaaring ilarawan bilang mga <i>sets</i>: <i>Set</i> A={D,T} at <i>Set</i> B={C,D,R,T,X}. Ang <i>set</i> A ba ay isang <i>subset</i> ng B (A ⊆ B)? ",
        "answer": True,
        "image": "https://imgur.com/1ZJCo3y.jpg",
        "image_width": 150,
        "explanation": "Dahil ang Sako A ay naglalaman lamang ng D at T, at pareho ang D at T ay nasa Sako B, ang A ay isang <i>subset</i> ng B."
    },
    {
        "statement": "Si Anna at Bob ay may iba't ibang koleksyon ng mga panulat. Ang koleksyon ni Anna ay maaaring ilarawan bilang <i>set</i> A={Pula, Asul} habang ang koleksyon ni Bob ay <i>set</i> B={Dilaw, Asul, Itim, Lila}. Ang <i>set</i> A ba ay isang <i>subset</i> ng B (A ⊆ B)? ",
        "answer": False,
        "image": "https://imgur.com/hLMBcF7.jpg",
        "image_width": 320,
        "explanation": "Dahil si Anna ay may pulang panulat na wala si Bob, ang <i>set</i> A ay hindi isang <i>subset</i> ng <i>set</i> B."
    }
]

# --------------------------
# RANDOMIZE AND PICK ONLY 7
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]
    remaining = questions[2:]
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:5]

q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]

# --------------------------
# DISPLAY
# --------------------------
# Place logo to the left of the heading/introduction
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("TAMA o MALI: Panimula sa Teorya ng Mga *Sets*")
    st.write("Ang *set* ay isang koleksyon ng mga natatanging bagay, na tinatawag na mga *elements*. Ang *subset* ay isang *set* kung saan ang lahat ng *elements* ay nandoon din sa ibang *set*.")
    
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")
# Progress bar (full width)
st.progress((st.session_state.index + 1) / len(q_list))

if q["image"]:
    image_width = q.get("image_width", 300)  # Default to 300 if not specified
    st.image(q["image"], width=image_width)

st.markdown(
    f"<div style='font-size:22px; margin-bottom:15px'>{q['statement']}</div>",
    unsafe_allow_html=True
)

# --------------------------
# TRUE / FALSE BUTTONS
# --------------------------
col1, col2 = st.columns(2)
with col1:
    if st.button("TAMA", disabled=st.session_state.answered):
        st.session_state.selected = True
        st.session_state.answered = True

with col2:
    if st.button("MALI", disabled=st.session_state.answered):
        st.session_state.selected = False
        st.session_state.answered = True

# --------------------------
# CHECK ANSWER
# --------------------------
if st.session_state.answered:
    if st.session_state.selected == q["answer"]:
        st.success("Tama! 🎉")
        if not st.session_state.wrong:
            last = st.session_state.get("last_scored_index", None)
            if last != st.session_state.index:
                st.session_state.score += 1
                st.session_state.last_scored_index = st.session_state.index
                st.balloons()
        st.session_state.wrong = False

    else:
        st.error("Mali ❌")
        st.markdown(
            f"<div style='background:#fce8e6;padding:12px;border-radius:8px;'>"
            f"<b>Paano Solusyunan:</b><br>{q['explanation']}</div>",
            unsafe_allow_html=True
        )
        st.session_state.wrong = True

    # mark last question submitted (answered) — show final regardless of correctness
    if st.session_state.index == len(q_list) - 1 and st.session_state.answered:
        st.session_state.submitted_last = True

# --------------------------
# RETRY WRONG ANSWER
# --------------------------
if st.session_state.wrong:
    if st.button("🔄 Subukan Ulit"):
        st.session_state.answered = False
        st.session_state.wrong = False
        st.session_state.selected = None
        st.rerun()

# --------------------------
# NAVIGATION BUTTONS
# --------------------------
col1, col2 = st.columns(2)

with col1:
    if st.session_state.index > 0:
        if st.button("← Nakaraang"):
            st.session_state.index -= 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.rerun()

# --------------------------
# FINAL RESULTS
# --------------------------
if st.session_state.submitted_last:
    st.markdown("---")
    col_left, col_mid, col_right = st.columns([2, 2, 2])
    with col_left:
        st.markdown("### 🎉 Kumpleto ang Pagsusulit!")
        st.markdown(f"<span style='font-size:1.3em; font-weight:bold;'>Panghuling Marka: {st.session_state.score} / {len(q_list)}</span>", unsafe_allow_html=True)
    with col_mid:
        if st.button("Suriin Muli ang Pagsusulit"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.submitted_last = False
            st.session_state.selected = None
            st.session_state.shuffled_questions = []
            if "last_scored_index" in st.session_state:
                del st.session_state["last_scored_index"]
            st.rerun()
    with col_right:
        st.markdown("<a href='/Pages/1_Set Theory-Rewriting Sets' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)

    st.stop()

# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Marka: **{st.session_state.score} / {len(q_list)}**")
