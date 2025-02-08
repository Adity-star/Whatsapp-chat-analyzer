The WhatsApp Chat Analyzer is a Python-based application 
that reads WhatsApp exported chat logs and generates useful insights, such as:

Total message count.
Most frequent contacts.
Distribution of messages over time.
Word cloud generation for popular words.
This tool helps in visualizing chat data and can be useful for personal use or for understanding message patterns.

Features
1. Message Count: Displays the total number of messages sent and received.
2. Frequent Contacts: Lists the contacts you interact with the most.
3. Time Analysis: Shows how messages are distributed over time (e.g., daily, monthly).
4. Word Cloud: Generates a word cloud visualization for frequently used words in the chat.
5. Export Data: Option to export the analysis results to a file (CSV, JSON, etc.).
   
Installation
Follow these steps to install and set up the WhatsApp Chat Analyzer:

Clone the repository:

`bash
git clone https://github.com/Adity-star/Whatsapp-chat-analyzer.git`

Navigate to the project directory:

`bash
cd Whatsapp-chat-analyzer`

Create a virtual environment (optional but recommended):
If you're using venv:
`bash
python3 -m venv venv`

Activate the virtual environment:
On Windows:
`bash
venv\Scripts\activate`

On macOS/Linux:
`bash
source venv/bin/activate`

Install dependencies:
`bash
pip install -r requirements.txt`

Usage
Export your WhatsApp chat:

On WhatsApp, go to the chat you want to analyze.
Tap on the three dots in the top right corner > More > Export Chat.
Choose whether to include media or not (for this tool, it's fine to just include text).
Run the analyzer:

After exporting the chat, place the .txt file in the project directory.
Run the following command in the terminal:
bash
Copy
Edit
python chat_analyzer.py your_chat.txt
Replace your_chat.txt with the actual name of your exported chat file.

View the results:

The results will be displayed in the terminal or a separate output file, depending on your configuration.
Generate visualizations (optional):

If you want to generate a word cloud, use the following command:
bash
Copy
Edit
python wordcloud_generator.py
This will generate and display a word cloud of the most frequently used words in your chat.

Technologies
This project uses the following technologies:

Python: The programming language used for the project.
Pandas: For data analysis and manipulation.
Matplotlib: For data visualization (charts/graphs).
WordCloud: For generating word cloud visualizations.
Regex: For parsing and processing the WhatsApp chat export.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your branch (git push origin feature/your-feature).
Open a pull request.
We welcome contributions and suggestions! If you find any bugs or have an idea for an improvement, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
WhatsApp for the exported chat format.
Python Libraries: Pandas, Matplotlib, WordCloud for their awesome contributions.
Any other libraries or resources you've used, feel free to add here.
Feel free to customize the Features, Usage, or any section based on the actual functionality of your project. If your project includes specific files (like chat_analyzer.py or wordcloud_generator.py), be sure to mention them and provide usage instructions accordingly. Let me know if you need any further adjustments!

Total message count.
Most frequent contacts.
Distribution of messages over time.
Word cloud generation for popular words.
This tool helps in visualizing chat data and can be useful for personal use or for understanding message patterns.

Features
Message Count: Displays the total number of messages sent and received.
Frequent Contacts: Lists the contacts you interact with the most.
Time Analysis: Shows how messages are distributed over time (e.g., daily, monthly).
Word Cloud: Generates a word cloud visualization for frequently used words in the chat.
Export Data: Option to export the analysis results to a file (CSV, JSON, etc.).
Installation
Follow these steps to install and set up the WhatsApp Chat Analyzer:

Clone the repository:

bash
Copy
Edit
git clone https://github.com/Adity-star/Whatsapp-chat-analyzer.git
Navigate to the project directory:

bash
Copy
Edit
cd Whatsapp-chat-analyzer
Create a virtual environment (optional but recommended):

If you're using venv:
bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy
Edit
venv\Scripts\activate
On macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Usage
Export your WhatsApp chat:

On WhatsApp, go to the chat you want to analyze.
Tap on the three dots in the top right corner > More > Export Chat.
Choose whether to include media or not (for this tool, it's fine to just include text).
Run the analyzer:

After exporting the chat, place the .txt file in the project directory.
Run the following command in the terminal:
bash
Copy
Edit
python chat_analyzer.py your_chat.txt
Replace your_chat.txt with the actual name of your exported chat file.

View the results:

The results will be displayed in the terminal or a separate output file, depending on your configuration.
Generate visualizations (optional):

If you want to generate a word cloud, use the following command:
bash
Copy
Edit
python wordcloud_generator.py
This will generate and display a word cloud of the most frequently used words in your chat.

Technologies
This project uses the following technologies:

Python: The programming language used for the project.
Pandas: For data analysis and manipulation.
Matplotlib: For data visualization (charts/graphs).
WordCloud: For generating word cloud visualizations.
Regex: For parsing and processing the WhatsApp chat export.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes and commit them (git commit -am 'Add new feature').
Push to your branch (git push origin feature/your-feature).
Open a pull request.
We welcome contributions and suggestions! If you find any bugs or have an idea for an improvement, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
WhatsApp for the exported chat format.
Python Libraries: Pandas, Matplotlib, WordCloud for their awesome contributions.
Any other libraries or resources you've used, feel free to add here.
Feel free to customize the Features, Usage, or any section based on the actual functionality of your project. If your project includes specific files (like chat_analyzer.py or wordcloud_generator.py), be sure to mention them and provide usage instructions accordingly. Let me know if you need any further adjustments!
