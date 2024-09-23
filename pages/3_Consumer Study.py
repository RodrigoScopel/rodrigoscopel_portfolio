import streamlit as st

st.set_page_config(page_title="Consumer Study", layout="wide", initial_sidebar_state="expanded")

st.markdown("<h1 style='text-align: center; color: white;'>Spitfire Audio</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Consumer Study</h3>", unsafe_allow_html=True)

st.divider()

st.title("Interview - AI in the music industry")

st.markdown("I have interviewed a selection of artists, music producers, software engineers and marketing professionals to get their perspectives on AI and Software Instruments. This page highlights their takes and key ideas of where there is space for improvement and innovation.")

st.divider()

c1,c2,c3 = st.columns(3)


with c1: 
    st.image("Tiago.png")
    st.markdown("*Tiago Flores - Maestro and Composer at ULBRA Orchestra*")
   
with c2: 
    st.markdown("<h3 style='text-align: left; color: white;'>Profile</h3>", unsafe_allow_html=True)
    st.markdown("Tiago is a Maestro, Arranger and Composer at ULBRA Orchestra. Tiago conducted his studies at St. Petesburgh Conservatory. Previously, Tiago has led other 9 symphony orchestras in Brazil")
    st.markdown("After several years of using technology to assist him with compositions and arrangements, he was forced to stop due to severe tendinitis.")
    st.markdown("Tiago has also mentioned that he struggles to find the time to use and keep himself updated on the new technologies coming out in the market.")
    
with c3:
    st.markdown("<h3 style='text-align: left; color: white;'>Opportunities</h3>", unsafe_allow_html=True)
    st.markdown("When asked about his perception of using AI to assist with work, Tiago said that he is completely open to it, especially when the main objective is to create quick mockups to send to the orchestra's musicians.")
    st.markdown(":red[Key Takeaway: Using AI to help with accessibility and streamlining scoring can be a great opportunity for Spitfire Audio.]")

st.divider()

c1,c2,c3 = st.columns(3)
with c1: 
 st.image("Ayres.png")
 st.markdown("*Ayres Pottof (Flutist) - Founder of Theatro São Pedro Orchaestra*")

with c2: 
    st.markdown("<h3 style='text-align: left; color: white;'>Profile</h3>", unsafe_allow_html=True)
    st.markdown("Ayres is a distinguished flutist and educator who has studied with renowned instructors in the U.S. and Brazil, earning a Master's degree in Flute. He is the founder of the Brazilian Association of Flutists and the iconic Theatro Sao Pedro Orchestra.")

with c3:
    st.markdown("<h3 style='text-align: left; color: white;'>Opportunities</h3>", unsafe_allow_html=True)
    st.markdown("Ayres mentioned relevant topics about the current state of audio recording technology now versus when he started in the music industry. In his opinion, musicians used to rely more on their listening skills, whereas today, the visual element is more prominent.")
    st.markdown("He also mentioned that when working on commercial projects for advertising, a lot of time is lost on choosing the right sound for the arrangement.")
    st.markdown(":red[Key Takeaway: Spitfire Audio could use AI algorithms to leverage the visual element of current recording software, to help artists in their recording workflow.]")
    st.markdown(":red[There is a big opportunity for a 'recommendation system' that helps artists make the most of the Spitfire Audio libraries, aiding in finding the best-suited one for each project.]")

st.divider()

c1,c2,c3 = st.columns(3)
with c1: 
    st.image("Matheus.png")
    st.markdown("*Matheus Gugelmim - Owner at Vox Haus (Music and Sound Production Company)*")

with c2: 
    
    st.markdown("<h3 style='text-align: left; color: white;'>Profile</h3>", unsafe_allow_html=True)
    st.markdown("Matheus Gugelmim is an awarded professional, boasting 15 Cannes Lions, and over 35 Dubai Lynx - including multiple Grand Prix for agencies. In 2023, Vox Haus ranked among the top 20 audio production companies in the world in the One Club for Creativity and among the top 10 in Latin America. Recently he has been invited to speak about the use of AI in Audio Production at CCSP.")

with c3: 
    
    st.markdown("<h3 style='text-align: left; color: white;'>Opportunities</h3>", unsafe_allow_html=True)
    st.markdown("Matheus uses Spitfire Audio on a daily basis, he is a superfan and believes no other company gets close when it comes to quality of sound.")
    st.markdown("He believes there is a lack of focus on technologies to help produce more natural dynamics.")
    st.markdown(":red[Key takeaway: There is a significant opportunity to improve articulation algorithms, which would lead to an increase in software accessibility and realistic outputs.]")


st.divider()

c1,c2,c3 = st.columns(3)
with c1: 
    st.image("Thiago.png")
    st.markdown("*Thiago Gauterio (Music producer and Sound Designer at Fita.nu*")
with c2: 

    st.markdown("<h3 style='text-align: left; color: white;'>Profile</h3>", unsafe_allow_html=True)
    st.markdown("Thiago has been working in the music industry for 18 years with a focus on building narratives for films and creating motion graphics and apps. He has worked on projects with Google, Nike, Audi, Freeletics, Huawei, MTV, Toyota, amongst others")
with c3: 

    st.markdown("<h3 style='text-align: left; color: white;'>Opportunities</h3>", unsafe_allow_html=True)
    st.markdown("Thiago is a fan of Spitfire Audio and has been using the Labs products since it's launch. When comparing Spitfire to its competitors, he said 'Spitfire is for grown-ups' - alluding to the power of the brand.")
    st.markdown(":red[Key takeaway: Leveraging Spitfire's brand relevance and working with indie and smaller producers can be an excellent way to build Spitfire Labs+ user community.]")

st.divider()

c1,c2,c3 = st.columns(3)
with c1: 
    st.image("Pedro.png")
    st.markdown("*Pedro Ramos (Creative Producer & Beatmaker)*")
with c2: 

    st.markdown("<h3 style='text-align: left; color: white;'>Profile</h3>", unsafe_allow_html=True)
    st.markdown("Pedro is a Brazilian beatmaker and turntablist based in Portugal with 20+ years of experience. He has studied at Run-DMC's Jam Master Jay 'Scratch DJ Academy' in New York. Recently, Pedro has been producing beats for AiMi.")
    st.markdown("Pedro also doubles as a creative producer and has worked in productions across 10+ countries, with clients in the Netherlands, Germany, Brazil, and the US.")

with c3: 

    st.markdown("<h3 style='text-align: left; color: white;'>Opportunities</h3>", unsafe_allow_html=True)
    st.markdown("Pedro quoted Spitfire Audio as a reference in branding for music software. He has also exemplified 'Teenage Engineering' as his main reference for hardware.")
    st.markdown(":red[Key Takeaway: Optmising content creation is a great opportunity for Spitfire Audio. Companies such as Arturia, Ableton and Native Instruments have great examples of engaging with indie producers - particularly Ableton with their '1-Thing' series on YouTube.]")


st.divider()




