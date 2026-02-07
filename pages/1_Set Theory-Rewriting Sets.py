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
if "retry_counts" not in st.session_state:
    st.session_state.retry_counts = {}
if "show_explanation" not in st.session_state:
    st.session_state.show_explanation = {}
# maximum retries allowed per question
MAX_RETRIES = 1

# --------------------------
# TRUE/FALSE QUESTIONS
# (NOW INCLUDING EXPLANATIONS)
# --------------------------
questions = [
    {
        "question": "Hayaan ang <i>set</i> A={lahat ng <i>integers</i> mula 2 hanggang 5}. Aling <i>set</i> ang kumakatawan sa <i>set</i> A?",
        "choices": ["{0,1,2,3}", "{1,2,3,4,5}", "{2,3,4,5}", "{0}"],
        "answer": "{2,3,4,5}",
        "explanation": "Ang mga <i>integers</i> ay mga bung numero gaya ng 2 at 3. Ilista ang mga buong numero mula 2 hanggang 5"
    },
    {
        "question": "Hayaan ang <i>set</i> A={lahat ng positibong <i>odd numbers</i> na mas mababa sa 10}. Aling <i>set</i> ang kumakatawan sa <i>set</i> A?",
        "choices": ["{1,2,3,4,5,6,7,8,9}", "{1,3,5,7,9}", "∅", "{0}"],
        "answer": "{1,3,5,7,9}",
        "explanation": "Ang mga <i>odd numbers</i> ay mga numero na hindi maaaring hatiin ng dalawa tulad ng numero 3"
    },
    {
        "question": "Hayaan ang <i>set</i> A={lahat ng positibong <i>even numbers</i> na higit sa 10 ngunit mas mababa sa o katumbas ng 21}. Aling <i>set</i> ang kumakatawan sa <i>set</i>A?",
        "choices": ["{1,2,3,4,5,6,7,8,9}", "{10,12,14,16,18,20}", "{12,14,16,18,20}", "{0}"],
        "answer": "{12,14,16,18,20}",
        "explanation": "Ang mga <i>even numbers</i> ay mga numero na maaaring hatiin ng dalawa tulad ng numero 12"
    },
    {
        "question": "Hayaan ang <i>set</i> B={Lahat ng positibong <i>multiple</i> ng 5 na mas mababa sa 25}. Aling <i>set</i> ang kumakatawan sa <i>set</i> B?",
        "choices": ["{5,10,15,20,25}", "{1,5,25}", "{1,25}", "{5,10,15,20}"],
        "answer": "{5,10,15,20}",
        "explanation": "Ang mga <i>multiple</i> ng 5 ay mga numero na maaaring hatiin ng 5 tulad ng numero 20. Ang numero 25 ay hindi kasama dahil hindi ito mas mababa sa 25."
    },
    {
         "question": "Hayaan ang <i>set</i> B={Lahat ng positibong <i>multiple</i> ng 6 na mas mababa sa o katumbas ng 30}. Aling <i>set</i> ang kumakatawan sa <i>set</i> B?",
        "choices": ["{6,12,18,24,30}", "{1,6,30}", "{1,30}", "{6,12,18,24}"],
        "answer": "{6,12,18,24,30}",
        "explanation": "Ang mga <i>multiple</i> ng 6 ay mga numero na maaaring hatiin ng 6 tulad ng numero 12."
    },
    {
         "question": "Hayaan ang <i>set</i> M={Lahat ng <i>factor</i> ng 10}. Aling <i>set</i> ang kumakatawan sa <i>set</i> M?",
        "choices": ["{2,5,10}", "{1,2,5}", "{1,2,5,10}", "{2,5}"],
        "answer": "{1,2,5,10}",
        "explanation": "Ang mga <i>factor</i> ng 10 ay mga numero na maaaring humati ng 10. Halimbawa ang numero 2 ay dapat na nasa <i>set</i> dahil maaari nitong hatiin ang 10 sa limang grupo."
    },
    {
         "question": "Hayaan ang <i>set</i> M={Lahat ng <i>factor</i> ng 30}. Aling <i>set</i> ang kumakatawan sa <i>set</i> M?",
        "choices": ["{2,5,10}", "{1,2,3,5,6,10,15,30}", "{5,6}", "{2,5}"],
        "answer": "{1,2,3,5,6,10,15,30}",
        "explanation": "Ang mga <i>factor</i> ng 30 ay mga numero na maaaring humati ng 30. Halimbawa ang numero 3 ay dapat na nasa <i>set</i> dahil maaari nitong hatiin ang 30 sa sampung grupo."
    },
    {
         "question": "Hayaan ang <i>set</i> P={Lahat ng <i>prime numbers</i> sa pagitan ng 20 at 30}. Aling <i>set</i> ang kumakatawan sa <i>set</i> P?",
        "choices": ["{21,23,25,29}", "{21,23,25,27,29}", "{23,29}", "∅"],
        "answer": "{23,29}",
        "explanation": "Ang mga <i>prime numbers</i> ay mga numero na may dalawang <i>factors</i> lamang: 1 at ang kanilang sarili. Halimbawa ang 23 ay prime dahil ang tanging <i>factors</i> nito ay 1 at 23. Habang ang 25 ay hindi prime dahil mayroon itong tatlong <i>factors</i>: 1, 5, at 25."
    },
    {
         "question": "Hayaan ang <i>set</i> P={Lahat ng <i>prime numbers</i> na mas mababa sa 10}. Aling <i>set</i> ang kumakatawan sa <i>set</i> P?",
        "choices": ["{2,3,5,7,9}", "{2,3,5,7}", "{2,3,5,7,11}", "{7}"],
        "answer": "{2,3,5,7}",
        "explanation": "Ang mga <i>prime numbers</i> ay mga numero na may dalawang <i>factors</i> lamang: 1 at ang kanilang sarili. Halimbawa ang 7 ay prime dahil ang tanging <i>factors</i> nito ay 1 at 7. Habang ang 9 ay hindi prime dahil mayroon itong tatlong <i>factors</i>: 1, 3, at 9."
    },
    {
         "question": "Hayaan ang <i>set</i> I={Lahat ng <i>integers</i> sa pagitan ng -5 at 5}. Aling <i>set</i> ang kumakatawan sa <i>set</i> I?",
        "choices": ["{-5,-4,-3,-2,-1,0,1,2,3,4}", "{0,1,2,3,4}", "{-4,-3,-2,-1,0}", "{-4,-3,-2,-1,0,1,2,3,4}"],
        "answer": "{-4,-3,-2,-1,0,1,2,3,4}",
        "explanation": "Ang mga <i>integers</i> ay mga buong numero na maaaring maging positibo o negatibo. Ang mga numero -5 at 5 ay hindi kasama sa <i>set</i> I dahil ang <i>set</i> I ay naglalaman lamang ng mga numero sa pagitan ng -5 at 5."
    },
    {
         "question": "Hayaan ang <i>set</i> A={Lahat ng <i>integers</i> sa pagitan ng -3 at 4}. Aling <i>set</i> ang kumakatawan sa <i>set</i> A?",
        "choices": ["{-2,-1,0,1,2,3,4}", "{-2,-1,0,1,2,3}", "{-3,-2,-1,0,1,2,3,4}", "{-4,-3,-2,-1,0,1,2,3,4}"],
        "answer": "{-3,-2,-1,0,1,2,3}",
        "explanation": "Ang mga <i>integers</i> ay mga buong numero na maaaring maging positibo o negatibo. Ang mga numero -3 at 4 ay hindi kasama sa <i>set</i> A dahil ang <i>set</i> A ay naglalaman lamang ng mga numero sa pagitan ng -3 at 4."
    },
    {
         "question": "Hayaan ang <i>set</i> I={Lahat ng <i>integers</i> sa pagitan ng -2 at 7 kasama ang -2 at 7}. Aling <i>set</i> ang kumakatawan sa <i>set</i> I?",
        "choices": ["{1,2,3,4,5,6}", "{0,1,2,3,4}", "{-2,-1,0}", "{-2,-1,0,1,2,3,4,5,6,7}"],
        "answer": "{-2,-1,0,1,2,3,4,5,6,7}",
        "explanation": "Ang mga <i>integers</i> ay mga buong numero na maaaring maging positibo o negatibo."
    },
    {
         "question": "Hayaan ang <i>set</i> C={<i>Multiple</i> ng 12 sa pagitan ng 13 at 20}. Aling <i>set</i> ang kumakatawan sa <i>set</i> C?",
        "choices": ["∅", "{12}", "{12,24}", "{0,12}"],
        "answer": "∅",
        "explanation": "Ang mga <i>multiple</i> ng 12 ay mga numerong pweding hatiin sa 12 gaya ng 12, 24, 36, atbp. Dahil walang <i>multiple</i> ng 12 sa pagitan ng 13 at 20, ang <i>set</i> C ay walang laman."
    },
    {
         "question": "Hayaan ang <i>set</i> F={lahat ng <i>factor</i> ng 35 sa pagitan ng 20 at 30}. Aling <i>set</i> ang kumakatawan sa <i>set</i> F?",
        "choices": ["{5,7}", "{20,30}", "∅", "{0}"],
        "answer": "∅",
        "explanation": "Ang mga <i>factor</i> ng 35 ay mga numero na maaaring humati sa 35 gaya ng 1, 5, 7, at 35. Ang mga <i>factor</i> ng 35 ay {1,5,7,35}. Walang mga <i>factors</i> na ito ay nasa pagitan ng 20 at 30, kaya ang <i>set</i> F ay walang laman."
    },
]

