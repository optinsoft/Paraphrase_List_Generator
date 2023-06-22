from parrot import Parrot
import torch
import spintax
from random import sample
import warnings
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

def generate(sentences: str, n_spin: int, original_if_no_paraphrase: bool, debug_print: bool = False):
    if debug_print:
        print("-"*100)
        print("Input_sentences (spintax): ", sentences)
        print("-"*100)
    for n in range(n_spin):
        ss = spintax.spin(sentences)
        if debug_print:
            print("-"*100)
            print("Input_sentences (spinned): ", ss)
            print("-"*100)
        s_list = list(filter(None, ss.strip().split('.')))
        if len(s_list) > 0:
            s_para_phrases = []
            for s_phrase in s_list:
                phrase = s_phrase.strip()
                if debug_print:
                    print("-"*100)
                    print("Input_phrase: ", phrase)
                    print("-"*100)
                para_phrases = parrot.augment(input_phrase=phrase, use_gpu=False)
                if debug_print:
                    print("-"*100)
                    print("Paraphrases:")
                    print("-"*10)
                if para_phrases is None:
                    if original_if_no_paraphrase:
                        para_phrase = (phrase, 0)
                        para_phrases = [para_phrase]
                    else:
                        if debug_print:
                            print("--- None ---")
                        para_phrases = []
                for para_phrase in para_phrases:
                    if debug_print:
                        print(para_phrase)
                s_para_phrases.append(para_phrases)
            if len(s_list) == len(s_para_phrases):
                if debug_print:
                    print("-"*100)
                    print("Output_sentences:")
                    print("-"*10)
                for s in generateS(s_para_phrases, 0):
                    if debug_print:
                        print(s)
                    yield s

if __name__ == '__main__':
    n_top = 100
    n_spin = 1
    original_if_no_paraphrase = True
    debug_print = True
    with open('phrases.txt') as fin:
        phrases = fin.readlines()      
    if len(phrases) < n_top: n_top = len(phrases)
    r_phrases = sample(phrases, n_top)
    sentences = []
    for phrase in r_phrases:
        for s in generate(phrase, n_spin, original_if_no_paraphrase, debug_print):
            sentences.append(s)
    sentences = sample(sentences, len(sentences))
    with open('sentences.txt', 'w') as fout:
        for s in sentences:
            fout.write(s + "\n")
