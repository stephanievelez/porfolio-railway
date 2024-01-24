# learning_log
 portfolio


## Run with Nixpacks

Build and package

```bash
nixpacks build . --name portfolio-railway
```

Run with docker

```bash
docker run -e PORT=8080 -p 8080:8080 portfolio-railway
```

Open in browser: [http://localhost:8080](http://localhost:8080)