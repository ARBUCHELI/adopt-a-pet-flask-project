from flask import Flask
from helper import pets
app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <html style="background-color: #cfe0e8; margin-top: 1em;">
      <h1 style="color: #c94c4c; text-align: center; font-family: 'Courier New', monospace; font-size: 4em; font-weight: bold;">ADOPT A PET!</h1>
      <img style=" display: block; margin-left: auto; margin-right: auto; border-radius: 5px; border: 1px solid #c94c4c" src="https://raw.githubusercontent.com/ARBUCHELI/adopt-a-pet-flask-project/master/adopt_a_pet.jpg" alt="Adopt a Pet" width="200" height="200">
      <h2 style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em; margin-bottom: 3em;">A minimalistic Pet Adoption Flask Web App</h2>
      <p style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em;">Browse through the links below to find your new furry friend:</p>
      <ul style = "text-align: center; color: #034f84; font-family: 'Courier New', monospace; font-size: 1.5em; list-style: none;">
        <li style="color: #c94c4c"><a href="/animals/dogs">Dogs</a></li>
        <li style="color: #c94c4c"><a href="/animals/cats">Cats</a></li>
        <li style="color: #c94c4c"><a href="/animals/rabbits">Rabbits</a></li>
      </ul>
      <a style = "color: #36486b; font-family: 'Courier New', monospace; font-size: 1em; margin-bottom: 3em; position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; font-weight: bold;" href="https://www.freepik.com/free-vector/adopt-pet-concept_8466085.htm#page=2&query=pet%20adoption&position=6&from_view=search&track=ais" target="_blank">Image by pikisuperstar on Freepik</a>
      <footer style = "color: #c94c4c; font-family: 'Courier New', monospace; font-size: 1.5em; margin-bottom: 3em; position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; font-weight: bold;">Bucheli © Web Development 2023</footer>
    </html>
    '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<html style="background-color: #cfe0e8; margin-top: 1em;">'
  html += f'<h1 style="color: #c94c4c; text-align: center; font-family: Courier New, monospace; font-size: 4em; font-weight: bold">List of {pet_type}</h1>'
  html += f'<img style=" display: block; margin-left: auto; margin-right: auto; border-radius: 5px; border: 1px solid #c94c4c" src="https://raw.githubusercontent.com/ARBUCHELI/adopt-a-pet-flask-project/master/animals.jpg" alt="Animals" width="200" height="200">'
  html += f'<h2 style = "text-align: center; color: #034f84; font-family: Courier New, monospace; font-size: 1.5em; margin-bottom: 3em;">Here you can choose a puppy for adoption!</h2>'
  html += '<ul style = "text-align: center; color: #034f84; font-family: Courier New, monospace; font-size: 1.5em; list-style: none;">'
  for idx, item in enumerate(pets[pet_type]):
    html += f'<li style="color: #c94c4c"><a href="/animals/{pet_type}/{idx}">' + item["name"] +'</a></li>'
  html += '</ul>'
  html += f'<a style = "color: #36486b; font-family: Courier New, monospace; font-size: 1em; margin-bottom: 3em; position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; font-weight: bold;"href="https://www.freepik.com/free-vector/cute-dog-playing-box-cartoon-illustration-animal-nature-concept-isolated-flat-cartoon_11189732.htm#query=puppy&position=7&from_view=search&track=sph#position=7&query=puppy?verify-email=success" target="_blank">Image by catalyststuff on Freepik</a>'
  html += f'<footer style = "color: #c94c4c; font-family: Courier New, monospace; font-size: 1.5em; margin-bottom: 3em; position: fixed; left: 0; bottom: 0; width: 100%; text-align: center; font-weight: bold;">Bucheli © Web Development 2023</footer>'
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