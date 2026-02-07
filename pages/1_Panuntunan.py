import streamlit as st  
import streamlit as st



col1, col2 = st.columns([1, 4])

with col1:
    st.image("https://imgur.com/wuASFCz.jpg", width=150)

with col2:
    st.markdown("<div style='display: flex; align-items: center; height: 100%;'><div><h1 style='margin: 0; padding-left: 20px; line-height: 1;'>More Rational PH</h1><h3 style='margin: -10px 0 0 20px; padding: 0; line-height: 1;'>Para sa Pag-unlad</h3></div></div>", unsafe_allow_html=True)

st.write("---")
sidebar_css = """
<style>
[data-testid="stSidebar"] {
    background: #7c4700 !important;
}
[data-testid="stSidebar"] .css-1v3fvcr,
[data-testid="stSidebar"] [data-testid="stSidebarNav"] {
    color: #fff !important;
}
[data-testid="stSidebar"] [data-testid="stSidebarNav"] span {
    color: #fff !important;
}
</style>
"""
st.markdown(sidebar_css, unsafe_allow_html=True)
st.markdown("<h2 style='font-size:27px'>Panuto at Kung ano ang Kailangang Gawin para Mahasa ang iyong Pag-iisip:</h2>", unsafe_allow_html=True)

st.markdown("<p style='font-size:19px'>Ang unang talata ay magbibigay-diin kung bakit pinili ng <b>More Rational PH</b> ang wikang pambansa para maisagawa ang web na ito. Naisagawa ang web na ito hindi lang para matuto tayong mag-rason at mahasa ang ating isip gamit ang ating sariling wika, bagkus tayong mga mag-aaral na Pilipino ay mapamahal sa ating sariling wika at kultura. Dito matututunan natin na kaya pala nating mag-rason gamit ang ating wikang pambansa.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>May piling mga sangay sa matematika at lohika na lubos na makakatulong sa ating pag-iisip. Ang pag-aaral ng <i>set theory</i>, <i>sequence</i>, <i>probabilities</i>, at marami pang iba ay malaking tulong para tumalas ang ating isipan. Pag-aralan natin ito at mamangha sa progresong maaaring maibigay kung tayo ay may rasyonal at kritikal na pag-iisip.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Sa kahalagahan ng pagkakaroon ng magandang pag-aaral, ang mga nilalaman ng web na ito ay pampuno sa kasalukuyang edukasyon. Para hindi mawalang-bahala ang natatag na matematikong konsepto, ginawang <i>itilize</i> ang mga konseptong matematika gaya ng <i>elements</i>, <i>set</i>, at <i>prime numbers</i> sa <i>number theory</i>. </p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Inihanda ang mga pagsusulit na kahit ang mga mag-aaral sa nakababatang baitang ay maaaring subukan upang malinang ang kanilang magandang pag-iisip.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Tapusin ang kursong ito at siguradong hindi lang ikaw ay mapapamahal sa ating kultura, tatalas din ang iyong pag-iisip!</p>", unsafe_allow_html=True)

st.markdown('''
<div style="width:100%; display:flex; align-items:center; justify-content:space-between;">
    <a href="/Home" style="display:inline-flex;align-items:center;text-decoration:none;margin-top:24px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="background:#fff;border-radius:8px;box-shadow:0 0 8px 2px #42a5f5, 0 1px 4px rgba(0,0,0,0.1);margin-right:10px;"><path d="M3 12L12 3l9 9"/><path d="M9 21V9h6v12"/></svg>
        <span style="font-size:19px;color:#222;font-weight:bold;vertical-align:middle;">Home</span>
    </a>
    <a href="/Pages/1_Set Theory-Panimula" style="display:inline-block;margin-top:24px;padding:16px 32px;background:#222;border-radius:12px;color:white;font-size:19px;text-decoration:none;box-shadow:0 0 16px 4px #42a5f5, 0 2px 8px rgba(0,0,0,0.2);font-weight:bold;">Simulan ang Pag-aaral &#8594;</a>
</div>
''', unsafe_allow_html=True)