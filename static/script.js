// GEO-LOCATION API


navigator.geolocation.getCurrentPosition((position)=>{
	onSucess(position.coords.latitude,position.coords.longitude)
},(positionError)=>{
	onFailure(positionError.message)
})

function onSucess(lat,long){
	console.log(`Latitude is ${lat} and longitude is ${long}`);
	let status = 1
	$.post("/", {
		userStatus : status,
		coord : [lat,long]
	});
	console.log(`Status is ${status}`);
	
}

function onFailure(message){
	console.log(message);
	let status = 0
	console.log(`if onfailure is getting executed ${status} and count is ${count}`);
	$.post("/", {
		userStatus : status,
	});
	console.log(`Status is ${status}`);
}

