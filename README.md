# DeepSeek Chat Interface

I have created an interface to use DeepSeek locally, which is downloaded via Ollama. Instead of using the terminal to chat with DeepSeek, you can use this web-based interface for a better experience.

  - ![Alt text](images.png)

## Features
- Simple and interactive UI using Streamlit
- Chat with DeepSeek AI without using the terminal
- Stores and displays chat history
- Supports formatted code responses

## Installation
1. Clone the repository:
   ```sh
   https://github.com/hassanalisyed021/deepseek-chat-interface.git
   cd deepseek-chat-interface
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Ensure you have **Ollama** installed and DeepSeek downloaded:
   ```sh
   ollama pull deepseek-r1:32b
   ```

## Usage
Run the Streamlit app:
```sh
streamlit run main.py
```
Now, you can interact with DeepSeek through the web interface instead of the terminal.

## License
This project is open-source. Feel free to modify and improve it!

