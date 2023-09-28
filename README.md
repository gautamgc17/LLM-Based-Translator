## English to Hinglish Translator using OpenAI's GPT-3

## Objective
Create a conversational interface to collect user information. The chat agents should guide users naturally and persuade them to provide information.

## Features
Designed a coherent conversation flow to collect Name, Email, Phone Number, Address, Date of Birth, and Education, using OpenAI language model: GPT-4 for chat responses and to implement multiple roles like "Introduction Agent," "Information Gathering Agent," "Validation Agent," and "Formatting Agent."

## Prerequisites
Before running the application, you'll need the following:

- Python 3.11 installed
- OpenAI API key (set as environment variable OPENAI_API_KEY)
- Streamlit and other required Python packages (install using pip install -r requirements.txt)


## Getting Started

**Step 1. Clone the repository to your local machine and then switch to code directory**

```
git clone https://github.com/gautamgc17/Translation.git
cd Translation
```

**Step 2. Create a Virtual Environment and install Dependencies.**

```
pip install virtualenv
```

Create a new Virtual Environment for the project and activate it.

```
virtualenv env
env\Scripts\activate
```
Once the virtual environment is activated, the name of your virtual environment will appear on left side of terminal.

Next, we need to install the project dependencies in this virtual environment, which are listed in `requirements.txt`.

```
pip install -r requirements.txt
```

**Step3. Set your OpenAI API key as an environment variable named OPENAI_API_KEY**

Create a file named _.env_ and store your [OpenAI API Key](https://platform.openai.com/account/api-keys) credentials in this file.

```
OPENAI_API_KEY = 'sk-'
```

**Step 4. Run the Streamlit application**

```
streamlit run main.py
```

## Usage
- Access the web application by visiting the provided URL after running the Streamlit application.
- Enter the English text you want to translate into the input field.
- Click the "Translate" button to initiate the translation process.
- The translated Hinglish text will be displayed below the input field.

## How it Works
- The application uses Streamlit for the user interface and interaction.
- It communicates with OpenAI's GPT-3 model using the openai Python library.
- The GPT-3 model is provided with system and user prompts to guide the translation process.
- Specific rules are applied to retain clarity, such as keeping certain words in English within the translation.
- The translation result is displayed on the Streamlit web interface.

## Examples
#### Example Input 1 - 


![example1](https://github.com/gautamgc17/Translation/blob/a3f4f9062f7413b36992e38ff8f94421c219b104/assets/2.PNG)

<br>

#### Example Input 2 -


![example1](https://github.com/gautamgc17/Translation/blob/a3f4f9062f7413b36992e38ff8f94421c219b104/assets/1.PNG)

<br>

#### Example Input 3 - 


![example1](https://github.com/gautamgc17/Translation/blob/a3f4f9062f7413b36992e38ff8f94421c219b104/assets/3.PNG)

<br>

#### Example Input 4 - 


![example1](https://github.com/gautamgc17/Translation/blob/a3f4f9062f7413b36992e38ff8f94421c219b104/assets/4.PNG)

<br>

## Notes
- The translation quality may vary based on the complexity of the input text.
- The GPT-3 model's responses might not always be perfect and might require adjustments.
- Feel free to experiment with different input texts and adjust the translation parameters.
