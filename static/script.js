// GEO-LOCATION API

navigator.geolocation.getCurrentPosition((position)=>{
	onSucess(position.coords.latitude,position.coords.longitude)
},(positionError)=>{
	onFailure(positionError.message)
})

function onSucess(lat,long){
	console.log(`Latitude is ${lat} and longitude is ${long}`);
}

function onFailure(message){
	console.log(message);
}