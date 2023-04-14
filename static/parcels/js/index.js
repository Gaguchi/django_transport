import RideList from "./ride-list.js";

const rideList = new RideList();

function init() {
  const destination = window.destination;
  rideList.displayRides(destination);
}

init();