# --------------------------
# RANDOMIZE AND PICK ONLY 5
# --------------------------
if not st.session_state.shuffled_questions:
    first_two = questions[:2]  # keep first two questions fixed
    remaining = questions[2:]  # randomize from the rest
    random.shuffle(remaining)
    st.session_state.shuffled_questions = first_two + remaining[:3]  # first two + 3 random from rest

q_list = st.session_state.shuffled_questions
q = q_list[st.session_state.index]


# --------------------------
# DISPLAY (logo + instructions)
# --------------------------
col_logo, col_header = st.columns([1, 5])
with col_logo:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)
    

with col_header:
    st.subheader("Teorya ng Mga *Sets*: Ilista ang mga *elements* na tinutukoy sa bawat *set*")
    st.write("Ilista ang lahat ng mga *elements* na inilarawan sa bawat *set*.")
    
    

st.write("--------")
st.subheader(f"Tanong {st.session_state.index + 1} ng {len(q_list)}")
# Progress bar (full width)
st.progress((st.session_state.index + 1) / len(q_list))


# --------------------------
# MULTIPLE-CHOICE (per-question options)
# --------------------------
# get options for this question and show them

st.markdown(
    f"<div style='font-size:20px; margin-bottom:10px'>{q['question']}</div>",
    unsafe_allow_html=True
)
# If explanation was unlocked for this question (from a previous wrong/ retry), show it here
if st.session_state.show_explanation.get(st.session_state.index, False):
    st.markdown(
        f"<div style='background:#fce8e6;padding:12px;border-radius:8px;'>"
        f"<b>How to Solve:</b><br>{q.get('explanation','')}</div>",
        unsafe_allow_html=True
    )
