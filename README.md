# ChatAK (AI powered chatbot built from scratch for personalized responses)

#### In this project, I have hard-coded ChatAK, an AI powered chatbot that uses `deep learning and neural networks based Machine learning algorithms.` This chatbot predicts the responses using `Python's Pytorch library.` I have used personalized datasets to train it.

#### I have deployed this chatbot using Flask and JavaScript in Heroku: [See deployed app here.](https://chatak.herokuapp.com/)

https://user-images.githubusercontent.com/68220732/152092372-37dcf4a9-9196-4780-b329-614a0063fd50.mp4

## Initial setup for running the app in your computer:

`This repo currently contains the final files.`

Clone repo and create a virtual environment. Below is the procedure for Windows users.

```
$ git clone https://github.com/python-engineer/chatbot-deployment.git
$ cd chatbot-deployment
$ python -m venv venv
$ source venv/Scripts/activate
```

Install dependencies

```
$ (venv) pip install Flask torch torchvision nltk
```

Install nltk package

```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```

Modify `intents.json` with different intents and responses for your Chatbot

Run

```
$ (venv) python train.py
```

This will dump data.pth file. And then run
the following command to test it in the console.

```
$ (venv) python chat.py
```

For deployment, publish the root directory (chatbot-deployment) to [GitHub](https://github.com/) as a new repository. After this, create a web-app in [Heroku](https://id.heroku.com/login) and link the published repository to the web-app. Learn more about deployment in Heroku [here.](https://www.youtube.com/watch?v=6plVs_ytIH8&t=1249s)
