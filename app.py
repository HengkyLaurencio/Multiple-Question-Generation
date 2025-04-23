from flask import Flask, render_template, request
from transformers import pipeline
import re

app = Flask(__name__)

pipe = pipeline("text2text-generation", model="./model/t5-mqg-base-model", tokenizer="./model/t5-mqg-base-model")

def parse_output(output_str):
    qa_pairs = re.findall(r"Q\d+: (.*?) A\d+: (.*?)(?= Q\d+:|$)", output_str, re.DOTALL)
    return [{"Q": q.strip(), "A": a.strip()} for q, a in qa_pairs]

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        paragraph = request.form["paragraph"]
        if paragraph.strip():
            prompt = "generate questions and answers: " + paragraph
            output_str = pipe(prompt, max_length=256)[0]['generated_text']
            result = parse_output(output_str)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
