#!/usr/bin/env python
# coding: utf-8

# In[1]:


import collections
from nltk.corpus import reuters
def get_sorted_categories_with_counts():
    cat_dic = {}
    categories = reuters.categories()
    for cat in categories:
        files = reuters.fileids(cat)
        train_files = list(filter(lambda doc: doc.startswith("train"), files))
        cat_dic[cat] = len(train_files)
    return collections.OrderedDict(sorted(cat_dic.items(), key=lambda x: x[1], reverse=True))


# In[11]:


def get_label_file_mapping():
    documents = reuters.fileids()
    mapping = {}
    train_docs_id = list(filter(lambda doc: doc.startswith("train"), documents))
    for t_id in train_docs_id:
        cats = reuters.categories(t_id)
        for cat in cats:
            if cat in mapping:
                mapping[cat].append(t_id)
            else:
                mapping[cat] = []
                mapping[cat].append(t_id)
    return mapping

