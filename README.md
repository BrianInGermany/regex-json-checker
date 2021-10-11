# Regex-JSON-Checker

- This is a flask app for testing regexes that can be uploaded to heroku, and is also available under:
[regex-json-checker.herokuapp.com](https://regex-json-checker.herokuapp.com)
- To execute locally, install flask (`pip install flask`) and run `python app.py`. It will open on [127.0.0.1:5000](http://127.0.0.1:5000/).

## The following syntax must be observed for the JSON:
- Remember to double-backslash all escapes
```json
[
   {
      "name": "DOMAIN__DINOSAURS",
      "pattern": [
         "(?=.*rex.*).*\\bTyrannosaurus\\b.*",
         ".*(?:saurus|sauri).*",
         ".*dactyl.*"
      ]
   },
   {
      "name": "DOMAIN__COWBOYS",
      "pattern": [
         "(?=.*\\bguns?\\b.*).*west.*",
         ".*yü.*(?:haw)?",
         ".*ride.*"
      ]
   }
]
```
## Test strings can be entered with a new string per each line:

```txt
I like Velociraptors
Stegosauruses have spikey tails
Archaeopteryx is kinda like a Pterodactyl maybe
Pterodactyls were poetic creatures. 
But only their feet (because of the "dactyl").
Brachiosauri have long necks
Tyrannosaurus (rex) is the king of the dinos
The Wako Kid was the fastest gun in the west.
Gunslingers abounded in the wild west.
Cowboys like lassos and guns
Do you think a cowboy ever herded Stegosauruses?
Or ride a Tyrannosaurus Rex?
Dü yü like ümlautß?
```