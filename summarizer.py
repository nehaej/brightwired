#adap summarizer + will add TTS and STT ltr
from transformers import BartForConditionalGeneration, AutoTokenizer
from ollama import chat
from ollama import ChatResponse
import textstat
import spacy

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
summarizer = BartForConditionalGeneration.from_pretrained("sshleifer/distilbart-cnn-12-6")
nlp = spacy.load("en_core_web_sm")

def modes(text, mode="Academic-Lite") :  # choosing output style
    
    if mode == "Child Core" :
        response = childify_prompt(text)
    elif mode == "Conversational" :
        response = converse_prompt(text)
    else:
        response = acad_prompt(text)
    return generate(response)

def childify_prompt(text) :    # prompts sent to llm
  
  prompt = f"You are a helpful assistant that explains complex ideas for a 10 yr old.Use very simple  ENGLISH language and juvenile tone. Do not summarize.Avoiding introductory phrases or extraneous information or any conclusive questions/statements,TEXT:\n\n{text}"
  return prompt

def converse_prompt(text) :

  prompt = f"Explain this like a cool genz friend talking to a teenager. Make sure to give the full explanation in ENGLISH, avoid summarization. USE ENGLISH ONLY.Avoid introductory words or extraneous sentences,TEXT:\n\n{text}"
  return prompt

def acad_prompt(text) :

  prompt = f"Explain this academic text. Don't shorten or summarize anything. Just use clearer, easier, formal ENGLISH language.ONLY USE ENGLISH.Avoid all introductory phrases or extraneous sentences, TEXT:\n\n{text}"
  return prompt

def generate(prompt):
    
    try:
      response: ChatResponse = chat(model="qwen2.5:0.5b", messages=[{'role': 'user','content': prompt}])
    
      return response.message.content

    except Exception as e:
       print(f"Error:{e}")
       


def summary(len_type, text, mode) :  # if user wants to summarize then summarize 

    simplified_text = modes(text, mode)
    
    if len_type == "as is" :
        return simplified_text  # if user wants to summarize then only summarize 
    
    inputs = tokenizer([simplified_text], max_length=1024, truncation=True, return_tensors="pt")
    if len_type == "tldr" :
        min_len, max_len = 50, 100
    elif len_type == "medium" :
        min_len, max_len = 100, 200
    elif len_type == "full" :
        min_len, max_len = 200, 500
    else :
        raise ValueError("Invalid summary len_type")
        
    summary_ids = summarizer.generate(inputs["input_ids"], num_beams=4, min_length=min_len, max_length=max_len, early_stopping=True)
    result = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return result
   
    

def read_improve(old_text,new_text) :   # comparing old and new text to see which is btr
    try:
        original = textstat.flesch_reading_ease(old_text)
        simplify = textstat.flesch_reading_ease(new_text)
        improve = simplify - original
        if improve > 0 :
            return f"Readiblity improved by {improve:.1f} points"
        else :
            return f"Difficulty remained the same"
    except Exception as e :
        return f"Error: {e}"

def keyword_extrct(result) :
    doc = nlp(result)
    return [token.lemma_.lower() for token in doc if token.pos_ in ("NOUN","PROPN", "ADJ")]
            