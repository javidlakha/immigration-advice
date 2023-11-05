# immigration-advice

> DO NOT USE IN PRODUCTION WITHOUT THE SUPERVISION OF A QUALIFIED LAWYER

Immigration Advice is a phone-based legal assistant that can take incoming
calls and understands and speaks many languages. It is connected to a database
of legal advice.

Immigration Advice is implemented using Twilio, Anthropic Claude, MongoDB Atlas
Vector Search, Whisper and GCP's text-to-speech.

Immigration Advice can understand

```
Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian,
Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish,
French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic,
Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian,
Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish,
Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili,
Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh
```

and can speak

```
Afrikaans, Arabic, Bulgarian, Catalan, Chinese, Czech, Danish, Dutch, English,
Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic
Indonesian, Italian, Japanese, Korean, Latvian, Lithuanian, Malay, Marathi,
Norwegian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Spanish,
Swedish, Tamil, Thai, Turkish, Ukrainian, Vietnamese, Welsh
```

in a native voice.

## Installation

First, install

* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

and then run

```bash
yarn install
```

## Local development

To launch the development server, ensure Docker is running and then run

```bash
yarn dev
```

The development server will be running in a container that can be accessed at
[http://localhost:8000/](http://localhost:8000/). It supports hot reloading:
changes made to the `api` directory will automatically be applied.


```
source .env && ngrok http --domain=$NGROK_DOMAIN 8000
```
