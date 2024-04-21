import transformers
import tokenizers

MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
#ACCUMULATION = 2
BERT_PATH = "E:/NLP/Sentiment Analysis/bert_base_uncased/"
MODEL_PATH = "model.bin"
TRAINING_FILE = "E:/NLP/Sentiment Analysis/IMDB Dataset.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH,do_lower_Case = True)
        # f"{BERT_PATH}/vocab.txt", 
        # lowercase=True)
    



