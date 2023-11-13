<div align="center">
<h1>VVCE Certificate Verifications</h1>
</div>
  
------------------------

<div align="center">
  <a><img src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/MongoDB_Atlas-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white"></a> &nbsp;
  <a><img src="https://img.shields.io/badge/azure-%230072C6.svg?style=for-the-badge&logo=microsoftazure&logoColor=white"></a> &nbsp;
</div>

------------------------

This Repository Contains the Code for a website built for Vidyavardhaka College of Engineering that verifies the Certificates Received as the part of the Institution by Validating the Certificate Reference ID. Its a Dynamic website Buits using HTML, CSS, Java Script, Python( Flask ) and Hosted using Azure web Services. Its data is Maintained in Mongo DB.

------------------------

## Requirments
Python 3.11.1 (Recommended) 

<a href="https://www.python.org/downloads/" alt="3.11.1">
        <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
  
<h4>Modules Required</h4>

- flask
- pymongo
- configparser

--------------------------
## How to Run?

- Intialize a Git Repository.
```bash
  git init
```

- Clone the Current Git Repository.
```bash
  git clone https://github.com/k-arthik-r/VVCE-Certificate-Verificaion-Site.git
```

- Crete a Virtual Environment named env and Activate it(PowerShell)
```bash
  python -m venv env

  .\env\Scripts\Activate.ps1
```

- Install all the Modules Present in [requirements](requirements.txt)
```bash
  pip install -r requirements.txt
```

- Give The Appropriate Mongo DB Credentials in [config](config.ini)

- After Importing all the mentioned modules, Run [app](app.py)
  
```bash
  python app.py
```
-------------------------

## How the Website?

The Webpage takes Reference ID (It is Printed on the Certificate) as Input form the User and Validates the ID. If the ID is Valid it will display the Name and Contribution of the User Along with the Event Name.
If the ID is Invalid, it will Display an Error Message stating ID is Invalid.

![Image](https://github.com/k-arthik-r/VVCE-Certificate-Verificaion-Site/assets/111432615/cee30172-9be6-4d0f-b35b-6cf09fa4980e)

----------------------------

## License

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

----------------------------

## Feedback
If you have any feedback, please reach out to us at voidex.developer@gmail.com .
You are also welcomed to add new features by creating Pull Requests.



