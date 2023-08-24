import openai
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')


st.title("English to Hinglish Translator")
text = st.text_input("Enter the English Text:", "")


SYSTEM_PROMPT = """
You are an AI language model specialized in translating English text to Hinglish. Hinglish is a mixture of Hindi and English language, especially the type of English used by speakers of Hindi. Your translations should sound natural and easy for non-native Hindi speakers to understand.  
""" 

USER_PROMPT = f"""Translate the given English text into Hinglish while strictly adhering to the rules:
Rules:\n
1. The translation must be indistinguishable from casual spoken Hindi. 
2. Specifically retain certain words in English language only to enhance clarity in the translation.
3. Maintain the original meaning of the text.\n

EXAMPLES:\n
English Text: I had about a 30 minute demo just using this new headset
Hinglish: मुझे सिर्फ ३० minute का demo मिला था इस नये headset का इस्तेमाल करने के लिए

Observe in the above example how words like 'headset', 'demo', and 'minute' have been maintained in English to enhance the meaning of the Hinglish translation. 
Similarly, while translating the given text, you need to keep certain words in English to ensure clarity.

\n\nEnglish Text: {text}\n\nHinglish:
"""

def hinglish_translation():

    result = ''

    try: 
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": USER_PROMPT},
                    ],
            temperature=0.3,
            max_tokens=100,
        )

        result = response.choices[0].message["content"]

    except Exception as e:
        result = "Request Failed!!"

    return result




if st.button("Translate"):
    with st.spinner("Translating..."):
        result = hinglish_translation()

    st.success("Hinglish Translation:")
    st.write(result)


