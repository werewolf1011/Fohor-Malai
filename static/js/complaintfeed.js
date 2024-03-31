// Select all elements with class "complaint-row"
let statusRows = document.querySelectorAll(".complaint-row");

// Loop through each row
statusRows.forEach((row) => {
  // Access the status text content within this row
  let complaintStatus = row.querySelector(".status").textContent;
  console.log("hello");
  // Check the complaint status and add corresponding class
  if (complaintStatus === "completed") {
    row.classList.add("completed");
  } else if (complaintStatus === "in_progress") {
    row.classList.add("in_progress");
  } else {
    row.classList.add("pending");
  }
});
