# Backend

## How to run the Dockerfile

### 1. Build
```bash
# working directory: backend/.
docker build -t myimage .
```

### 2. Run
Either like this: 

```bash
docker run -d --name mycontainer -p 80:80 myimage
```

Or like this for live reload:

```bash
docker run -d -p 80:80 -v $(pwd):/app myimage /start-reload.sh
```
