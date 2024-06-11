// Function to fetch data from the backend
function fetchBestSellingCards() {
    fetch('/get_best_selling')  // Assuming your backend route
      .then(response => response.json())
      .then(data => displayCards(data))
  }
  
  // Function to display the fetched card data
  function displayCards(cards) {
    // ... Logic to create card elements and insert them into the HTML ... 
  }
  
  // Call the function to fetch data initially
  fetchBestSellingCards();
  