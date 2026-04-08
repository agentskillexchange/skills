---
title: KeyBERT Minimal Keyword Extraction with BERT Embeddings
description: 'Overview KeyBERT is a lightweight Python library for keyword and keyphrase
  extraction that uses BERT-based transformer embeddings to identify the most relevant
  terms in a document. Unlike traditional statistical keyword extractors (TF-IDF,
  RAKE), KeyBERT leverages the semantic understanding of transformer models to find
  keywords that truly represent the meaning of a text. How It Works KeyBERT extracts
  document-level embeddings using sentence-transformers and compares them against
  n-gram candidate embeddings using cosine similarity. The candidates with the highest
  similarity to the full document embedding are selected as keywords. Two diversity
  algorithms are supported: Max Sum Similarity (maximizes candidate distance while
  maintaining relevance) and Maximal Marginal Relevance (iteratively selects keywords
  that are both relevant and diverse). Key Features Multiple embedding backends: sentence-transformers,
  Flair, spaCy, and Gensim Configurable n-gram range: Extract single keywords or multi-word
  keyphrases Diversity algorithms: MMR and Max Sum for diverse keyword sets Guided
  extraction: Seed keywords to guide the extraction toward specific topics Highlight
  mode: Visualize extracted keywords directly in the source document Vectorizer support:
  Use CountVectorizer or KeyphraseCountVectorizer for candidate generation Agent Integration
  AI agents can use KeyBERT for automated content analysis workflows: extracting keywords
  from blog posts for SEO tagging, generating topic summaries from research papers,
  building content taxonomies, or creating keyword-driven content briefs. The Python
  API is straightforward — instantiate KeyBERT with a model, call extract_keywords()
  with your text, and receive ranked keyword-score pairs. Installation pip install
  keybert For additional backends: pip install keybert[flair] or pip install keybert[gensim]
  Quick Example from keybert import KeyBERT kw_model = KeyBERT() keywords = kw_model.extract_keywords(doc,
  keyphrase_ngram_range=(1, 2), stop_words="english", top_n=10)'
verification: security_reviewed
source: https://github.com/MaartenGr/KeyBERT
category:
- Content Writing &amp; SEO
framework:
- Custom Agents
tool_ecosystem:
  github_repo: MaartenGr/KeyBERT
  github_stars: 4143
---

# KeyBERT Minimal Keyword Extraction with BERT Embeddings

Overview KeyBERT is a lightweight Python library for keyword and keyphrase extraction that uses BERT-based transformer embeddings to identify the most relevant terms in a document. Unlike traditional statistical keyword extractors (TF-IDF, RAKE), KeyBERT leverages the semantic understanding of transformer models to find keywords that truly represent the meaning of a text. How It Works KeyBERT extracts document-level embeddings using sentence-transformers and compares them against n-gram candidate embeddings using cosine similarity. The candidates with the highest similarity to the full document embedding are selected as keywords. Two diversity algorithms are supported: Max Sum Similarity (maximizes candidate distance while maintaining relevance) and Maximal Marginal Relevance (iteratively selects keywords that are both relevant and diverse). Key Features Multiple embedding backends: sentence-transformers, Flair, spaCy, and Gensim Configurable n-gram range: Extract single keywords or multi-word keyphrases Diversity algorithms: MMR and Max Sum for diverse keyword sets Guided extraction: Seed keywords to guide the extraction toward specific topics Highlight mode: Visualize extracted keywords directly in the source document Vectorizer support: Use CountVectorizer or KeyphraseCountVectorizer for candidate generation Agent Integration AI agents can use KeyBERT for automated content analysis workflows: extracting keywords from blog posts for SEO tagging, generating topic summaries from research papers, building content taxonomies, or creating keyword-driven content briefs. The Python API is straightforward — instantiate KeyBERT with a model, call extract_keywords() with your text, and receive ranked keyword-score pairs. Installation pip install keybert For additional backends: pip install keybert[flair] or pip install keybert[gensim] Quick Example from keybert import KeyBERT kw_model = KeyBERT() keywords = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=10)

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keybert-keyword-extraction-bert/)
