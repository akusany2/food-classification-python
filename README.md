# Getting started
- Extract the code inside a directory or download from https://github.com/akusany2/food-classification-python
- Create an environment using – python -m venv ./env
- Go inside the project directory and download the trained model (model_v1_inceptionV3) from S3 using the link https://cmlproject.s3.amazonaws.com/model_v1_inceptionV3.h5
- The backend is power by Python’s FastAPI, so to run the project on the local environment directly use the command - uvicorn main:app  --reload --host 0.0.0.0 --port 8000, this will run the API on port 8000.
- To run the project through docker simply create an image -  docker build -t cml . and instantiate the container - docker run -d --name cont -p 8000:8000 cml
