require("dotenv").config();

const API = process.env.API || "http://localhost:8000/";

module.exports = {
  // publicRuntimeConfig: {
  //   APP_NAME: "Dog Breed Identifier",
  //   API_DEVELOPMENT: "http://localhost:8000/",
  //   API_PRODUCTION: "http://159.65.5.51:8000/",
  //   PRODUCTION: true,
  //   DOMAIN_DEVELOPMENT: "http://localhost:3001",
  //   DOMAIN_PRODUCTION: "http://dogbreed.oyong.tk",
  //   API: API,
  // },
  publicRuntimeConfig: {
    API: API,
  },
};
