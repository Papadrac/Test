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
       "question": "May dalawang garapon na may lamang mga marbles. Anong kulay ng marbles ang makikita mo sa unang garapon na wala sa pangalawang garapon?",
        "choices": ["Berde", "Asul", "Pula", "Dilaw"],
        "answer": {"Berde","Asul"},
        "image": "https://imgur.com/QlPfqvd.jpg",
        "image_width": 310
    },
    {
        "question": "Hayaan ang <i>set</i> A = {1,3,5,6,7,8,9} at B = {2,3,6,7,8}, hanapin ang A - B (mga elemento sa A ngunit hindi sa B)?",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {1,5,9},
        "image": None
    },
    {
        "question": "Mayroon kang dalawang garapon na may lamang marbles. Hanapin ang lahat ng mga kulay ng marbles sa garapon A ngunit hindi sa garapon B.",
        "choices": ["Luntian", "Dilaw",  "Asul","Lila", "Pula","Orange"],
        "answer": { "Dilaw",  "Lila"},
        "image": "https://imgur.com/ENVpapC.jpg",
        "image_width": 310
    },
    
    
    {
        "question": "Hayaan ang <i>set</i> A = {5,8,9,12,13,17,20} at B = {2,3,6,7,8,12,17,19}, hanapin ang A - B (mga elemento sa A ngunit hindi sa B)?",
        "choices": [5,8,9,12,13,17,20],
        "answer": {5,9,13,20},
        "image": None
    },
    {
        "question": "Si Anna at Bob ay parehong may koleksyon ng mga panulat. Ilista ang lahat ng kulay ng mga panulat na mayroon Anna ngunit wala si Bob.",
        "choices": ["Pula", "Asul", "Berde",  "Itim","Dilaw","Lilang-lila"],
        "answer": {"Pula",  "Berde"},
        "image": "https://imgur.com/jeVN1qN.jpg",
        "image_width": 350
    },
    {
        "question": "Ang <i>set</i> A at B ay naglalaman ng mga titik na tinukoy tulad ng sumusunod: A={D,I,X,M} at B={I,X,E,Y}. Ano ang mga titik na nasa <i>set</i> A ngunit hindi sa B.",
        "choices": ["A", "B","M", "D","E", "F", "I"],
        "answer": {"M", "D"},
        "image": None
    },
    {
        "question": "Ang <i>set</i> X at Y ay naglalaman ng mga titik na tinukoy tulad ng sumusunod: X={L,O,L,A} at Y={A,P,O}. Ano ang mga titik na nasa <i>set</i> X ngunit hindi sa Y.",
        "choices": ["A", "P","O", "L"],
        "answer": {"L"},
        "image": None
    },
    {
        "question": "Dalawang sako A at B ay naglalaman ng mga titik na ipinapakita sa itaas. Hanapin ang lahat ng mga titik sa sako A ngunit hindi sa sako B.",
        "choices": ["A","B","C","E","T","Z","R"],
        "answer": { "A",  "E","Z" },
        "image": "https://imgur.com/T81OlbN.jpg",
        "image_width": 320
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
    st.subheader("Teorya ng Mga *Sets*: *Set difference* (A−B)")
    st.write("Ang *set difference* A − B o A\B ay naglalaman ng lahat ng mga elemento sa *set* A na hindi sa *set* B.")
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
        st.write("Paliwanag: Ang *difference* ng dalwang *sets* ay naglalaman ng mga elemento sa unang *set* na hindi sa pangalawang *set*.")
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
        st.markdown("<a href='/Pages/5_Set Theory-Hamon na Tanong1.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# BUHAY NA PUNTOS
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
