# 🤖 ChatAK: AI-Powered Chatbot

**ChatAK** is an AI-powered chatbot built from scratch, leveraging deep learning and neural networks for personalized responses. It uses `Python's PyTorch library` and is trained on custom datasets to predict user-specific replies.

## 🎥 Demo
[🧑‍💻 ChatAK Sample Demo](https://user-images.githubusercontent.com/68220732/152092372-37dcf4a9-9196-4780-b329-614a0063fd50.mp4)

## ⚙️ Initial Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/python-engineer/chatbot-deployment.git
   cd chatbot-deployment
   ```
2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```
3. **Install Dependencies**:
    ```bash
    pip install Flask torch torchvision nltk
    ```
4. **Download NLTK Package**:
    ```bash
    >>> import nltk
    >>> nltk.download('punkt')
    ```
5. **Customize Chatbot**:
    Edit `intents.json` to add your intents and responses.
6. **Train Model**:
    ```bash
    python train.py
    ```
7. **Test Locally**:
    ```bash
    python chat.py
    ```

## 🛠 Technologies Used
- **Python** with PyTorch
- **Flask** for backend
- **JavaScript** for frontend
- **Heroku** for deployment
- **nltk** for text processing

## 📂 Folder Structure
**train.py:** Training script for the chatbot model.<br>
**chat.py:** Console-based testing.<br>
**intents.json:** Stores intents and responses.<br>
**static/:** Frontend files.<br>
**templates/:** HTML templates for the web interface.<br>
**data.pth:** Trained model file.

---

**Happy Chatting!** 🎉 [Try it here](https://chatak.herokuapp.com/)