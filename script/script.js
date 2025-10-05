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

  // Load map visualization (visualization.vg.json)
  loadVisualization("visualization/map.vg.json", "#map-chart", "vega");
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
