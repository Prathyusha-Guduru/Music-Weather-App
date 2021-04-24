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
		lat : lat,
		long : long
	});
	console.log(`Status is ${status}`);
	
}

function onFailure(message){
	console.log(message);
	let failed = 0
	console.log(`if onfailure is getting executed ${failed} and `);
	$.post("/", {
		userStatus : failed,
		lat : 0,
		long : 0
	});
	console.log(`Status is ${failed}`);
}

