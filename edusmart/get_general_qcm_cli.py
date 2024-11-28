from utils.utils import *
import argparse
import os


def save_qcm_to_html(qcm_data, output_file="qcm_output.html"):
    """
    Convert QCM data to a formatted HTML file with properly separated text and LaTeX
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>QCM Questions</title>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
            }
            .question {
                margin-bottom: 30px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            .question-text {
                font-weight: bold;
                margin-bottom: 15px;
                font-size: 1.2em;
            }
            .question-content {
                margin-bottom: 15px;
                font-style: italic;
            }
            .options {
                margin-left: 20px;
            }
            .option {
                margin: 15px 0;
                padding: 10px;
                background-color: white;
                border-radius: 4px;
                border: 1px solid #eee;
            }
            .correct-answer {
                color: #2e7d32;
                font-weight: bold;
                margin-top: 15px;
                padding: 10px;
                background-color: #e8f5e9;
                border-radius: 5px;
            }
        </style>
        <script>
            MathJax = {
                tex: {
                    inlineMath: [['$', '$']],
                    displayMath: [['$$', '$$']],
                    processEscapes: true,
                    packages: ['base', 'ams', 'noerrors', 'noundefined']
                }
            };
        </script>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        <h1>QCM Questions</h1>
    """
    
    def fix_latex(text):
        """Clean up LaTeX formatting"""
        # Remove extra backslashes and fix spacing
        text = text.replace('\\\\', '\\')
        # Ensure math expressions are properly delimited
        if '\\mathbb' in text or '\\forall' in text or '\\exists' in text or '\\geq' in text:
            if not text.startswith('$'):
                text = '$' + text
            if not text.endswith('$'):
                text = text + '$'
        return text

    def process_option(option):
        """Process each option to separate letter label and content"""
        parts = option.split(' - ', 1)
        if len(parts) == 2:
            label, content = parts
            return f"{label} - {fix_latex(content)}"
        return fix_latex(option)

    # Add each question
    for i, item in enumerate(qcm_data['data'], 1):
        question = fix_latex(item['question'])
        
        html_content += f"""
        <div class="question">
            <div class="question-text">Question {i}:</div>
            <div class="question-content">{question}</div>
            <div class="options">
        """
        
        # Add options
        for option in item['options']:
            processed_option = process_option(option)
            html_content += f'<div class="option">{processed_option}</div>'
        
        # Add correct answer
        html_content += f"""
            </div>
            <div class="correct-answer">Correct Answer: {item['correct_answer']}</div>
        </div>
        """
    
    html_content += """
    </body>
    </html>
    """
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"QCM has been saved to {output_file}")



def main(level, year, branch, subject, lesson, difficulty, num_questions):
    qcm_data =  generate_general_qcm(level, year, branch, subject, lesson, difficulty, num_questions) #json.loads(cv.example_generated_qcm)
    save_qcm_to_html(qcm_data, output_file="qcm_output.html")
    #print(qcm_data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Description of your script functionality.")

    # Add arguments
    parser.add_argument("--level", type=str, help="lycee, college or primaire", default="lycee")
    parser.add_argument("--year", type=str, help="Ex: tronc_commun, 1_bac, 2_bac", default="1_bac")
    parser.add_argument("--branch", type=str, help="Ex: sci_eco, sci_math...", default="sci_math")
    parser.add_argument("--subject", type=str, help="Ex: math...", default = "math")
    parser.add_argument("--lesson", type=str, help="Ex: notion_de_logique...", default = "notion_de_logique")
    parser.add_argument("--difficulty", type=str, help="Facile, Moyen ou Difficile", default = "Moyen")
    parser.add_argument("--num_questions", type=int, help="Number of questions to generate", default = 5)


    # Parse arguments and pass them to main
    args = parser.parse_args()
    main(args.level, args.year, args.branch, args.subject, args.lesson, args.difficulty, args.num_questions)


