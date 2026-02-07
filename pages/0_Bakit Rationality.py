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
    background: #14532d !important;
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
st.markdown("<h2 style='font-size:27px'>Ang Malaking Tulong ng Pagkakaroon ng Rasyonal at Kritikal na Pag-iisip:</h2>", unsafe_allow_html=True)

st.markdown("<p style='font-size:19px'>Hindi ko intensyon na sabihin ito sa negatibong paraan, pero isang mahalagang obserbasyon na kung ikukumpara mo ang Pilipinas sa ibang progresibong bansa, ang mga Pilipinong mag-aaral ay halos huli sa academic performance.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ano ang gagawin? Sa kalagayan ng bansang Pilipinas ngayon, kailangan nating magkaroon ng makabago at talentadong mga Pilipinong mag-aaral. Ito ay masisimulan natin sa ating pag-iisip. Ang pagkakaroon ng rasyonal at kritikal na pag-iisip ay malaking impluwensiya sa halos lahat ng aspeto kung paano tayo mamuhay.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ang pagkakaroon ng negatibong pilosopiya ay maaaring magdulot ng malaking pinsala hindi lamang sa iyong sarili pati na rin sa iyong mga minamahal sa buhay o maging sa buong bansang Pilipinas.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Ang rasyonalidad ay parang isang tagalinis ng isipan upang maalis at mapalitan ang mga idolohiyang nakakasama.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Para sa pag-unlad, inaanyayahan ko kayong magkaroon o hasain pa ang inyong magandang pag-iisip. Ang More Rational PH ay naghahandog ng mga pahinang maaaring pag-aralan upang makatulong sa iyong pag-iisip.</p>", unsafe_allow_html=True)
st.markdown("<p style='font-size:19px'>Para sa iyong pag-unlad!!!</p>", unsafe_allow_html=True)

st.markdown('''
<div style="width:100%; display:flex; align-items:center; justify-content:space-between;">
    <a href="/Home" style="display:inline-flex;align-items:center;text-decoration:none;margin-top:24px;">
        <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="#222" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="background:#fff;border-radius:8px;box-shadow:0 0 8px 2px #42a5f5, 0 1px 4px rgba(0,0,0,0.1);margin-right:10px;"><path d="M3 12L12 3l9 9"/><path d="M9 21V9h6v12"/></svg>
        <span style="font-size:19px;color:#222;font-weight:bold;vertical-align:middle;">Home</span>
    </a>
    <a href="./Pages/1_Panuntunan.py" style="display:inline-block;margin-top:24px;padding:16px 32px;background:#222;border-radius:12px;color:white;font-size:19px;text-decoration:none;box-shadow:0 0 16px 4px #42a5f5, 0 2px 8px rgba(0,0,0,0.2);font-weight:bold;">Simulan ang Pag-aaral &#8594;</a>
</div>
''', unsafe_allow_html=True)