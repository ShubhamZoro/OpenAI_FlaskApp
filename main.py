from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = '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'
chat_history=[]
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'POST':
        condition = request.form['condition']
        severity = request.form['severity']
        user_message = request.form['message']
        message=f'Condition: {condition}\nSeverity: {severity}\nUser: {user_message}\n'

        # Send the condition and severity to the ChatGPT API
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
         messages=[
        {"role": "assistant", "content":message},

    ]
    )
        if response['choices'][0]['message']!=None:
            chatbot_response = response['choices'][0]['message']
        else:
            chatbot_response="no response"
        chat_history.append({'sender':f'Condition: {condition}\nSeverity: {severity}\nUser: {user_message}\n', 'message': chatbot_response})
        chat_history.reverse()
        print(chat_history)

        return render_template('index.html', chat_history=chat_history)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
