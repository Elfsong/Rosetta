import os
from tqdm import tqdm
from functools import partial
from multiprocessing import Pool
from google.cloud import translate_v2 as translate

# import Google Service Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./google_key.json"


class Rosetta(object):
    def __init__(self):
        self.client = translate.Client()
    
    @staticmethod
    def batch(iterable, n=1):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx:min(ndx + n, l)]

    def translate_text(self, target, text, source=None):
        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = self.client.translate(text, target_language=target, source_language=source)
        return result

    def translate_file(self, target, output_filename, input_filename, source=None, batch_size=10):
        input_lines = list()
        output_lines = list()

        # [Input=>] Load input lines from input file
        with open(input_filename, 'r', encoding='utf8') as input_file:
            for line in input_file.readlines():
                input_lines += [line.strip()]

        # Batch processing
        # TODO(mingzhe): parallel processing with a pool
        for batch_lines in tqdm(self.batch(input_lines, batch_size), total=len(input_lines) // batch_size):
            batch_result = self.translate_text(target, batch_lines)
            for result in batch_result:
                output_lines += [result["translatedText"]]
        
        # [Output<=] Write output lines to output files
        with open(output_filename, 'w', encoding='utf8') as output_file:
            for line in output_lines:
                output_file.write(line + "\n")
        

if __name__ == "__main__":
    rosetta = Rosetta()

    # Get supported languages
    print(rosetta.client.get_languages())
    
    # Detect source_language and translate to 'zh'
    print(rosetta.translate_text("zh", "Hello, My name is Du Mingzhe."))

    # Translate by given source language and target language
    print(rosetta.translate_text("zh", "Hello, My name is Du Mingzhe.", "en"))

    # Detect source_language and translate to 'zh' in the file way
    rosetta.translate_file("zh-CN", "./output.data", "./input.data")

    # Translate by given source language and target language in the file way
    rosetta.translate_file("zh-CN", "./output.data", "./input.data", "en")