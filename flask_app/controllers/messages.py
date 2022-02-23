from flask import redirect,session,request
from flask_app import app
from flask_app.models.message import Message

@app.route('/post_message', methods=['POST'])
def post_message():
    if 'user_id' not in session:
        return redirect('/')
    if not Message.validate_message(request.form):
        return redirect('/dashboard')
    data = {
        "sender_id": request.form['sender_id'],
        "receiver_id": request.form['receiver_id'],
        "content": request.form['content']
    }
    Message.save_message(data)
    return redirect('/dashboard')

@app.route('/destroy/message/<int:id>')
def destroy_message(id):
    data = {
        "id": id
    }
    Message.destroy_message(data)
    return redirect('/dashboard')