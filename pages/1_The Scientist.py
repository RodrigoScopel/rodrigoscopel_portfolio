import streamlit as st
from streamlit import session_state as ss



st.set_page_config(page_title="The Scientist", layout="wide", initial_sidebar_state="expanded")
st.markdown("<h1 style='text-align: center; color: white;'>The Scientist</h1>", unsafe_allow_html=True)


st.divider()


c1,c2,c3,c4,c5 = st.columns(5)
with c3:
    st.image("Profile.png",width=200)
with st.expander("The Scientist", expanded=False):

    st.markdown(':white_small_square: Business-savvy innovation scientist with 16+ years in consumer-centric innovation strategy and new product development across multiple categories, focusing on :red[data-driven decision-making and product performance optimisation.]')
    st.markdown(':white_small_square: Passionate about :red[multi-disciplinary problem-solving], data science, materials science, product development, and consumer insights. Award-winning innovative solutions in sustainability and product performance.')
    st.markdown(':white_small_square: Proven track record in using data science for technology development and market share growth, demonstrated by multiple publications, conference presentations, and :red[establishing a business intelligence division] at a startup.')

with st.expander("Academic Background", expanded=False):

    st.markdown('Executive Education, Data Science and Business Analytics, Imperial College Business School, UK (2023)')
    st.markdown('Postdoctoral Fellow, Materials Engineering and Technology, PUCRS, Brazil (2017)')
    st.markdown("Ph.D., Materials Engineering and Technology, PUCRS, Brazil (2017)")
    st.markdown("Visiting Graduate Researcher, Bioengineering, UCLA, US (2015)")
    st.markdown("M.Sc., Materials Engineering and Technology, PUCRS, Brazil (2013)")
    st.markdown("B.S., Chemical Engineering (Academic Distinction), PUCRS, Brazil (2011)")
st.divider()



c1,c2 = st.columns([0.2,0.8])

with c1: 
      st.image("tuslogo1.png",width=100)

with c2:
    st.markdown("<h2 style='text-align: left; color: white;'>THE UNSEEN BEAUTY - London, UK (2021 to 2024)</h2>", unsafe_allow_html=True)
st.markdown("")





col1, col2= st.columns([1,2])



