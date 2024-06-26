import config
import torch

class BERTDataset:
    def __init__(self,review,target):
        self.review = review
        self.target = target
        self.tokenizer = config.TOKENIZER
        self.max_len = config.MAX_LEN

    def __len__(self):
        return len(self.review)
    
    def __getitem__(self,item):
        review = str(self.review[item])
        review = " ".join(review.split())

        input = self.tokenizer.encode_plus(
            review,
            None,
            add_special_tokens=True,
            max_length=self.max_len,
            pad_to_max_length=True,
            return_token_type_ids=False
        )
        ids = input['input_ids']
        mask = input['attention_mask']
        token_type_ids = input['token_type_ids']

        padding_length = self.max_len - len(ids)
        ids = ids + ([0] * padding_length)
        mask = mask + ([0] * padding_length)

        token_type_ids = token_type_ids + ([0] * padding_length)

        return {
            'ids': torch.tensor(ids,dtype=torch.long),
            'mask': torch.tensor(mask,dtype=torch.long),
            'token_type_ids': torch.tensor(token_type_ids,dtype=torch.long),
            'targets': torch.tensor(self.target[item],dtype=torch.float)
        }