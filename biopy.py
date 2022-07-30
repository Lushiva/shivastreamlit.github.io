#import
import streamlit as st
import time

#header
st.header("Biografi")

#photo_profil
from PIL import Image
image = Image.open("pp.jpeg")
st.image(image,width=200,clamp=True,caption="Asifa Ahmad")

#tabs
tab1, tab2, tab3, tab4 = st.tabs(['Personal Information', 'Address', 'Contact', 'Education'])
with tab1:
	st.write('Hi, You can call me Sifa, My real name is Asifa Ahmad.')
	st.write('Informatics Engineering student at [STIMIK Tunas Bangsa Banjarnegara.](https://stb.ac.id/)')
	st.write("I'm interested in software developers, I'm studying [Kotlin](https://id.wikipedia.org/wiki/Kotlin_(bahasa_pemrograman)) programming language and [Python](https://id.wikipedia.org/wiki/Python_(bahasa_pemrograman)) programming language.")
with tab2:
	st.write('I live in Indonesia, Central Java Province, Banjarnegara City.')
with tab3:
	st.write("My Public [Whatsapp Number.](https://wa.me/6285700997818)")
	st.write('Here is My [Instagram.](https://www.instagram.com/_shva_x)')
	st.write('Or My [Facebook.](https://www.facebook.com/achieploonx.kancrutz.9)')
with tab4:
	if st.button('Elementary School'):
		st.header('SDN 1 Kincang')
		st.write('Graduated 2015')
	if st.button('Junior HighSchool'):
		st.header('MTs AlMaarif Rakit')
		st.write('Graduated 2018')
	if st.button('HighSchool'):
		st.header('SMK Panca Bhakti Rakit')
		st.write('Graduated 2021')
	if st.button('College'):
		st.header('STIMIK Tunas Bangsa Banjarnegara')
		st.write('Now')

with st.container():
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")
		st.write(" ")


if st.button('Say hello'):
	my_bar = st.progress(0)

	for percent_complete in range(100):
		time.sleep(0.001)
		my_bar.progress(percent_complete + 1)
	st.info('Hello There!')