# Teckium front


## Requirements 
- Python 3.5 or more
- virtualenv
- gulp-cli
- npm
```
pip install virtualenv
```

## Quick Start
First clone the repository: 

```
>>  git clone https://github.com/JoseAntpr/tradingApp.git
>>  cd tradingApp 
```

You need virtualenv installed to work in a virtual enviroment:
```
# Create virtual enviroment 
>> virtualenv -p python3 <nameVirtualEnv>
# Activate virtual enviroment
>> source <nameVirtualEnv>/bin/activate
```

Optional commands for virtualenv:
```
# Disable Python virtual enviroment
>> deactivate
# Add a requirement to the virtualenv requirements
>> pip freeze > requirements.txt
```

Install all packages for npm
```
npm install
```

## Development server
Run `python manage.py runserver` for a dev back-end server.
Run  `gulp` for a dev proxy front-end server. Navigate to `http://localhost:3000/`.