with col1:
    st.markdown("<h5 style='text-align: left; color: white;'>Data Sciece Projects</h5>", unsafe_allow_html=True)
    with st.expander("THE BRAIN", expanded=False):



        st.markdown("THE BRAIN - This was an iniative created to provide visibility on all company's KPIs. Attached is an example of the dashboard available to leadership.")
        st.link_button("Go to Project", "https://drive.google.com/file/d/1TV8KQfsDyZE76aKGogTUCXxEbpGuxC38/view?usp=drive_link")

    with st.expander("FORECASTING MODEL", expanded=False):
        st.markdown("FORECASTING MODEL - I have used several machine learning models to create a sales forecasting model. This was aimed at optmising business investments.")
        st.link_button("Go to Project", "https://drive.google.com/file/d/1Y5keDBvoYGjn4YOvn2LtO1kBajlZBsoY/view?usp=drive_link")



    with st.expander("CONSUMER INSIGHTS STUDIES", expanded=False):
        st.markdown("Brow products: This study was ran to acquire information on *size of the prize* for an eyebrow innovation.")
        st.link_button("Go to Project", "https://drive.google.com/file/d/167iOSxN8NsmvOhr2nmkHaf6Rka8lCVV4/view?usp=drive_link")
        
        st.markdown("Chrome Hair: This study was ran to acquire information on *size of the prize* for a new hair makeup product.")
        st.link_button("Go to Project", "https://drive.google.com/file/d/167iOSxN8NsmvOhr2nmkHaf6Rka8lCVV4/view?usp=drive_link")

    st.markdown("<h5 style='text-align: left; color: white;'>Formulation Projects</h5>", unsafe_allow_html=True)
    with st.expander("Eye Shadow Collection - Colour Alchemy Eyes", expanded=False):

 
        html_code = """
    <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/reel/CrOQqL4sKV6/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/reel/CrOQqL4sKV6/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#FFFFFF; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:100%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 100px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/reel/CrOQqL4sKV6/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by THE UNSEEN Beauty (@theunseenbeauty)</a></p></div></blockquote>
<script async src="//www.instagram.com/embed.js"></script>

"""
        st.components.v1.html(html_code,width=350,height=500) 

    with st.expander("Hair Make-up - Spectra Hair", expanded=False):
        html_code1 = """

    <blockquote class="instagram-media" data-instgrm-permalink="https://www.instagram.com/tv/CaabQJ8A1TB/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#000000; border:0; border-radius:3px; box-shadow:0 0 1px 0 rgba(0,0,0,0.5),0 1px 10px 0 rgba(0,0,0,0.15); margin: 1px; max-width:5px; min-width:16px; padding:0; width:10.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);"><div style="padding:16px;"> <a href="https://www.instagram.com/tv/CaabQJ8A1TB/?utm_source=ig_embed&amp;utm_campaign=loading" style=" background:#000000; line-height:0; padding:0 0; text-align:center; text-decoration:none; width:20%;" target="_blank"> <div style=" display: flex; flex-direction: row; align-items: center;"> <div style="background-color: #000000; border-radius: 50%; flex-grow: 0; height: 40px; margin-right: 14px; width: 40px;"></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center;"> <div style=" background-color: #000000; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 80px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 60px;"></div></div></div><div style="padding: 19% 0;"></div> <div style="display:block; height:50px; margin:0 auto 12px; width:50px;"><svg width="50px" height="50px" viewBox="0 0 60 60" version="1.1" xmlns="https://www.w3.org/2000/svg" xmlns:xlink="https://www.w3.org/1999/xlink"><g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"><g transform="translate(-511.000000, -20.000000)" fill="#000000"><g><path d="M556.869,30.41 C554.814,30.41 553.148,32.076 553.148,34.131 C553.148,36.186 554.814,37.852 556.869,37.852 C558.924,37.852 560.59,36.186 560.59,34.131 C560.59,32.076 558.924,30.41 556.869,30.41 M541,60.657 C535.114,60.657 530.342,55.887 530.342,50 C530.342,44.114 535.114,39.342 541,39.342 C546.887,39.342 551.658,44.114 551.658,50 C551.658,55.887 546.887,60.657 541,60.657 M541,33.886 C532.1,33.886 524.886,41.1 524.886,50 C524.886,58.899 532.1,66.113 541,66.113 C549.9,66.113 557.115,58.899 557.115,50 C557.115,41.1 549.9,33.886 541,33.886 M565.378,62.101 C565.244,65.022 564.756,66.606 564.346,67.663 C563.803,69.06 563.154,70.057 562.106,71.106 C561.058,72.155 560.06,72.803 558.662,73.347 C557.607,73.757 556.021,74.244 553.102,74.378 C549.944,74.521 548.997,74.552 541,74.552 C533.003,74.552 532.056,74.521 528.898,74.378 C525.979,74.244 524.393,73.757 523.338,73.347 C521.94,72.803 520.942,72.155 519.894,71.106 C518.846,70.057 518.197,69.06 517.654,67.663 C517.244,66.606 516.755,65.022 516.623,62.101 C516.479,58.943 516.448,57.996 516.448,50 C516.448,42.003 516.479,41.056 516.623,37.899 C516.755,34.978 517.244,33.391 517.654,32.338 C518.197,30.938 518.846,29.942 519.894,28.894 C520.942,27.846 521.94,27.196 523.338,26.654 C524.393,26.244 525.979,25.756 528.898,25.623 C532.057,25.479 533.004,25.448 541,25.448 C548.997,25.448 549.943,25.479 553.102,25.623 C556.021,25.756 557.607,26.244 558.662,26.654 C560.06,27.196 561.058,27.846 562.106,28.894 C563.154,29.942 563.803,30.938 564.346,32.338 C564.756,33.391 565.244,34.978 565.378,37.899 C565.522,41.056 565.552,42.003 565.552,50 C565.552,57.996 565.522,58.943 565.378,62.101 M570.82,37.631 C570.674,34.438 570.167,32.258 569.425,30.349 C568.659,28.377 567.633,26.702 565.965,25.035 C564.297,23.368 562.623,22.342 560.652,21.575 C558.743,20.834 556.562,20.326 553.369,20.18 C550.169,20.033 549.148,20 541,20 C532.853,20 531.831,20.033 528.631,20.18 C525.438,20.326 523.257,20.834 521.349,21.575 C519.376,22.342 517.703,23.368 516.035,25.035 C514.368,26.702 513.342,28.377 512.574,30.349 C511.834,32.258 511.326,34.438 511.181,37.631 C511.035,40.831 511,41.851 511,50 C511,58.147 511.035,59.17 511.181,62.369 C511.326,65.562 511.834,67.743 512.574,69.651 C513.342,71.625 514.368,73.296 516.035,74.965 C517.703,76.634 519.376,77.658 521.349,78.425 C523.257,79.167 525.438,79.673 528.631,79.82 C531.831,79.965 532.853,80.001 541,80.001 C549.148,80.001 550.169,79.965 553.369,79.82 C556.562,79.673 558.743,79.167 560.652,78.425 C562.623,77.658 564.297,76.634 565.965,74.965 C567.633,73.296 568.659,71.625 569.425,69.651 C570.167,67.743 570.674,65.562 570.82,62.369 C570.966,59.17 571,58.147 571,50 C571,41.851 570.966,40.831 570.82,37.631"></path></g></g></g></svg></div><div style="padding-top: 8px;"> <div style=" color:#3897f0; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:550; line-height:18px;">View this post on Instagram</div></div><div style="padding: 12.5% 0;"></div> <div style="display: flex; flex-direction: row; margin-bottom: 14px; align-items: center;"><div> <div style="background-color: #000000; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(0px) translateY(7px);"></div> <div style="background-color: #F4F4F4; height: 12.5px; transform: rotate(-45deg) translateX(3px) translateY(1px); width: 12.5px; flex-grow: 0; margin-right: 14px; margin-left: 2px;"></div> <div style="background-color: #F4F4F4; border-radius: 50%; height: 12.5px; width: 12.5px; transform: translateX(9px) translateY(-18px);"></div></div><div style="margin-left: 8px;"> <div style=" background-color: #F4F4F4; border-radius: 50%; flex-grow: 0; height: 20px; width: 20px;"></div> <div style=" width: 0; height: 0; border-top: 2px solid transparent; border-left: 6px solid #f4f4f4; border-bottom: 2px solid transparent; transform: translateX(16px) translateY(-4px) rotate(30deg)"></div></div><div style="margin-left: auto;"> <div style=" width: 0px; border-top: 8px solid #F4F4F4; border-right: 8px solid transparent; transform: translateY(16px);"></div> <div style=" background-color: #F4F4F4; flex-grow: 0; height: 12px; width: 16px; transform: translateY(-4px);"></div> <div style=" width: 0; height: 0; border-top: 8px solid #F4F4F4; border-left: 8px solid transparent; transform: translateY(-4px) translateX(8px);"></div></div></div> <div style="display: flex; flex-direction: column; flex-grow: 1; justify-content: center; margin-bottom: 24px;"> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; margin-bottom: 6px; width: 224px;"></div> <div style=" background-color: #F4F4F4; border-radius: 4px; flex-grow: 0; height: 14px; width: 144px;"></div></div></a><p style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; line-height:17px; margin-bottom:0; margin-top:8px; overflow:hidden; padding:8px 0 7px; text-align:center; text-overflow:ellipsis; white-space:nowrap;"><a href="https://www.instagram.com/tv/CaabQJ8A1TB/?utm_source=ig_embed&amp;utm_campaign=loading" style=" color:#c9c8cd; font-family:Arial,sans-serif; font-size:14px; font-style:normal; font-weight:normal; line-height:17px; text-decoration:none;" target="_blank">A post shared by THE UNSEEN Beauty (@theunseenbeauty)</a></p></div></blockquote> <script async src="//www.instagram.com/embed.js"></script>
    """ 
    
        st.components.v1.html(html_code1,width=400,height=500)  



