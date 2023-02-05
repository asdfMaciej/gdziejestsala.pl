# gdziejestsala.pl

[![Backend tests](https://github.com/USOS-WEB/backend/actions/workflows/test-backend.yml/badge.svg)](https://github.com/USOS-WEB/backend/actions/workflows/test-backend.yml)
[![Fly.io deploy](https://github.com/asdfMaciej/gdziejestsala.pl/actions/workflows/fly.yml/badge.svg)](https://github.com/asdfMaciej/gdziejestsala.pl/actions/workflows/fly.yml)

## About the project

[gdziejestsala.pl](https://gdziejestsala.pl) is an in-door navigation system designed for college campuses. The project is under active development.

The idea stems from the AKAI Code 2022 hackathon. Along with my team we've created [a working prototype](https://github.com/orgs/USOS-WEB/repositories) of navigation for the Poznań University of Technology.    

## Developer guide

The project warmly accepts outside contributions :)

### Running the project

Docker is required. Run the following commands in the project root:

```bash
cp .env.example .env
docker-compose up -d
```  

Frontend should be available under localhost:8000, backend should be available under localhost:80.
The admin panel should be accessible at /api/v1/admin under the default .env credentials.
You can view the API docs under /api/v1/docs and /api/v1/redoc

### Local development

Modified files will be auto-reloaded when working on frontend or backend.

See respective backend and frontend directories' README for more detailed instructions.

#### WSL2 and VS Code setup

Install npm and Python 3.10 on the host machine.
Run ```npm ci``` in the frontend directory - installed node-modules will enable linting in VS Code and remove Typescript errors.

Run ```pip install requirements-dev.txt``` in the backend directory - it will install black (a code formatter), pigar (a tool for generating requirements.txt), and pre-commit (a tool for pre-commit hooks). 

Install required extensions in VS Code (Python, Vue, Typescript, ...).

After installing the Python extension, enter Settings, set Black as the "python formatting provider", and enable "format on save".

Configure [Takeover Mode](https://vuejs.org/guide/typescript/overview.html#ide-support) in Volar for frontend editing.

Lastly, run ```pre-commit install``` in the root directory to install pre-commit hooks. 

Note: this setup isn't ideal, as it relies on the host machine. It could utilize dev containers VS Code functionality. 

#### Building the frontend

First, set the env variable VITE_BACKEND_URL to an empty string, as after build frontend will run under the same URL as backend. 
Next, launch the frontend container and run:
```bash
su node
npm run build
```

Frontend builds to the backend dist directory (per vite.config.ts file).
Upon build, the website should be available under the localhost:80 backend URL.

### Deploying on fly.io

The project should work out of the box on fly.io. 

Start with building the frontend using the previously mentioned steps.

Setup an fly.io app (name used: gdziejestsala), a volume (gdziejestsala_volume) and a postgres database.

Please note that the Postgres database URL starts with "postgres" while "postgresql" prefix is needed. 

Deploy the project from the backend directory, using the following commands:

```bash
flyctl secrets set \
  ADMIN_USERNAME=CHANGEME  \
  ADMIN_PASSWORD=CHANGEME  \
  ADMIN_EMAIL=CHANGEME     \
  DATABASE_URL=postgresql:// --stage

flyctl deploy 
```

If you want to hook the project to a custom domain, you should generate a certificate using flyctl.

### Style guide 
Commits should be in present-tense, imperative style.

