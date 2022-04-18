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

    def translate_file(self, target, input_filename, output_filename, source=None, batch_size=10):
        input_lines = list()
        output_lines = list()

        # Load input lines from input file
        with open(input_filename, 'r', encoding='utf8') as input_file:
            for line in input_file.readlines():
                input_lines += [line.strip()]

        # Batch processing
        print(f"Approximate batches: {len(input_lines) / batch_size}")
        for batch_lines in tqdm(self.batch(input_lines, batch_size)):
            batch_result = self.translate_text(target, batch_lines)
            for result in batch_result:
                output_lines += [result["translatedText"]]
        
        # Write output lines to output files
        with open(output_filename, 'w', encoding='utf8') as output_file:
            for line in output_lines:
                output_file.write(line + "\n")
        

if __name__ == "__main__":
    rosetta = Rosetta()
    # result = rosetta.translate_text("zh-CN", "Ban")
    rosetta.translate_file("zh-CN", "./input.data", "./output.data")