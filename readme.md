# GraphRAG + GPT-4o mini Knowledge Graph Retrieval Application
[中文版](README_CN.md) | [English](README.md)
## Introduction

This is a Streamlit-based web application that utilizes GraphRAG and GPT-4o mini to build and query knowledge graphs. The application supports both Chinese and English interfaces, allowing users to upload text files, build knowledge indexes, and perform queries.

## Features

- Bilingual interface (Chinese/English)
- Text file upload
- Automatic installation of GraphRAG
- Knowledge graph index construction
- GPT-4o mini-based query functionality

## Requirements

- Python 3.7+
- Streamlit
- GraphRAG (automatically installed by the application)
- OpenAI API key

## Installation

1. Clone this repository:
``` git clone https://github.com/ehowang/graphrag-webui.git```

1. Install dependencies:
   run the script to install dependencies
   - MacOS/Linux:```init.sh```
   - Windows：```init.bat```

## Usage

1. Run the application:```streamlit run app.py```

2. Open the displayed URL in your browser (typically http://localhost:8501).

3. Using the interface:
   - Select your preferred language (Chinese/English)
   - Upload a text file (.txt format)
   - Enter your OpenAI API key
   - Click the "Initialize and Build Index" button
   - Enter your question in the query box and click "Execute Query"

## Notes

- Ensure you have a valid OpenAI API key.
- Uploaded text files should be in plain text format (.txt).
- On first run, the application will automatically install GraphRAG, which may take some time.

## Troubleshooting

If you encounter issues:
- Ensure your Python version is compatible (3.7+)
- Check if the API key is entered correctly
- Review the console output for detailed error messages

## Contributing

Issues and pull requests are welcome to help improve this project.

