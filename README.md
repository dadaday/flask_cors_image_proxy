# flask_cors_image_proxy
Proxy for getting images from CORS secured sites


# To run using docker you should run following commands

```commandline
docker build --tag flask_cors .  
```

```commandline
docker run -d -p 5000:5000 flask_cors:latest
```

# Environment variables

| Name        | Required | Description | Example |
| ----------- | ----------- |----------- |----------- |
| PROXIES     | No       | List of proxies, separated by commas | "https://8.8.8.8:8888,https://username:password@1.1.1.1:2222" |