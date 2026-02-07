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
if "retry_counts" not in st.session_state:
    st.session_state.retry_counts = {}


# --------------------------
# QUIZ DATA (ORIGINAL LIST)
# --------------------------
questions = [
    {
        "question": "Si Anna, Kevin, at Juan ay may sinulat na mga salita sa puting pisara. Hanapin ang salita na makikita sa tatlong pisara. Ito ay katumbas sa <i>intersection</i> ng tatlong <i>sets</i> A ∩ B ∩ C.",
        "choices": ['Mama', 'Apo', 'Ate', 'Kuya'],
        "answer": {'Apo'},
        "image": "https://imgur.com/aDotyIV.jpg",
        "image_width": 800,
        "hint": "Tingnan ang mga salita na isinulat sa lahat ng tatlong pisara. Ang *intersection* ay ang mga salita na makikita sa lahat ng pisara."
    },
    
    {
        "question": "Balikan ang imahe sa nakaraang tanong. Pag pinagsama mo ang mga salita na sinulat ni Anna at Kevin, peru tinatanggal ang mga salita na sinulat ni Juan, ano ang magiging resulta? Ito ay katumbas sa (A ∪ B) - C. ",
        "choices": ['Mama', 'Apo', 'Ate', 'Kuya','Papa'],
        "answer": {'Kuya',"Mama"},
        "image": "https://imgur.com/aDotyIV.jpg",
        "image_width": 800,
        "hint": "Una, pagsama-samahin ang lahat ng salita mula sa Anna at Kevin (A ∪ B). Pagkatapos, alisin ang mga salita na sinulat ni Juan."
    },
    {
        "question": "Merun kang tatlong garapon A,B, at C, pag pinagsama mo ang mga marbles sa A at B peru tinangal mo ang mga marbles na may kulay na makikita sa C, anong mga kulay ang matitira? Ito ay katumbas sa (A ∪ B) - C. ",
        "choices": ['Pula', 'Berde', 'Asul', 'Dilaw'],
        "answer": {'Pula',"Asul"},
        "image": "https://imgur.com/eYvjTcs.jpg",
        "image_width": 600,
        "hint": "Una, pagsama-samahin ang lahat ng marbles mula sa A at B (A ∪ B). Pagkatapos, alisin ang mga marbles na nasa C."
    },
    {
        "question": "Balikan ulit ang imahe sa nakaraang tanong. Pag kihuma mo ang salitang parehong sinulat ni Anna at Juan at pagkatapos sinama ang mga salita na sinulat ni Kevin, ano ang magiging resulta? Ito ay katumbas sa (A ∩ C) ∪ B. ",
        "choices": ['Mama', 'Apo', 'Ate', 'Kuya','Papa',"Tito","Lolo"],
        "answer": {"Apo","Kuya","Ate","Mama"},
        "image": "https://imgur.com/aDotyIV.jpg",
        "image_width": 800,
        "hint": "Una, hanapin ang mga salita na pareho kay Anna at Juan (A ∩ C). Pagkatapos, pagsama-samahin ito sa lahat ng salitang sinulat ni Kevin."
    },
    
    {
        "question": "Merun kang tatlong garapon A,B, at C. Pag kinuha mo ang kulay na pareho mong makikita sa B at C, pagkatapos pagsama-samahin ito sa lahat ng kulay na nasa A, anong mga kulay ang makikita mo? Ito ay katumbas sa (B ∩ C) ∪ A. ",
        "choices": ['Pula',"Lila","Kayumanggi",'Berde', 'Asul', 'Dilaw'],
        "answer": {'Berde','Pula',"Asul","Dilaw"},
        "image": "https://imgur.com/eYvjTcs.jpg",
        "image_width": 600,
        "hint": "Una, hanapin ang mga kulay na pareho sa B at C (B ∩ C). Pagkatapos, pagsama-samahin ito sa lahat ng kulay na nasa A."
    },
    {
        "question": "Hayaan ang A = {1,2,3,4,5}, B = {2,3,6,7}, at C = {3,7,8,9}. Hanapin ang A ∩ B ∩ C (ang mga elemento sa lahat ng tatlong <i>sets</i>).",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {3},
        "image": None,
        "hint": "Hanapin ang numero na parehas sa A, B, at C. Simulan sa intersection ng A at B, pagkatapos tingnan kung nasa C din."
    },
    {
        "question": "Hayaan ang A = {1,2,3,4,5}, B = {2,3,6,7}, at C = {3,7,8,9}. Hanapin ang (A ∩ B) ∪ C.",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {2,3,7,8,9},
        "image": None,
        "hint": "Una, hanapin ang A ∩ B (mga numero sa parehong A at B). Pagkatapos, pagsama-samahin ito sa lahat ng elemento ng C."
    },
    {
        "question": "Merung tatlong sakong may nakasulat na mga titik. Hanapin ang (A - B) ∪ (B - C). ",
        "choices": ['a', 'b', 'c', 'd','e',"f","g"],
        "answer": {'a','b','d'},
        "image": "https://imgur.com/hG0k2dg.jpg",
        "image_width": 600,
        "hint": "Una, hanapin ang mga titik na nasa A pero hindi sa B (A - B). Pagkatapos, hanapin ang mga titik na nasa B pero hindi sa C (B - C). Pagsama-samahin ang dalawang resulta."
    },
    {
        "question": "Hayaan ang A = {m,n,r,s}, B = {o,t,r,s}, at C = {t,m,r}. Hanapin ang (A∩B) ∪ (B∩C).",
        "choices": ['m','n','o','t','r','s'],
        "answer": {'r','s','t'},
        "image": None,
        "hint": "Kalkulahin ang A ∩ B at B ∩ C nang hiwalay, pagkatapos pagsama-samahin ang mga resulta."
    }
]


