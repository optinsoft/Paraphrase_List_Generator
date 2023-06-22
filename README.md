# Paraphrase List Generator

## Install

```bash
pip install git+https://github.com/PrithivirajDamodaran/Parrot_Paraphraser.git
pip install transformers[torchhub]
pip install sentencepiece
pip install python-Levenshtein 
pip install fuzzywuzzy
pip install sentence-transformers
pip install pandas
pip install spintax
```

## Usage

Create source file `phrases.txt` with phrases for which you would like to generate paraphrases. You can use spintax here. Example ("Business Thank-You Phrases"): 

```text
I appreciate your assistance and look forward to your continuing to work on our account.
Many thanks for giving me this opportunity.
Thank you for referring your {clients|customers} to me for Opt-In List Manager.
Thank you for referring us to {Microsoft|Google|Facebook}.
Thanks very much for the assistance you provide my business. I sincerely appreciate it.
```

Run `pp.py` script:

```bash
python ./pp.py
```

Output file `sentences.txt` will look like this:

```text
Thank you very much for the support that you give my business. I sincerely appreciate it. 
Thank you for the support you gave my business. I'm so grateful. 
Thank you so much for giving me this opportunity. 
Thank you very much for helping me with my business. I'm so grateful. 
Thank you for the support you gave my business. I'm truly grateful for this. 
Thank you for referring your customers to me for opt-in list manager. 
Thank you very much for the support that you give my business. I'm so grateful. 
Thank you very much for the support that you give my business. I'm really grateful. 
Thank you for your assistance and i look forward to continuing to work on our account. 
Thank you for referring to google. 
Thank you very much for helping me with my business. I'm truly grateful for this. 
I appreciate your help and look forward to you continuing to work on our account. 
Thank you for the support you gave my business. I sincerely appreciate it. 
Thank you very much for helping me with my business. I sincerely appreciate it. 
Thank you very much for the support that you give my business. I'm truly grateful for this. 
Thank you very much for helping me with my business. I'm really grateful. 
Thank you for linking us to google. 
Thank you for giving me this opportunity. 
Thank you for pointing us to google. 
Thank you for referring us to google. 
I appreciate your help and look forward to your continuing work on our account. 
Thank you for the support you gave my business. I'm really grateful. 
I appreciate your assistance and look forward to you continuing to work on our account. 
I appreciate your assistance and look forward to working on our account with you. 
```