with col2:

    st.markdown(':white_small_square: Created and led a data science division, developed nodes for data gathering via APIs, and performed multiple data-related activities such as analysis, modelling and business optimisation. Additionally, liaised with key stakeholders to define relevant KPIs and established a centralised dashboard for real-time data access.')
    st.markdown(':white_small_square: Conducted consumer insights studies to test innovation concepts, managed data analysis and reporting using Python, Supermetrics, and SQL tools, and effectively communicated findings to key stakeholders. This drove the development of the product portfolio and secured funding.')
    st.markdown(':white_small_square: Led strategic and hands-on R&D activities, synthesising and optimising materials with data-centric approaches to enhance performance. This was exemplified by developing and patenting an antibacterial home cleaning formulation with live bacteria indicators, funded by Innovate UK & Eurostars.')
    st.image("tus3.png",width=500)

st.divider()

c1,c2 = st.columns([0.8,0.2])

with c1: 
    st.markdown("<h2 style='text-align: left; color: white;'>PROCTER AND GAMBLE - New Castle Upon Tyne, UK (2020 to 2021)</h2>", unsafe_allow_html=True)
 
with c2:
    st.image("pglogo.png",width=150 )
    
col1, col2 = st.columns(2)

with col1:


    st.markdown(':white_small_square: Spearheaded a modelling and simulation program to optimise laundry product manufacturing processes, reducing trial numbers and changeover times through collaboration with statisticians, data analysts, the consumer insights division and R&D.')
    st.markdown(':white_small_square: Led the Front-End Innovation Team to develop new raw materials and concepts for the India region, contributing to P&Gs 2030 strategic plan.')
    st.markdown(":white_small_square: Collaborated with product development, research, engineering, and plant sites to deliver cost- saving and innovative solutions for Ariel and Tide brands, focusing on India's dry laundry plants.")




