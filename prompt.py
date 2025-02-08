from langchain_community.llms import Ollama

SYSTEM_PROMPT = """
நீங்கள் உதவிகரமான மற்றும் மரியாதைக்குரிய மற்றும் நேர்மையான AI உதவியாளர். எப்போதும் முடிந்தவரை உதவிகரமாக பதிலளிக்கவும்.
ஒரு கேள்விக்கான பதில் உங்களுக்குத் தெரியாவிட்டால், தவறான தகவல்களைப் பகிர வேண்டாம்.
"""

def firePrompt(prompt: str, temp=0.4) -> str:
    """Generates a response from the Ollama model based on the given prompt."""
    llm = Ollama(  # Initialize the Ollama model
        system=SYSTEM_PROMPT,
        temperature=temp
    )
    
    # Invoke the model with the prompt
    response = llm.invoke(prompt)
    
    return response
