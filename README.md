# LYRICS GENERATOR WEB API 
# by Eric B., Jordan P., Audrey N.

Windows configuration


### 1. Install dependencies

<code>pip install requirements.txt</code>


### 2. Launch flask local server with Powershell

<code>$ env:FLASK_APP= "main"</code>

<code>$ flask run</code>



### 3. Consumming API

<code>GET http:127.0.0.1:5000/api</code>

1. Get lstm model prediciton

    <code>GET http:127.0.0.1:5000/lstm/<parameter></code>

2. Get transformer (BERT) model prediction 

    <code>GET http:127.0.0.1:5000/transformer/<parameter></code>

3. Query and response

Url <parameter> must be a string of 7 english words.

    **Query parameters :**

    | Type | Params | Values |
    |:-----|:-------|:-------|
    | GET | data | *< string >* |


    **Response :**

    | Status | Response |
    |:-----|:-------|
    | 200 | { "lstm_generated_text": *< string >* } |
    | 200 | { "transformer_generated_text": *< string >* } |
