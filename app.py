from codecs import encode
from flask import Flask, render_template, request
import re
import json

from werkzeug.datastructures import FileStorage
app = Flask(__name__)  
app.secret_key = 'development key'  
 
@app.route('/', methods = ['GET','POST'])  
def send_patterns():  
   return render_template('form_textarea.html')  
 
 
 
@app.route('/results',methods = ['GET','POST'])  
def check_matches(): 
   # form = request.get_json() 
   
   # breakpoint()
   # regexes = request.files["regex_file"]
   
   # strings = request.files["string_file"]
   # breakpoint()
   # with open(regexes, "r", encoding="utf-8") as regexes:
   #    with open(strings,"r", encoding="utf-8") as strings:
   regexes = request.form["regex_patterns"]
   strings = request.form["strings"]
   try:
      regex_json = json.loads(regexes)
   except:
      return "Please ensure json is valid and retry."
   results = {}
   for utt_string in strings.split("\n"):
   # for utt_string in strings.split("\n"):
      # utt_string = utt_string.decode('UTF-8')
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
            try: 
               if re.fullmatch(adapted_pattern, utt_string):
                  
                  if utt_string not in results.keys(): 
                     results[utt_string] = []
                     results[utt_string].append(["\"" + pattern + "\""])
                     results[utt_string].append(pattern_object["intent"])
                  else:
                     if len(results[utt_string]) > 1:
                        if results[utt_string][1] == "":
                           results[utt_string][1] = pattern_object["intent"]
                     results[utt_string][0].append("\"" + pattern + "\"")
                     
               else:
                  if utt_string not in results.keys():
                     results[utt_string] = []
                     results[utt_string].append([])
                     results[utt_string].append("")
                  else:
                     pass
            except:
               return f"Regex pattern {pattern} has an error. Fix and retry."
   def takeSecondLen(elem):
      return len(elem[1][0])
   result_list = []
   for key, val in results.items():
      result_list.append([key, val])
   result_list.sort(key=takeSecondLen)

   
      
               
            

   return render_template("results.html", patterns = result_list)  

if __name__ == '__main__':  
   app.run(debug = True)  