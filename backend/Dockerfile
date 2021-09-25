# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /src

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
<<<<<<< HEAD
# RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
=======
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
>>>>>>> 82d10738b19dc75eaa5f5a03cdc8a65924b99513
RUN pip install -r requirements.txt

# EXPOSE 8000

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]