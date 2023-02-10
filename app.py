import streamlit as st
from PIL import Image, ImageDraw, ImageFont

the_font = ImageFont.truetype('data/swiss.ttf',22)
the_colour = '#ffe500'
the_banner = 'data/nzdf.png'
banner_name = None
image = Image.open(the_banner)

st.set_page_config(
    page_title="TT Totara Banner Creator",
    layout='wide',
    initial_sidebar_state='expanded'
)

def create_banner(service,course_code,course_name):

    if service == 'Defence':
        the_colour = '#ffe500'
        the_banner = 'data/nzdf.png'

    if service == 'Navy':
        the_colour = '#0099d8'
        the_banner = 'data/navy.png'

    if service == 'Army':
        the_colour = '#c62026'
        the_banner = 'data/army.png'

    if service == 'Air':
        the_colour = '#28b6ea'
        the_banner = 'data/air.png'

    ban = Image.open(the_banner)
    img = ImageDraw.Draw(ban)
    img.text((205,130),course_code,font=the_font, fill=(the_colour))
    img.text((205,160),course_name,font=the_font, fill=(255,255,255))
    banner_name = course_code + '.png'
    ban.save(banner_name)

    return ban, banner_name

st.title('TT Totara Banner Creator')
st.sidebar.header('Banner Creation Form:')
st.sidebar.caption('Complete the form below and click create banner')


with st.sidebar.form("create_banner"):
    st.radio("Select Service",
        options=("Navy","Army","Air","Defence"),
        key='service',
        horizontal=True)

    st.text_input('Course Code','Course Code', key="code")
    st.text_input('Course Name','Course Name', key='name')


   # Every form must have a submit button.
    submitted = st.form_submit_button("Create Banner")
    if submitted:
        create_banner(st.session_state.service,st.session_state.code,st.session_state.name)
        image = Image.open(st.session_state.code + '.png')

        
        
st.image(image,caption=st.session_state.code + ': ' + st.session_state.name)

db = st.download_button(label='Download Image',
        data= open(st.session_state.code + '.png', 'rb').read(),
        file_name=st.session_state.code + '.png',
        mime='image/png')



