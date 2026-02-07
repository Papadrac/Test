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


# --------------------------
# QUIZ DATA (ORIGINAL LIST)
# --------------------------
questions = [
    {"question": "May dalawang garapon na may lamang mga marbles. Anong kulay ng marbles na makikita mo sa parihong garapon?",
        "choices": ["Berde", "Asul", "Pula", "Dilaw"],
        "answer": {"Pula"},
        "image": "https://imgur.com/sH7Sdd6.jpg",
        "image_width": 310
        
    },
    {
        "question": "Hanapin ang <i>intersection</i> sa pagitan ng A={1,2,3,4} at B={3,4,6,7,9}?",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {3,4},
        "image": None
    },
    {
        "question": "Dalawang sako A and B na merun mga titik na nakasulat na pweding ilarawan bilang <i>sets</i>. Anong mga titik ang merun sa dalawang <i>sets</i>?",
        "choices": ["N", "B", "T", "E", "O", "R", "N"],
        "answer": {"T", "O", "N"},
        "image": "https://imgur.com/lmQYmws.jpg",
        "image_width": 310
    },
    {
        "question": "Mayroon kang dalawang garapon ng mga marbles. Hanapin ang lahat ng kulay ng mga marbles na nasa parehong garapon.",
        "choices": ["Berde", "Dilaw", "Kulay-abo",  "Asul","Lila", "Pula"],
        "answer": {"Berde", "Asul", "Pula"},
        "image": "https://imgur.com/ENVpapC.jpg",
        "image_width": 320
    },
    {
        "question": "Mayroon kang dalawang garapon ng mga marbles. Hanapin ang lahat ng kulay ng mga marbles na nasa parehong garapon.",
        "choices": ["Orange","Berde", "Dilaw", "Kulay-abo",  "Asul","Lila", "Pula"],
        "answer": {"Orange", "Asul"},
        "image": "https://imgur.com/QSwePbT.jpg",
        "image_width": 330
    },
    
    {
        "question": "Hanapin ang <i>intersection</i> sa pagitan ng A={3,5,6,9,12,17} at B={19,17,7,8,3,20,6}?",
        "choices": [3,5,6,7,8,9,12,17,19,20],
        "answer": {3,6,17},
        "image": None
    },
    {
        "question": "Si Maria ay may limang hayop na pweding ilarawan bilang isang <i>set</i>: {Manok, Kalabaw, Leon, Tarzier, Aso}. Si John naman ay may: {Tarzier, Aso, Pato, Agila, Pusa}. Aling hayop ang pareho silang mayroon?",
        "choices": ["Manok", "Kalabaw", "Leon", "Tarzier", "Aso", "Pato", "Agila", "Pusa"],
        "answer": {"Tarzier", "Aso"},
        "image": "https://imgur.com/WmM5fwT.jpg",
        "image_width": 350
    },
    {
        "question": "Dalawang sako A and B na merun mga titik na nakasulat na pweding ilarawan bilang <i>sets</i>. Anong mga titik ang parehong merun sa dalawang <i>sets</i>?",
        "choices": ["K", "U", "Y", "A", "B", "N"],
        "answer": {"U"},
        "image": "https://imgur.com/aRr08CH.jpg",
        "image_width": 300
    },
    {
        "question": "Ang <i>set</i> M at N ay naglalaman ng mga titik: M={A,B,D,F,I} at N={D,G,I,X}. Hanapin ang <i>intersection</i> ng M at N.",
        "choices": ["A", "B", "D", "F", "I", "G", "X"],
        "answer": {"D", "I"},
        "image": None
    },
    {
        "question": "Ang mga <i>sets</i> A at B ay naglalaman ng mga titik: A={B,U,N,S,O,T,A,Y} at B={K,U,Y,A,T,E}. Hanapin ang <i>intersection</i> ng A at B.",
        "choices": ["A", "B", "N", "F", "I", "G", "U", "Y", "T", "E"],
        "answer": {"A", "U", "Y", "T"},
        "image": None
    },
    {
        "question": "Kung ang <i>set</i> M={Lahat ng <i>even positive integers</i> na hindi lalagpas ng 20} at ang <i>set</i> N={Lahat ng <i>positive multiples of 3</i> na hindi lalagpas ng 20}, hanapin ang <i>intersection</i> ng M at N.",
        "choices": ["2", "3", "6", "5", "12", "10", "15", "18", "20"],
        "answer": {"6", "12", "18"},
        "image": None
    },
    {
        "question": "Kung ang <i>set</i> A={Lahat ng <i>factors</i> ng 10} at ang <i>set</i> B={Lahat ng <i>factors</i> ng 15}, hanapin ang <i>intersection</i> ng A at B.",
        "choices": ["1", "2", "3", "5", "10", "15", "15"],
        "answer": {"1", "5"},
        "image": None
    }
]


# --------------------------
# RANDOMIZE AND PICK ONLY 5
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[2:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:3]  # first two + 3 random from rest


# --------------------------
# USE THE SHUFFLED QUESTION LIST
# --------------------------
q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]


# --------------------------
# DISPLAY QUESTION (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col_header:
    st.subheader("Teorya ng Mga Sets: *Intersection* (A ∩ B)")
    st.write("Ang *intersection* ng mga *sets* A at B (tinatukoy bilang A ∩ B) ay naglalaman ng lahat ng mga elemento na parehong nasa *sets*.")
    
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")

# Progress bar for this page's quiz (full width)
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
# SUBMIT
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
        st.write("Paliwanag: Ang *intersection* ay naglalaman lamang ng mga elemento na parehong nasa *sets*.")
        st.session_state.answered = True
        st.session_state.wrong = True

    # final-question completion handled below after retry logic


# --------------------------
# RETRY WRONG ANSWER
# --------------------------

if "retry_counts" not in st.session_state:
    st.session_state.retry_counts = {}

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


# If this is the last question, mark the quiz complete when it's been submitted and is correct, or when retries exhausted
if st.session_state.index == len(q_list) - 1:
    last_retry = st.session_state.retry_counts.get(st.session_state.index, 0)
    if st.session_state.answered and (not st.session_state.wrong or last_retry >= MAX_RETRIES):
        st.session_state.submitted_last = True
    else:
        st.session_state.submitted_last = False


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
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.rerun()


# --------------------------
# SHOW RESULTS WHEN FINISHED
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
        st.markdown("<a href='/Pages/2_Set Theory-Union.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# LIVE SCORE
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
