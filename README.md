# AI Journalist Assistant

## Overview
This project provides an AI-powered assistant for journalists, leveraging OpenAI's GPT-3.5-turbo model to generate articles based on given facts and writing parameters.

## Features
- Generate articles based on provided facts
- Customize tone, length, and style of the generated content
- Easy-to-use Python interface

## Prerequisites
- Python 3.6+
- OpenAI API key

## Installation
1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-journalist-assistant.git
   cd ai-journalist-assistant
   ```

2. Install the required packages:
   ```
   pip install openai
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root
   - Add your API key: `OPENAI_API_KEY=your-api-key-here`

## Usage
1. Import the necessary modules:
   ```python
   from journalist_assistant import assist_journalist
   ```

2. Call the `assist_journalist` function with your desired parameters:
   ```python
   article = assist_journalist(
       facts=["The sky is blue", "The grass is green"],
       tone="informal",
       length_words=100,
       style="elegant"
   )
   print(article)
   ```

## Configuration
You can modify the `prompt_role` variable in the `journalist_assistant.py` file to adjust the base instructions given to the AI.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
This tool is for assisting journalists and should not be used to generate false or misleading information. Always verify the generated content for accuracy and adhere to journalistic ethics.