st.divider()

c1,c2 = st.columns([0.3,0.7])

with c1: 
      st.markdown("")
      st.image("lushlogo.png",width=200 )

with c2:
    st.markdown("<h2 style='text-align: right; color: white;'>LUSH FRESH HANDMADE COSMETICS - Poole, UK (2017 to 2020)</h2>", unsafe_allow_html=True)



col1, col2 = st.columns(2)



with col2:
    
    c1,c2,c3 = st.columns(3)


    st.markdown(":white_small_square: Defined KPIs, created mathematical models, and optimised natural ingredient extraction processes, enhancing global communities' revenue and expanding Lush's fragrance raw materials library.")
    st.markdown(":white_small_square: Managed the development of the first non-ionic surfactant, transitioning from palm-based surfactants to environmentally friendly alternatives, supporting Lush's regenerative supply chain.")
    st.markdown(":white_small_square: Collaborated with company founders and product designers on developing and scaling 100+ formulations for hair care, colour cosmetics, and hygiene products.")

st.divider()


with st.expander("The Life Time Passion", expanded=False):
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("")
        st.video("personal_1.mov", autoplay=True, loop=True)

    with col2:
            st.markdown("<h2 style='text-align: right; color: white;'>Music is my passion</h2>", unsafe_allow_html=True)

            st.markdown("I have been playing guitar as far as I can remember. Since I got my first guitar I never put it down. I have played in dozens of bands (the current one being a punk rock noise-maker called 'First Time Dead') and recorded multiple tracks. Now, I am building my very own home studio, to take my passion projects to the next level. ")
            st.markdown(":red[I have been using Spitfire Audio for a long time and absolutely love it.] It would be a privilege to contribute to enabling artists to express themselves via my favourite language: music.")




