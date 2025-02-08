# WhatsApp Chat Analyzer

A Python-based application that reads WhatsApp exported chat logs and generates useful insights, such as:

- Total message count
- Most frequent contacts
- Distribution of messages over time
- Word cloud generation for popular words

This tool helps visualize chat data and can be useful for personal use or for understanding message patterns.

## Features

- **Message Count**: Displays the total number of messages sent and received.
- **Frequent Contacts**: Lists the contacts you interact with the most.
- **Time Analysis**: Shows how messages are distributed over time (e.g., daily, monthly).
- **Word Cloud**: Generates a word cloud visualization for frequently used words in the chat.
- **Export Data**: Option to export the analysis results to a file (CSV, JSON, etc.).

## Installation

Follow these steps to install and set up the WhatsApp Chat Analyzer:

### Clone the repository:
```bash
git clone https://github.com/Adity-star/Whatsapp-chat-analyzer.git
cd Whatsapp-chat-analyzer
```

### Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
```

### Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Export your WhatsApp chat:
1. Open WhatsApp and navigate to the chat you want to analyze.
2. Tap on the three dots in the top right corner > More > Export Chat.
3. Choose whether to include media or not (for this tool, it's fine to just include text).
4. Place the exported `.txt` file in the project directory.

### Run the analyzer:
```bash
python chat_analyzer.py your_chat.txt
```
Replace `your_chat.txt` with the actual name of your exported chat file.

### View the results:
The results will be displayed in the terminal or saved to an output file, depending on your configuration.

### Generate a word cloud (optional):
```bash
python wordcloud_generator.py
```
This will generate and display a word cloud of the most frequently used words in your chat.

## Technologies Used

- **Python**: Core programming language.
- **Pandas**: For data analysis and manipulation.
- **Matplotlib**: For visualizing data.
- **WordCloud**: For generating word cloud visualizations.
- **Regex**: For parsing and processing the WhatsApp chat export.

## Contributing

We welcome contributions and suggestions! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -am 'Add new feature'
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **WhatsApp** for the exported chat format.
- **Python Libraries**: Pandas, Matplotlib, and WordCloud for their awesome contributions.

Feel free to modify this README based on your project updates. Let me know if you need further adjustments!

