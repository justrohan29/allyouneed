import streamlit as st
import webbrowser

st.title('Percentage Calculator for Two Term System of CBSE.')
st.subheader('Check you percentage here :)')
t1 = st.slider('Enter your Term 1 Percentage:', 0, 100)



total = st.slider('Enter Percentage you want to achieve:', 0, 100)
o1 = st.slider('Enter term-1 weightage:', 0, 100)
o2 = 100 - o1
#total*100 = (o1*t1+o2*x)
a = total*100
b = o1*t1
c = a-b
answer = c/o2


if st.button('Get Answer'):
	if answer < 100:
     		st.success(answer)
	else:
		st.error('Required Percentage is above 100. Sorry, please lower your expectations :)')



#with st.sidebar:
#	if st.button('Study Resources'):
 #   		webbrowser.open_new_tab('www.cbse.online')
#	if st.button('Check me out'):
 #   		webbrowser.open_new_tab('https://just--rohan.blogspot.com/')
	st.write('Made By: Rohan Singh🙏')