# --------------------------
# MULTIPLE CHOICE OPTIONS
# --------------------------
choice = st.radio("Select your answer:", q["choices"], index=0)

if choice:
    st.session_state.selected = choice

# Submit button: record the selected choice and mark answered
if st.button("Ipadala"):
        if st.session_state.get("selected"):
            st.session_state.selected_text = st.session_state.selected
            try:
                st.session_state.selected_index = q["choices"].index(st.session_state.selected_text)
            except Exception:
                st.session_state.selected_index = None
            st.session_state.answered = True
        else:
            st.warning("Pumili ng isang opsyon bago ipadala.")

# --------------------------
# CHECK ANSWER
# --------------------------
if st.session_state.answered:
    # determine correctness by comparing submitted text to the question's answer
    selected_text = st.session_state.get("selected_text", None)
    correct_answer = q.get("answer", None)

    is_correct = (selected_text is not None and correct_answer is not None and str(selected_text) == str(correct_answer))

    if is_correct:
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
        # always unlock and show the explanation for this question
        st.session_state.show_explanation[st.session_state.index] = True
        st.markdown(
            f"<div style='background:#fce8e6;padding:12px;border-radius:8px;'>"
            f"<b>Paano Solusyunan:</b><br>{q.get('explanation','')}</div>",
            unsafe_allow_html=True
        )
        retry_count = st.session_state.retry_counts.get(st.session_state.index, 0)
        if retry_count >= MAX_RETRIES:
            if correct_answer is not None:
                st.info(f"Tamang sagot: **{correct_answer}**")
        else:
            st.info(f"Mali — mayroon kang {MAX_RETRIES - retry_count} subukan pa ulit.")
        st.session_state.wrong = True

    # markahan ang huling tanong na isinumite lamang kapag tama ang huling tanong o walang na-retry na natitira
    if st.session_state.index == len(q_list) - 1 and st.session_state.answered:
        last_retry = st.session_state.retry_counts.get(st.session_state.index, 0)
        if is_correct or last_retry >= MAX_RETRIES:
            st.session_state.submitted_last = True
        else:
            st.session_state.submitted_last = False

