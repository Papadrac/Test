import streamlit as st
import base64
from pathlib import Path



# --- Set new background image from Imgur with light overlay ---
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url('https://imgur.com/FIdMR75.jpg');
    background-size: cover;
    background-position: center;
    position: relative;
}}
[data-testid="stAppViewContainer"]::before {{
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.8); /* 80% white overlay */
    z-index: 0;
    pointer-events: none;
}}
[data-testid="stHeader"] {{
    background-color: #FFFFFF;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_page_config(
    page_title="More Rational PH",
    initial_sidebar_state="expanded",
    layout="wide"
)

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #FFFFFF;
}
[data-testid="stHeader"] {
    background-color: #FFFFFF;
}
/* Sidebar dark purple and page name white */
[data-testid="stSidebar"] {
    background: #3a185c !important;
}
[data-testid="stSidebar"] .css-1v3fvcr, /* fallback for older Streamlit */
[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    color: #fff !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] span {
    color: #fff !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


col1, col2 = st.columns([1, 6])

with col1:
    st.image("https://imgur.com/wuASFCz.jpg", width=200)


with col2:
    st.markdown("<div style='display: flex; align-items: center; height: 100%;'><div><h1 style='margin: 0; padding-left: 20px; line-height: 1; font-size: 2.7em;'>More Rational PH</h1><h3 style='margin: -10px 0 0 20px; padding: 0; line-height: 1; font-size: 1.7em;'>Para sa Pag-unlad</h3></div></div>", unsafe_allow_html=True)
st.write("---")

st.subheader("Ano ang More Rational PH?")
st.markdown("<p style='font-size:24px; text-align:justify;'>Kumusta! Maligayang pagdating sa More Rational PH. Ang unang talata ay magbibigay-diin kung bakit pinili ng <b>More Rational PH</b> ang wikang pambansa para maisagawa ang web na ito. Naisagawa ang web na ito hindi lang para matuto tayong mag-rason at mahasa ang ating isip gamit ang ating sariling wika, bagkus tayong mga mag-aaral na Pilipino ay mapamahal sa ating sariling wika at kultura. Dito matututunan natin na kaya pala nating mag-rason gamit ang ating wikang pambansa.</p>", unsafe_allow_html=True)

    # Show images/meet1.JPG to the right of the first two paragraphs
with st.container():
        col_left, col_right = st.columns([5, 3])
        with col_left:
            st.markdown("<p style='font-size:24px; text-align:justify;'>Para lumawak ang pag-iisip, gumagawa ang grupo ng mga regular na pagtitipon. Dito nagkakaroon ng pagbabahagi ng mga ideya sa bawat miyembro, mapasang-ayon man o labag sa kani-kanilang paniniwala.</p>", unsafe_allow_html=True)

            st.markdown("<p style='font-size:24px; text-align:justify;'>Ang napag-uusapan ay mula sa pilosopiya, agham, matematika, o ano mang konseptong puwedeng magpalawak ng ating isipan. </p>", unsafe_allow_html=True)
            
        with col_right:
            st.image("images/meet3.JPG", width=700)

st.markdown("<p style='font-size:24px; text-align:justify;'>Para mapalaganap ang misyon ng grupong makatulong sa bansang Pilipinas gamit ang pagpapahalaga sa rasyonal at kritikal na pag-iisip, layunin namin na tulungan ang ating mga Pilipinong mag-aaral kagaya mo na tumalas pa ang iyong pag-iisip. Ito ay kailangan natin hindi lang para sa ating sariling pag-unlad pati na rin sa ikabubuti ng ating bansa. Lubos na kailangan ng bansa ngayon ang mga makabago at talentadong mag-aaral, at sana ikaw na ang susunod na mapahusay ang kakayahan gamit ang inihandang pag-aaral at pagsusulit.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:24px; text-align:justify;'>Sa platapormang ito, nag-aalok kami ng mga interaktibong pahina na dinisenyo upang palawakin ang iyong kaalaman at kasanayan sa iba't ibang aspeto ng matematika at lohika, mula sa mga pangunahing konsepto hanggang sa mga mas komplikadong teorya.</p>", unsafe_allow_html=True)

st.markdown("<p style='font-size:24px; text-align:justify;'>Para sa pag-unlad, simulan natin sa ating pag-iisip! Pagbutihin ang iyong pag-iisip gamit ang mga sumusunod na pahina.</p>", unsafe_allow_html=True)

st.markdown('''
<div style="width:100%; display:flex; align-items:center; justify-content:space-between;">
    <a href="/Home" style="display:inline-flex;align-items:center;text-decoration:none;margin-top:24px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="background:#fff;border-radius:8px;box-shadow:0 0 8px 2px #42a5f5, 0 1px 4px rgba(0,0,0,0.1);margin-right:10px;"><path d="M3 12L12 3l9 9"/><path d="M9 21V9h6v12"/></svg>
        <span style="font-size:22px;color:#222;font-weight:600;vertical-align:middle;">Home</span>
    </a>
    <a href="./Pages/1_Panuntunan.py" style="display:inline-block;margin-top:24px;padding:16px 32px;background:#222;border-radius:12px;color:white;font-size:19px;text-decoration:none;box-shadow:0 0 16px 4px #42a5f5, 0 2px 8px rgba(0,0,0,0.2);font-weight:bold;">Tingnan ang Panuntunan &#8594;</a>
</div>
''', unsafe_allow_html=True)
