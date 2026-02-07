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
        "question": "Si Rayan at James ay pwedi lang pumili sa anim na kulay na pweding irepresentang <i>universal set</i> U={Dilaw, Pula, Berde, Asul, Itim, Lila}. Kay Rayan at James ay pweding ilarawang bilang <i>sets</i> A at B. Hanapin ang (A ∪ B)'. Ibig sabihin, ilista ang mga kulay na hindi napili ni Rayan at James.",
        "choices": ['Dilaw', 'Pula', 'Berde', 'Lila', 'Itim', 'Asul'],
        "answer": {'Berde', 'Lila'},
        "image": "https://imgur.com/G8CslXR.jpg",
        "image_width": 350,
        "hint": "Hanapin muna ang (A ∪ B). Ang *union* ay ang mga kulay na makikita sa kahit na isa sa dalawang set. Pagkatapos, hanapin ang mga kulay na hindi nasa (A ∪ B)."
    },
    {
        "question": "Hayaan ang <i>universal set</i> U = {1,2,3,4,5,6,7,8,9}, A = {2,3,6,7}, at B = {3,7,8,9}. Hanapin ang (A ∩ B)'.",
        "choices": [1,2,3,4,5,6,7,8,9],
        "answer": {1,2,4,5,6,8,9},
        "image": None,
        "hint": "Una, hanapin ang A ∩ B (mga numero sa parehong A at B). Tingnan ulit ang *universal set*, tangalin dito ang mga numero na nasa A ∩ B, yon na ang iyong sagot sa (A ∩ B)'."
    },
    {
        "question": "Si Rayan at James ay pwedi lang pumili sa anim na kulay na pweding irepresentang bilang <i>universal set</i> U={Dilaw, Pula, Berde, Asul, Itim, Lila}. Ang napiling kulay ni Rayan at James ay pweding ilarawan bilang <i>sets</i> A and B. Hanapin ang B'∩A.",
        "choices": ['Dilaw', 'Pula', 'Berde', 'Lila', 'Itim', 'Asul'],
        "answer": {'Itim'},
        "image": "https://imgur.com/G8CslXR.jpg",
        "image_width": 350,
        "hint": "Hanapin muna ang B', ito yong mga kulay na hindi napili ni James. Tapos hanapin ang mga parehong kulay sa B' at A, yon na ang iyong magiging sagot sa B'∩A"
    },
    {
        "question": "Hayaan ang <i>universal set</i> U={a,e,k,t,u,y}, A={a,t,e}, at B={k,u,y,a}. Hanapin ang (A-B)'",
        "choices": ['a', 'e', 'k', 't','u','y'],
        "answer": {'a', 'k', 'u', 'y'},
        "image": None,
        "hint": "Tingnan ang mga salita na isinulat sa lahat ng tatlong pisara. Ang *intersection* ay ang mga salita na makikita sa lahat ng pisara."
    },
    {
        "question": "Hayaan ang <i>universal set</i> U={2,3,5,7,11,15}, A={2,3,7,15}, at B={3,5,7,15}. Hanapin ang A'∪B",
        "choices": ['2', '3', '5', '7','11','15'],
        "answer": {'3', '5', '7', '11','15'},
        "image": None,
        "hint": "Hanapin muna ang A', ito yong mga numerong nasa *universal set* U peru wala sa A. Tapos pagsamasamahin ang mga numero sa A' at B ito ang iyong magiging sagot sa A'∪B"
    },
    {
        "question": "Hayaan ang <i>universal set</i> U={a,e,k,t,u,y}, A={a,t,e}, at B={k,u,y,a}. Hanapin ang A'∪B'",
        "choices": ['a', 'e', 'k', 't','u','y',],
        "answer": { 'k', 'u','y','e','t'},
        "image": None,
        "hint": "Hanapin muna ang A' at B'. Ang *complement* ay ang mga titik na nasa *universal set* pero hindi nasa *set* na tinutukoy. Pagkatapos, hanapin pagsamasamahin ang mga titik na makikita sa A' at B'."
    },

]


# --------------------------
# RANDOMIZE AT PUMILI LAMANG 6
# --------------------------
if not st.session_state.shuffled_questions:
    first_four = questions[:2]  # keep first four questions fixed
    remaining = questions[2:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_four + remaining[:2]  # first four + 2 random from rest


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
    st.subheader("Teorya ng Mga *Sets*: Mga Hamon na Tanong2")
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
        st.markdown("<a href='#' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Wakas ng Seksyon</button></a>", unsafe_allow_html=True)
    st.stop()


# --------------------------
# BUHAY NA PUNTOS
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
# No further section to link to, so nothing is added here.
