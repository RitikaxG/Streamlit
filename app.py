import streamlit as st
st.title('Title-> Hey Mates, Welcome Onboard!')  # Title
st.header('Header-> Hey Mates')                  # Header
st.subheader('Subheader-> Hey Mates')            # Subheader
st.text('Text-> Hey Mates')                      # Text


st.markdown('Yoo')                               # Markdown
st.markdown('# Yoo')
st.markdown('## Yoo')
st.markdown('### Yoo')
st.markdown('#### Yoo')
st.markdown('##### Yoo')


st.success('You are onboard!Success')            # Success
st.info('Information!')                          # Info
st.warning('Warning!')                           # Warning
st.error('Error!')                               # Error

exp = ZeroDivisionError('Division not possible')
st.exception(exp) 
                                                # Exception
# Takes to the Documentation 
st.help(ZeroDivisionError)

st.write("range(1,10)")                         # Write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)

st.code('x=10\n'                                # Code
        'for i in range(1,x):\n'
            '\tprint(i)')


st.checkbox('Male')                             # Checkbox
st.checkbox('Female')
st.checkbox('Other')


if(st.checkbox('Adult')):                       # Checkbox with Validation
    st.write("You 're an adult.")


st.radio('Select :', ('Check', 'Uncheck'))      # Radio Button
radioButton = st.radio('Select :', ('Student', 'Professional'))

if(radioButton == 'Student'):
    st.write("Enjoy, Have fun!")
elif(radioButton == 'Professional'):
    st.write("Get back to work.")

st.subheader('Select Button')                   # SelectBox
selectBox = st.selectbox("Data Science:",['Data Analysis','Web Scraping',
                        'Machine Learning','Deep Learning',
                        'Natural Language Processing','Computer Vision',
                        'Image Processing'])

st.write('You have selected: ',selectBox) 

st.subheader('Multi-Select Button')             # Multi-SelectBox
multiSelectBox = st.multiselect("Data Science:",['Data Analysis','Web Scraping',
                        'Machine Learning','Deep Learning',
                        'Natural Language Processing','Computer Vision',
                        'Image Processing'])

st.write('You have selected: ',len(multiSelectBox),multiSelectBox)


st.subheader('Button')                         # Button

if(st.button('Click me')):
    st.write('Thanks for clicking me')


st.subheader('Slider')                         # Slider
vol = st.slider('Select the volume',1,100,step=1)
st.write('Volume is:',vol)

st.subheader("Text Input")                      # Text-Input
username = st.text_input('Username:')
password = st.text_input('Password:',type='password')


st.subheader("Text Area")                      # Text-Area
textArea = st.text_area('What are you currently aiming for?')
st.write(textArea)


st.subheader("Input Number")                   # Input-Number
st.number_input("Select your age:",18,110)

st.subheader("Input Date")                     # Input-Date
st.date_input("Date")

st.subheader("Input Time")                     # Input-Time
st.time_input("Time")