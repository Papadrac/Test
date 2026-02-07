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
        "question": "Lahat ng titik na makikita mo sa sako A ay makikita mo rin sa sako U. Pwedi nating tawagin ang sako U bilang isang <i>universal set</i>. Anong mga titik ang makikita mo sa <i>universal set </i>U na wala sa <i>set</i> A",
        "choices": ["N", "T",  "B","E", "O"],
        "answer": { "N",  "B","O"},
        "image": "https://imgur.com/3qbX3Hk.jpg"
    },
    {
        "question": "Kung ang universal <i>set</i> U = {1,2,5,6,7} at A = {2,6}, hanapin ang A'? Ibigsabihin ilista ang mga numero na nasa U ngunit wala sa A.",
        "choices": [1,2,5,6,7],
        "answer": {1,5,7},
        "image": None
    },
    {
        "question": "Mayroon kang dalawang garapon ng mga marbles. Ang Garapon B ay may mas kaunting iba't ibang kulay kaysa sa Garapon A. Hanapin ang lahat ng kulay na makikita mo sa garapon A ngunit hindi sa garapon B.",
        "choices": ["Berde", "Dilaw",  "Asul","Lila", "Pula","Kahel"],
        "answer": { "Dilaw",  "Pula"},
        "image": "https://imgur.com/bVjIlCp.jpg"
    },
    
    {
        "question": "Kung ang universal <i>set</i> ay U = {1,2,3,4,5,6,7,8,9} at A = {2,3,4,6,7}, hanapin ang A'? Ibigsabihin ilista ang mga numero na nasa U ngunit wala sa A.",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {1,5,8,9},
        "image": None
    },
    {
        "question": "Kung ang universal <i>set</i> ay U = {Lahat ng positibong buong numero na mas mababa sa 16}, hanapin ang <i>complement</i> ng A = {Lahat ng <i>multiple</i> ng 3 na mas mababa sa 16}?",
        "choices": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ],
        "answer": {1,2,4,5,7,8,10,11,13,14},
        "image": None
    },
    {
        "question": "Si Bob ay may mas kaunting panulat kaysa kay Anna. Hanapin ang lahat ng kulay ng panulat na mayroon Anna ngunit wala si Bob.",
        "choices": ["Pula", "Asul", "Berde",  "Itim"],
        "answer": {"Pula",  "Berde"},
        "image": "https://imgur.com/TtE44jy.jpg"
    },
    {
        "question": "Ang <i>universal set</i> U at N ay naglalaman ng mga titik na tinukoy tulad ng sumusunod: U={A,B,D,I,X} at N={A,I,X}. Hanapin ang N'. Ibig sabihin ilista ang mga titik na nasa U ngunit wala sa N.",
        "choices": ["A", "B","C", "D","E", "F", "I", "G", "X"],
        "answer": {"B", "D"},
        "image": None
    },
    {
        "question": "Ang <i>universal set</i> U at M ay naglalaman ng mga titik na tinukoy tulad ng sumusunod: U={A,T,E} at M={A,E}. Ano ang mga titik na nasa <i>set</i> U ngunit hindi sa M.",
        "choices": ["A", "T","E"],
        "answer": {"T"},
        "image": None
    },
    {
        "question": "Si Maria at John ay nakatira sa isang sakahan. Si John ay may mas kaunting hayop kaysa sa Maria at ang lahat ng hayop sa sakahan ni John ay nasa sakahan ni Maria din. Hanapin ang lahat ng hayop na mayroon Maria ngunit wala si John.",
        "choices": ["Manok", "Kalabao",  "Tarzier", "Aso", "Pato", "Agila", "Pusa"],
        "answer": { "Kalabao",  "Pato" },
        "image": "https://imgur.com/cjrK6TH.jpg"
    }
]


# --------------------------
# RANDOMIZE AND PICK ONLY 4
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[3:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:3]  # first two + 2 random from rest


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
    st.subheader("Teorya ng Mga *Set*: *Complement of a set* (A')")
    st.write("Ang *complement* ng *set* A (tinatukoy bilang A') ay naglalaman ng lahat ng mga elemento sa *universal set* na wala sa *set* A.")
st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")

# Progress bar for this page's quiz (full width)
progress_value = (st.session_state.index + 1) / len(q_list)
st.progress(progress_value)

if q["image"]:
    st.image(q["image"], width=400)

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
        st.write("Pahiwatig: Ang *complement* ay naglalaman ng mga elemento sa *universal set* na hindi makikita sa pangalawang *set*.")
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
        st.markdown("<a href='/Pages/4_Set Theory-Set Difference.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# BUHAY NA PUNTOS
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
