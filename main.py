import streamlit as st
import os
import re
import requests
import openai

openai.api_key = ""



st.sidebar.title('KANJI MASTER')
st.sidebar.text("@ Welcome in Kanji Master ")
st.sidebar.title('Page Selection Menu')
page = st.sidebar.radio("Select Required Feature",("English word to Kanji",))
test_prompt = "above"
model_name = "curie:ft-personal-2023-01-31-04-43-24"
if page=='English word to Kanji':
	st.title('English word to Kanji')
	test_prompt = st.text_area("Enter your english  word",'')

	if st.button("Generate Kanji !"):
		if test_prompt=="":
			st.error("Please enter your word")
		else:	
			with st.spinner("Fetching response..."):
				response = openai.Completion.create(
					engine=model_name,
					prompt= test_prompt,
					temperature=0.6,
					max_tokens=600,
					top_p=0.7,
					frequency_penalty=0,
					presence_penalty=0.6,
					stop = ["END"],)




				st.markdown(response['choices'][0]['text'])
			    
				#match =re.search('-> (.+?)end', response['choices'][0]['text'])
				#if match:

					#result = match.group(1)
					#st.write(result)


				#else:
					#st.write("No match found.")
			
			
			#if result:
			
  				#print(result.group(1))
			
			
			#st.markdown(response['choices'][0]['text'])'''




