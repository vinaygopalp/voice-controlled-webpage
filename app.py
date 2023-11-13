from flask import Flask, render_template, url_for, redirect, request, flash
# import requests
# import os
# import time
# import serial
# import webbrowser

# ser = serial.Serial(
  
#    port='/dev/ttyS0',  #ttyAMA0 ttyS0
#    baudrate = 9600,
#    parity=serial.PARITY_NONE,
#    stopbits=serial.STOPBITS_ONE,
#    bytesize=serial.EIGHTBITS,
#    timeout=1
# )

# ser.flushInput()

# TOKEN = "5337327052:AAGC95ZKe574gqpiJ49vV-BpzEAi2q-vuLg"
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates?offset=-1"
# ##r = sr.Recognizer()

app = Flask(__name__, static_folder='static')
    
@app.route('/')
def index():
    return render_template('index.html', message='WELCOME')

# @app.route('/demo')
# def demo():
#     a=0
#     d='WELCOME'
#     while(1):
#         try:
#             message = requests.get(url).json()
#             Text = message['result'][0]['message']['text']
#             if not os.path.exists('msg.txt'):
#                 f = open('msg.txt', 'w')
#                 f.write(Text)
#                 f.close()
                
#             f = open('msg.txt', 'r')
#             d=f.read()
#             f.close()
            
#             if d != Text:
#                 f = open('msg.txt', 'w')
#                 f.write(Text)
#                 f.close()
#                 a=1
#                 break
#         except:
#             pass
#         try:
#             print('speak')
#             MyText=ser.readline()
#             print(MyText)
#             MyText = MyText.decode('UTF-8')
#             MyText = MyText.lower()
#             if len(MyText.strip()) > 0:
#                 print(MyText)
#                 break
#         except:
#             pass

#     if a==1:
#         print('telegram')
#         print(Text)
#         return render_template('index.html', message=Text)
#     else:
#         print('voice assistant')
#         File=''
#         rows=[]
#         Sem = None
#         if '1st sem' in MyText or 'first sem' in MyText:
#             Sem = '1st'
#         if '2nd sem' in MyText or 'second sem' in MyText:
#             Sem = '2nd'
#         if '3rd sem' in MyText or 'third sem' in MyText:
#             Sem = '3rd'
#         if '4th sem' in MyText or 'fourth sem' in MyText:
#             Sem = '4th'
#         if '5th sem' in MyText or 'fifth sem' in MyText:
#             Sem = '5th'
#         if '6th sem' in MyText or 'sixth sem' in MyText:
#             Sem = '6th'
#         if '7th sem' in MyText or 'seventh sem' in MyText:
#             Sem = '7th'
#         if '8th sem' in MyText or 'eighth sem' in MyText:
#             Sem = '8th'

#         print('{} sem selected'.format(Sem))
#         if not(Sem is None):
#             if 'advertisment' in MyText or 'advertisement' in MyText:
#                 path = 'static/'+Sem+'/advertisment'
#                 video = []
#                 for i in os.listdir(path):
#                     video.append('http://127.0.0.1:5000/'+path+'/'+i)
#                 print(video)
#                 #for i in os.listdir(path)[:1]:  
#                 #    webbrowser.open(path+'/'+i)
#                 return render_template('index.html', anchor="video", videos=video, message=d)
            
#             if 'internal' in MyText:
#                 path = 'static/'+Sem+'/internal_time_table'
#                 images = []
#                 for i in os.listdir(path):
#                     images.append('http://127.0.0.1:5000/static/'+Sem+'/internal_time_table/'+i)
#                 print(images)
#                 return render_template('index.html', anchor="image", images=images, message=d)

#             if 'calender' in MyText or 'calendar' in MyText:
#                 path = 'static/'+Sem+'/calender'
#                 docs = []
#                 for i in os.listdir(path):
#                     docs.append('http://127.0.0.1:5000/static/'+Sem+'/calender/'+i)
#                 print(docs)
#                 return render_template('index.html', anchor="doc", docs=docs, message=d)
            
#             if 'class' in MyText:
#                 path = 'static/'+Sem+'/class_time_table'
#                 images = []
#                 for i in os.listdir(path):
#                     images.append('http://127.0.0.1:5000/static/'+Sem+'/class_time_table/'+i)
#                 return render_template('index.html', anchor="image", images=images, message=d)

#             if 'vtu' in MyText:
#                 path = 'static/'+Sem+'/vtu_time_table'
#                 images = []
#                 for i in os.listdir(path):
#                     images.append('http://127.0.0.1:5000/static/'+Sem+'/vtu_time_table/'+i)
#                 print(images)
#                 return render_template('index.html', anchor="image", images=images, message=d)
            
#             if 'subject' in MyText:
#                 path = 'static/'+Sem+'/subject'
#                 docs = []
#                 for i in os.listdir(path):
#                     docs.append('http://127.0.0.1:5000/static/'+Sem+'/subject/'+i)
#                 print(docs)
#                 return render_template('index.html', anchor="doc", docs=docs, message=d)

#             if 'student' in MyText:
#                 path = 'static/'+Sem+'/student_list'
#                 docs = []
#                 for i in os.listdir(path):
#                     docs.append('http://127.0.0.1:5000/static/'+Sem+'/student_list/'+i)
#                 print(docs)
#                 return render_template('index.html', anchor="doc", docs=docs, message=d)
            
#             if 'result' in MyText:
#                 path = 'static/'+Sem+'/results'
#                 docs = []
#                 for i in os.listdir(path):
#                     docs.append('http://127.0.0.1:5000/static/'+Sem+'/results/'+i)
#                 print(docs)
#                 return render_template('index.html', anchor="doc", docs=docs, message=d)
                
#             if 'general' in MyText:
#                 path = 'static/'+Sem+'/general_circuler'
#                 docs = []
#                 for i in os.listdir(path):
#                     docs.append('http://127.0.0.1:5000/static/'+Sem+'/general_circuler/'+i)
#                 print(docs)
#                 return render_template('index.html', anchor="doc", docs=docs, message=d)
#             else:
#                 return render_template('index.html', message=d)
        
#         else:
#             return render_template('index.html', message=d)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
