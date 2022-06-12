# Rosetta

## Install

```shell
# Create a conda environment
conda create -n rosetta python=3.7
conda activate rosetta
```

```shell
# Install Google Translate Client
pip install google-cloud-translate==2.0.1
```

## Setup Google Cloud
Google Translate API is **chargeable**. We must pay for this. Fortunately, Google offers every new user a $300 credit. You can use it to cover the cost.
So, the first thing is to set up a new Google cloud account.

## Enable Google Translate API
[Google Translate API](https://console.cloud.google.com/apis/library/translate.googleapis.com?project=lucky-re)

Enable this API, and you can also estimate the cost by referencing the Pricing part.

## Get Credentials
[Credentials](https://console.cloud.google.com/apis/credentials)

Create a Service Account which can access Translate APIs, than generate a JSON key of the Service Account.
Set GOOGLE_APPLICATION_CREDENTIALS at Line 8: [Code](https://github.com/Elfsong/Rosetta/blob/main/rosetta.py)

## Usage
```python
# Get supported languages
print(rosetta.client.get_languages())
    
# Detect source_language and translate to 'zh'
print(rosetta.translate_text("zh", "Hello, My name is Du Mingzhe."))

# Translate by given source language and target language
print(rosetta.translate_text("zh", "Hello, My name is Du Mingzhe.", "en"))

# Detect source_language and translate to 'zh' in the file way
rosetta.translate_file("zh", "./output.data", "./input.data")

# Translate by given source language and target language in the file way
rosetta.translate_file("zh", "./output.data", "./input.data", "en")
```