# --------------------------
# RANDOMIZE AT PUMILI LAMANG 6
# --------------------------
if not st.session_state.shuffled_questions:
    first_four = questions[:3]  # keep first four questions fixed
    remaining = questions[3:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_four + remaining[:3]  # first four + 2 random from rest


# --------------------------
# GAMITIN ANG SHUFFLED QUESTION LIST
# --------------------------
q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]


# --------------------------
# IPAKITA ANG TANONG (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Teorya ng Mga *Sets*: Mga Hamon na Tanong1")
    st.write("Mga kombinadong operasyon sa *set* na sumusubok sa iyong pag-unawa sa *union*, *intersection*, *complement*, at *difference*.")
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")

# Progress bar para sa quiz ng pahinang ito (full width)
progress_value = (st.session_state.index + 1) / len(q_list)
st.progress(progress_value)

if q["image"]:
    image_width = q.get("image_width", 400)  # Default to 400 if not specified
    st.image(q["image"], width=image_width)
st.markdown(
    f"<div style='font-size:19px; margin-bottom:10px'>{q['question']}</div>",
    unsafe_allow_html=True
)


selected = st.multiselect(
    "Piliin ang lahat ng tamang sagot:",
    q["choices"],
    key=f"q{st.session_state.index}"
)


# --------------------------
# IPADALA
# --------------------------
if st.button("Ipadala"):
    def _format_as_set(a):
        if isinstance(a, (set, list, tuple)):
            items = list(a)
            if all(isinstance(x, (int, float)) for x in items):
                items = sorted(items)
            else:
                items = sorted(items, key=lambda x: str(x))
            return "{" + ", ".join(map(str, items)) + "}"
        return str(a)
    
    st.write(f"Iyong sagot: **{_format_as_set(selected)}**")
    
    if set(selected) == q["answer"]:
        st.success("Tama! 🎉")
        if not st.session_state.wrong and not st.session_state.answered:
            st.session_state.score += 1
            st.balloons()
        st.session_state.answered = True
        st.session_state.wrong = False
    else:
        st.error("Mali ❌, subukan muli.")
        hint = q.get("hint", "Sundin nang mabuti ang mga operasyon ng <i>set</i> sa pagkakasunod-sunod.")
        st.write(f"Paliwanag: {hint}")
        st.session_state.answered = True
        st.session_state.wrong = True

    # final-question completion handled below after retry logic


# --------------------------
# RETRY WRONG ANSWER
# --------------------------

MAX_RETRIES = 2

if st.session_state.wrong:
    retry_count = st.session_state.retry_counts.get(st.session_state.index, 0)
    if retry_count < MAX_RETRIES:
        if st.button("🔄 Subukan Ulit"):
            st.session_state.retry_counts[st.session_state.index] = retry_count + 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()
        st.write(f"Natitirang subukan ulit: {MAX_RETRIES - retry_count}")
    else:
        st.write("Walang natitirang subukan para sa tanong na ito.")
        ans = q.get("answer")
        def _format_as_set(a):
            if isinstance(a, (set, list, tuple)):
                items = list(a)
                if all(isinstance(x, (int, float)) for x in items):
                    items = sorted(items)
                else:
                    items = sorted(items, key=lambda x: str(x))
                return "{" + ", ".join(map(str, items)) + "}"
            return str(a)

        st.info(f"Tamang sagot: **{_format_as_set(ans)}**")


# --------------------------
# MGA BUTTON NG NABIGATION
# --------------------------
col1, col2 = st.columns(2)

with col1:
    if st.session_state.index > 0:
        if st.button("← Nakaraang"):
            st.session_state.index -= 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()


# If this is the last question, mark the quiz complete when it's been submitted and is correct, or when retries exhausted
if st.session_state.index == len(q_list) - 1:
    last_retry = st.session_state.retry_counts.get(st.session_state.index, 0)
    if st.session_state.answered and (not st.session_state.wrong or last_retry >= MAX_RETRIES):
        st.session_state.submitted_last = True
    else:
        st.session_state.submitted_last = False


# --------------------------
# IPAKITA ANG RESULTA KAPAG TAPOS
# --------------------------
if st.session_state.submitted_last:
    st.markdown("---")
    st.markdown("### 🎉 Kumpleto ang Pagsusulit!")
    row = st.columns([2, 1, 1])
    with row[0]:
        st.markdown(f"<span style='font-size:1.3em; font-weight:bold;'>Huling Puntos: {st.session_state.score} / {len(q_list)}</span>", unsafe_allow_html=True)
    with row[1]:
        if st.button("Suriin Muli"):
            st.session_state.index = 0
            st.session_state.score = 0
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.submitted_last = False
            st.session_state.selected = None
            st.session_state.selected_text = None
            st.session_state.show_explanation = {}
            st.session_state.shuffled_questions = []
            if "last_scored_index" in st.session_state:
                del st.session_state["last_scored_index"]
            if "selected_index" in st.session_state:
                del st.session_state["selected_index"]
            st.rerun()
    with row[2]:
        st.markdown("<a href='/Pages/6_Set Theory-Hamon na Tanong2.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# BUHAY NA PUNTOS
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
