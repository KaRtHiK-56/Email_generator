from langchain.prompts import PromptTemplate
from langchain.llms import Ollama
import streamlit as st 

#creating the UI of the code 
st.title("E-mail Generator")
st.header("Your email generating assistance")
contexts = st.text_area("Please enter your email outline/context:",height=250)

#creating the style required to generate the response style of the email
styles = st.selectbox("Style of your email",("Formal", "Informal", "Semi-formal", "Neutral", "Thank you email",

"Formal letter of appreciation",

"Letter of complaint",

"Cover letter",

"Reminder email",

"Letter of apology for a client",

"Apology letter from boss",

"Apology mail for the manager",

"Introduction email to client (outreach)",

"Sample email for proposal submission",

"Proposal submission email",

"Quotation email",

"Email asking for feedback",

"Email of inquiry requesting information",

"Email asking for a status update",

"Sick leave mail format",

"Letter asking for a discount from the supplier",

"Ask for a raise",

"Email your boss about a problem (asking for help)",

"Email to schedule a meeting",

"Email to the client sharing the status of project",

"Email to the boss about work progress",

"Acceptance email",

"Job rejection email"), index=0)

#creating the python function for generating the email response using LLM
def email_genearator(context,style):
    template = " write a contexual and professional email with in 100 words about the outline {context} and in the {style} style"
    prompt_template = PromptTemplate.from_template(template=template)
    prompt = prompt_template.format(context=context,style=style)
    llm = Ollama(model="llama3",temperature=0)
    response = llm(prompt)
    return response


#ceating the submit button and passing the data after submit button is clicked
submit = st.button("Generate")

if submit:
    st.write(email_genearator(contexts,styles))