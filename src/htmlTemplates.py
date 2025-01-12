css = """
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}

.e1obcldf1{
    background-color: blue;
    border-color: white;
}
.e1obcldf1:hover{
    background-color: white;
    border-color: white;
    color: blue;
}
# .stTextInput  {
#     position: fixed;
#     bottom: 0;
# }
.st-key-reset_button{
    position: fixed;
    bottom: 0;
    margin-bottom: 12px;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.stImage {
    max-width: 200px;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
"""

bot_template = """
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-photo/woman-with-blue-eyes-silver-robot-face_14865-1654.jpg?w=740" style="max-height: 78px; width: 100px; border-radius: 50%; object-fit: fill;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
"""

user_template = """
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/free-vector/user-circles-set_78370-4704.jpg?t=st=1715349716~exp=1715353316~hmac=1cfaada9b4f950badd141ee8db93d34691faeac8c4721d0cd331a9b8a4ee3f29&w=740" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: fill;">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
"""
