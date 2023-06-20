// 0 - easy
// 1 - hard
// 2 - medium
import tf from "@tensorflow/tfjs";

async function run() {
	const model = await tf.loadLayersModel("file://questionClassifyer_bert");
	model.summary();
}

run();
