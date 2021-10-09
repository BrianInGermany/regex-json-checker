from codecs import encode
from flask import Flask, render_template, request
import re
import json

from werkzeug.datastructures import FileStorage
app = Flask(__name__)  
app.secret_key = 'development key'  
 
@app.route('/', methods = ['GET','POST'])  
def send_patterns():  
   return render_template('form_regex.html')  
 
 
 
@app.route('/results',methods = ['GET','POST'])  
def check_matches(): 
   # form = request.get_json() 
   
   # breakpoint()
   regexes = request.files["regex_file"]
   
   strings = request.files["string_file"]
   # breakpoint()
   # with open(regexes, "r", encoding="utf-8") as regexes:
   #    with open(strings,"r", encoding="utf-8") as strings:
   
   regex_json = json.load(regexes, encoding="utf-8")
   results = {}
   for utt_string in strings.readlines():
   # for utt_string in strings.split("\n"):
      utt_string = utt_string.decode('UTF-8')
      utt_string = utt_string.strip()
      utt_string = utt_string.lower()
      
      if utt_string == "":
         continue
      for pattern_object in regex_json:
   
         for pattern in pattern_object["pattern"]:
            # pattern = pattern.decode('UTF-8')pattern
            # breakpoint()
            adapted_pattern = pattern.lower()
            try: 
               adapted_pattern = adapted_pattern.replace("\\\\", "\\")
            except:
               pass
            adapted_pattern = "^" + adapted_pattern + "$"
            
            if re.fullmatch(adapted_pattern, utt_string):
               if utt_string in results.keys():
                  results[utt_string].append("\"" + pattern + "\"")
               else: 
                  results[utt_string] = ["\"" + pattern + "\""]
               
            else:
               if utt_string not in results.keys():
                  results[utt_string] = []
   def takeSecond(elem):
      return elem[1]
   result_list = []
   for key, val in results.items():
      result_list.append([key, val])
   result_list.sort(key=takeSecond)

   
      
               
            

   return render_template("results.html", patterns = result_list)  

if __name__ == '__main__':  
   app.run(debug = True)  