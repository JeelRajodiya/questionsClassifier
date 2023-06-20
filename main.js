// 0 - easy
// 1 - hard
// 2 - medium
// import tf from "@tensorflow/tfjs";
import fetch from "node-fetch";
async function run() {
	const questions = [
		"what is the capital of india?",
		"what is the capital of china?",
	];

	const res = await fetch(
		"https://questionsclassifier.azurewebsites.net/predict",
		{
			method: "POST",
			headers: { "content-type": "application/json" },
			body: JSON.stringify(questions),
		}
	);
	const data = await res.json();
	console.log(data);
}

run();
