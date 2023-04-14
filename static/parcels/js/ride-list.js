export default class RideList {
  constructor() {}

  filterRides(destination, rides) {
    if (!destination) {
      return rides;
    }
    return rides.filter(function (ride) {
      return ride.destination === destination;
    });
  }

  displayRides(destination) {
    fetch(`/api/rides?destination=${destination}`)
      .then((response) => response.json())
      .then((data) => {
        let rides = this.filterRides(destination, data.rides);
        let rideList = document.getElementById("ride-list");
        rideList.innerHTML = "";
        if (rides.length === 0) {
          let p = document.createElement("p");
          p.textContent = "No rides available.";
          rideList.appendChild(p);
        } else {
          for (let ride of rides) {
            let div = document.createElement("div");
            div.classList.add("ride");
            let name = document.createElement("h2");
            name.textContent = ride.name;
            div.appendChild(name);
            let startDate = document.createElement("p");
            startDate.textContent = "Start date: " + new Date(ride.start_date).toLocaleDateString();
            div.appendChild(startDate);
            let endDate = document.createElement("p");
            endDate.textContent = "End date: " + new Date(ride.end_date).toLocaleDateString();
            div.appendChild(endDate);
            rideList.appendChild(div);
          }
        }
      });
  }
}