# --------------------------
# SUBUKAN ULIT ANG MALING SAGOT
# --------------------------
if st.session_state.wrong:
    # payagan ang hanggang MAX_RETRIES na subukan ulit bawat tanong
    retry_count = st.session_state.retry_counts.get(st.session_state.index, 0)
    if retry_count < MAX_RETRIES:
        if st.button("🔄 Subukan Ulit"):
            # dagdagan ang retry counter para sa tanong na ito
            st.session_state.retry_counts[st.session_state.index] = retry_count + 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.session_state.selected_text = None
            st.session_state.selected_label = None
            if "selected_index" in st.session_state:
                del st.session_state["selected_index"]
            st.rerun()
        st.write(f"Natitirang subukan: {MAX_RETRIES - retry_count}")
    else:
        st.write("Walang natitirang subukan para sa tanong na ito.")

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
            st.session_state.submitted_last = False
            st.rerun()

with col2:
    if st.session_state.index < len(q_list) - 1:
        if st.button("Susunod →"):
            st.session_state.index += 1
            st.session_state.answered = False
            st.session_state.wrong = False
            st.session_state.selected = None
            st.session_state.submitted_last = False
            st.rerun()

# --------------------------
# HULING RESULTA
# --------------------------
# Ipakita ang huling resulta lamang kapag isinumite na ng user ang huling tanong
if st.session_state.submitted_last and st.session_state.index == len(q_list) - 1 and st.session_state.answered:
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
        st.markdown("<a href='/Pages/2_Set Theory-Intersection.py' target='_self'><button style='font-size:16px;padding:8px 16px;border-radius:6px;background:#0099f6;color:white;border:none;cursor:pointer;'>Pumunta sa Susunod na Seksyon →</button></a>", unsafe_allow_html=True)

    st.stop()

# --------------------------
# BUHAY NA PUNTOS
# --------------------------
st.markdown(f"##### Puntos: **{st.session_state.score} / {len(q_list)}**")
