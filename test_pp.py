from parrot import Parrot
import torch
import warnings
import spintax
warnings.filterwarnings("ignore")

''' 
uncomment to get reproducable paraphrase generations
def random_state(seed):
  torch.manual_seed(seed)
  if torch.cuda.is_available():
    torch.cuda.manual_seed_all(seed)

random_state(1234)
'''

#Init models (make sure you init ONLY once if you integrate this to your code)
parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5")

def generateS(s_para_phrases, i):
    if i < len(s_para_phrases):
        p_list = s_para_phrases[i]
        for para_phrase in p_list:
            if i+1 < len(s_para_phrases):
                for t in generateS(s_para_phrases, i+1):
                    yield para_phrase[0].capitalize() + ". " + t
            else:
                yield para_phrase[0].capitalize() + ". "

def generate(sentences: str, n_spin: int):
    for n in range(n_spin):
        ss = spintax.spin(sentences)
        s_list = list(filter(None, ss.split('.')))
        if len(s_list) > 0:
            s_para_phrases = []
            for phrase in s_list:
                print("-"*100)
                print("Input_phrase: ", phrase)
                print("-"*100)
                para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
                if para_phrases is None:
                    print("--- None ---")
                else:
                    for para_phrase in para_phrases:
                        print(para_phrase)
                    s_para_phrases.append(para_phrases)
            if len(s_list) == len(s_para_phrases):
                print("-"*100)
                print("Sentences:")
                print("-"*100)
                for s in generateS(s_para_phrases, 0):
                    print(s)

s_phrase = "Your {patronage|business|purchasing|purchases|support} is very much {appreciated|relished|cherished|highly valued|really liked|revered|gracious}. We are {grateful|fortunate|privileged|honored|appreciative} to have {consumer|client|patron|customer} like you."

generate(s_phrase, 3)
