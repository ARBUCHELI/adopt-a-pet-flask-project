from flask import Flask
from helper import pets
app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <html style="background-color: #cfe0e8; margin-top: 1em;">
      <h1 style="color: #c94c4c; text-align: center; font-family: 'Courier New', monospace; font-size: 4em; font-weight: bold;">ADOPT A PET!</h1>
      <img style=" display: block; margin-left: auto; margin-right: auto; border-radius: 5px; border: 1px solid #c94c4c" src="https://raw.githubusercontent.com/ARBUCHELI/adopt-a-pet-flask-project/master/adopt-pet-concept_23-2148517279.avif" alt="Girl in a jacket" width="200" height="200">
      <h2 style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em; margin-bottom: 3em;">A minimalistic Flask Web App with information about Pets</h2>
      <p style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em;">Browse through the links below to find your new furry friend:</p>
      <ul style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em; list-style: none;">
        <li style="color: #c94c4c"><a href="/animals/dogs">Dogs</a></li>
        <li style="color: #c94c4c"><a href="/animals/cats">Cats</a></li>
        <li style="color: #c94c4c"><a href="/animals/rabbits">Rabbits</a></li>
      </ul>
    </html>
    '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<html style="background-color: #cfe0e8; margin-top: 1em;">'
  html += f'<h1 style="color: #c94c4c; text-align: center; font-family: Courier New, monospace; font-size: 4em; font-weight: bold">List of {pet_type}</h1>'
  html += '<ul>'
  for idx, item in enumerate(pets[pet_type]):
    html += f'<li><a href="/animals/{pet_type}/{idx}">' + item["name"] +'</a></li>'
  html += '</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return f'''
  <h1>{pet["name"]}</h1>
  <img src="{pet["url"]}"/>
  <p>{pet["description"]}</p>
  <ul>
    <li>{pet["breed"]}</li>
    <li>{pet["age"]}</li>
  </ul>
  '''