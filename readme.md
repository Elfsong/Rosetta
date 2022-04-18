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
