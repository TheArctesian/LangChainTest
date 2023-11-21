#import langchain.llms import OpenAI
# for now wiil change to lama later
#from dotenv import load_dotenv
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

"""
This model is got from install ollama
And running 'ollama run llama2-uncensored
Its about 3gb and you need an okay gpu to run it
"""

def generate(name):
    llm = Ollama(
        model="llama2-uncensored"
         #callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]
         )
    
    proTemp = PromptTemplate(
        input_variables=['name'],
        template = "What is the date and location of birth for {name}"
    )

    nameChain = LLMChain(llm=llm, prompt=proTemp)
    res = nameChain({'name': name})
    return res
# Full API ref: https://api.python.langchain.com/en/latest/llms/langchain.llms.ollama.Ollama.html

if __name__ == "__main__":
    print(generate("Emmanuel Kant"))