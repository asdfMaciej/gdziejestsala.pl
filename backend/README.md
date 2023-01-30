# Backend

TODO - readme. See the root README for more details.

Use ```pigar generate``` to update the requirements.txt after installing a new package.
Auto-format the code using Black.
Make sure the tests pass by running pytest.

### Useful Docker commands

Those come in handy when debugging the Dockerfile.
```bash
docker build -t backend-img .

docker run \
-p 80:80 \
-e DATABASE_URL=postgresql://usos_user:usos_password@host.docker.internal/usos_db \
-e ADMIN_USERNAME=rzodkiewkaczerwona \
-e ADMIN_PASSWORD=twarozekbialy2008 \
-e ADMIN_EMAIL=admin@example.com -it backend-img 
```
