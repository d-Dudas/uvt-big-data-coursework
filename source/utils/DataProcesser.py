from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

from scipy.sparse import csr_matrix
from scipy.sparse import hstack

class DataProcesser:
    def __init__(self, df):
        self.df = df
        self.ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=True)
        self.user_id_encoder = LabelEncoder()
        self.label_encoder = LabelEncoder()
        self.tfidf = TfidfVectorizer(max_features=500)

    def get_encoded_features(self):
        process_and_event_name_encoded = self.ohe.fit_transform(self.df[['processName', 'eventName']])

        user_id_encoded = self.user_id_encoder.fit_transform(self.df['userId'])
        user_id_encoded = user_id_encoded.reshape(-1, 1) 
        user_id_sparse = csr_matrix(user_id_encoded)

        args_encoded = self.tfidf.fit_transform(self.df['args'].astype(str))

        return hstack([process_and_event_name_encoded, user_id_sparse, args_encoded])
    
    def get_encoded_labels(self):
        return self.label_encoder.fit_transform(self.df['label'].values)

    def encode_features(self, df):
        process_and_event_name_encoded = self.ohe.transform(df[['processName', 'eventName']])

        user_id_encoded = self.user_id_encoder.transform(df['userId'])
        user_id_encoded = user_id_encoded.reshape(-1, 1) 
        user_id_sparse = csr_matrix(user_id_encoded)

        args_encoded = self.tfidf.transform(df['args'].astype(str))

        return hstack([process_and_event_name_encoded, user_id_sparse, args_encoded])
    
    def encode_labels(self, df):
        return self.label_encoder.transform(df['label'].values) 
    
    def decode_labels(self, labels):
        return self.label_encoder.inverse_transform(labels)