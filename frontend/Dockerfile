FROM node:12

ENV PORT 3000

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Installing dependencies
COPY package*.json /usr/src/app/
RUN npm install

# Copying source files
COPY . /usr/src/app

# Building app
RUN npm run build
EXPOSE 3000

# USER nextjs
# Running the app
<<<<<<< HEAD
CMD "npm" "run" "start"

=======
CMD "npm" "run" "start"
>>>>>>> 82d10738b19dc75eaa5f5a03cdc8a65924b99513
