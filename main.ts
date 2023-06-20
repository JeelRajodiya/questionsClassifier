// 0 - easy
// 1 - hard
// 2 - medium
// import tf from "@tensorflow/tfjs";
import fetch from "node-fetch";
async function run() {
	const questions = [
		"Which of the following is not a valid JavaScript variable name?",
		"Why so JavaScript and Java have similar name?",
	];
	const res = await fetch(
		"https://questionsclassifier.azurewebsites.net/predict",
		{
			method: "POST",
			body: JSON.stringify({questions}),
		}
	);
	const data = await res.json();
	console.log(data);
}

run();
