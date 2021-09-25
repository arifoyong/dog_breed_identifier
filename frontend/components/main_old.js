import fetch from "isomorphic-unfetch";
import { useState } from "react";

import { API } from "../config";

const Main = ({ children }) => {
  const [state, setState] = useState({
    top10: [],
    isLoading: false,
    initial: true,
  });
  // const [isLoading, setIsLoading] = useState(false);
  const [imgFile, setImgFile] = useState(null);

  const onUpload = async (e) => {
    if (e.target.files) {
      const top10 = [];
      const isLoading = true;

      setState({ top10, isLoading });
      setImgFile(URL.createObjectURL(e.target.files[0]));

      const formData = new FormData();
      await formData.append("file", e.target.files[0]);
      await formData.append("filename", "test");

      const res = await fetch(`${API}uploadfile`, {
        method: "POST",
        headers: {
          Accept: "application/json",
        },
        body: formData,
      });

      const data = await res.json();
      console.log(data);
      setState({ ...state, top10: data.top10, isLoading: false });
    }
  };

  const formatPrediction = (pred) => {
    let splitStr = pred.split("_");
    let capitalizeWords = [];

    splitStr.forEach((element) => {
      capitalizeWords.push(
        element[0].toUpperCase() + element.slice(1, element.Length)
      );
    });

    return capitalizeWords.join(" ");
  };

  const formatProbability = (prob) => {
    let num = prob * 100;
    let displayNum = " (" + num.toFixed(2).toString() + "%)";
    return displayNum;
  };

  const showResult = () => {
    const top3 = state.top10.slice(0, 3);

    return top3.map((item, i) => {
      const dogName = Object.keys(item)[0];
      const probability = item[dogName];

      return (
        <p key={i} className="text-lg font-normal text-gray-600">
          <span>{formatPrediction(dogName)}</span>
          <span>{formatProbability(probability)}</span>
        </p>
      );
    });
  };

  const resultCard = () => (
    <React.Fragment>
      <h4 className="text-xl font-bold text-gray-800 uppercase">
        Top 3 predictions
      </h4>
      {showResult()}
      <div className="flex py-2 overflow-hidden">
        <img className="object-contain h-auto" src={imgFile} />
      </div>
    </React.Fragment>
  );

  const introCard = () => (
    <div className="flex-1 px-2 py-2 mt-4 rounded-lg border-gray-400 border-2 bg-gray-200 w-11/12 ">
      <div className="py-6 px-8 text-gray-600">
        <h4 className="text-xl font-bold md:text-4xl">
          Dog Breed Identification
        </h4>
        <p className="mt-4 md:text-2xl font-semibold text-gray-500">
          Machine learning based model to predict dog breed. The model was
          trained with{" "}
          <a
            className="text-blue-500 hover:text-blue-800"
            href="https://www.kaggle.com/c/dog-breed-identification"
          >
            kaggle dataset
          </a>
          .
        </p>
      </div>
    </div>
  );

  return (
    <React.Fragment>
      <div className="flex flex-col viewport100 sm:h-screen">
        <div className="bg-gray-100 flex-1 flex flex-col items-center justify-start overflow-y-auto pt-2">
          {state.top10.length > 0 ? resultCard() : introCard()}
        </div>
        <div className="bg-gray-100 flex items-center py-4 justify-center">
          <label className="bg-gray-800 hover:bg-gray-600 text-white rounded-full px-8 py-2 md:text-2xl">
            Get Image
            <input onChange={onUpload} type="file" accept="image/*" hidden />
          </label>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Main;
