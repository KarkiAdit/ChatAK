# ChatAK (AI powered chatbot built from scratch for personalized responses)

In this project, I have hard-coded ChatAK, `an AI powered chatbot that uses deep learning and neural networks based Machine learning algorithms.` This chatbot predicts the responses using `Python's Pytorch library.` I have used `personalized datasets` to train it.

I have deployed this chatbot using Flask and JavaScript in Heroku: [See the Deployment here](https://chatak.herokuapp.com/)

This gives 2 deployment options:

- Deploy within Flask app with jinja2 template
- Serve only the Flask prediction API. The used html and javascript files can be included in any Frontend application (with only a slight modification) and can run completely separate from the Flask App then.

## Initial setup for running the app in your computer:

This repo currently contains the final files.

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

Now for deployment upload the root directory (chatbot-deployment) to [GitHub](https://github.com/) and [Heroku](https://id.heroku.com/login). After this, publish your root directory in GitHub as a repository, create a web-app in Heroku and link the published repository to the web-app. Learn more about deployment in Heroku[here](https://www.youtube.com/watch?v=6plVs_ytIH8&t=1249s)
