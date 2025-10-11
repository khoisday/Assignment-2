// Australian Travel & Transport Dashboard - JavaScript

// Filter button functionality
document.addEventListener("DOMContentLoaded", function () {
  const filterButtons = document.querySelectorAll(".filter-btn");

  filterButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Remove active class from all buttons
      filterButtons.forEach((btn) => btn.classList.remove("active"));

      // Add active class to clicked button
      this.classList.add("active");

      // Get selected region
      const selectedRegion = this.textContent;
      console.log("Selected region:", selectedRegion);

      // Future: Update charts based on selected region
      // updateDashboard(selectedRegion);
    });
  });

  // Load visualizations
  loadVisualizations();
});

// Function to load all visualizations
function loadVisualizations() {
  // Load pie chart (trans_pie.vl.json)
  loadVisualization(
    "visualization/trans_pie.vl.json",
    "#pie-chart",
    "vega-lite"
  );

  // Load line chart (line_chart.vl.json)
  loadVisualization(
    "visualization/line_chart.vl.json",
    "#line-chart",
    "vega-lite"
  );

  // Load map visualization (map.vl.json)
  loadVisualization("visualization/map.vl.json", "#map-chart", "vega-lite");

  // Load public transport by city chart (public-transport-by-city.vl.json)
  loadVisualization(
    "visualization/public-transport-by-city.vl.json",
    "#public-transport-chart",
    "vega-lite"
  );

  // Load inter-capital bar chart (inter-capital-bar.vl.json)
  loadVisualization(
    "visualization/inter-capital-bar.vl.json",
    "#inter-capital-chart",
    "vega-lite"
  );

  // Load heatmap visualization (heatmap.vl.json)
  loadVisualization(
    "visualization/heatmap.vl.json",
    "#heatmap-chart",
    "vega-lite"
  );
}

// Generic function to load a visualization
function loadVisualization(jsonFile, containerId, type) {
  fetch(jsonFile)
    .then((response) => response.json())
    .then((spec) => vegaEmbed(containerId, spec, { actions: false }));
}

// Export functions for use in future chart implementations
window.dashboardUtils = {
  loadVisualization,
};
