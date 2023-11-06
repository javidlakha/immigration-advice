# karibu

> DO NOT USE IN PRODUCTION WITHOUT THE SUPERVISION OF A QUALIFIED LAWYER

Karibu is a phone-based legal assistant that can take incoming
calls and understands and speaks many languages. It is connected to a database
of legal advice.

Karibu is implemented using Twilio, Anthropic Claude, MongoDB Atlas
Vector Search, Whisper and GCP's text-to-speech.

Karibu can understand

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

You will need a [Twilio](https://www.twilio.com/) phone number.

First, install

* [AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html)
* [Docker](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

Then populate `.env`. Make sure that `WEBHOOK_DOMAIN` corresponds to the
webhook URLs in the Twilio console.

Finally, run

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

To connect Twilio to the development server, use [ngrok](https://ngrok.com/).

```
source .env && ngrok http --domain=$WEBHOOK_DOMAIN 8000
```

where `WEBHOOK_DOMAIN` is obtained from ngrok and set in the Twilio console.
