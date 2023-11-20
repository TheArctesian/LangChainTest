#import langchain.llms import OpenAI
# for now wiil change to lama later
#from dotenv import load_dotenv
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.llms import Ollama

llm = Ollama(
    model="llama2-uncensored", callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

if __name__ == "__main__":
    print(llm("Tell me why trump should win the election in 2024"))