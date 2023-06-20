// 0 - easy
// 1 - hard
// 2 - medium
// import tf from "@tensorflow/tfjs";
import fetch from "node-fetch";
async function run() {
	const questions = {
		questions: [
			"what is the capital of india",
			"what is the capital of china",
		],
	};
	// console.log(JSON.stringify(questions));
	const res = await fetch(
		"https://questionsclassifier.azurewebsites.net/predict",
		{
			method: "POST",
			body: JSON.stringify(questions),
		}
	);
	const data = await res.json();
	console.log(data);
}

run();
