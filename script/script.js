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
});

// Utility function for drawing donut charts (for future use)
function drawDonutChart(canvasId, data, colors) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;

  const ctx = canvas.getContext("2d");
  const centerX = canvas.width / 2;
  const centerY = canvas.height / 2;
  const radius = Math.min(centerX, centerY) - 20;
  const innerRadius = radius * 0.6;

  let currentAngle = -Math.PI / 2;

  data.forEach((value, index) => {
    const sliceAngle = (value / 100) * 2 * Math.PI;

    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
    ctx.arc(
      centerX,
      centerY,
      innerRadius,
      currentAngle + sliceAngle,
      currentAngle,
      true
    );
    ctx.closePath();
    ctx.fillStyle = colors[index];
    ctx.fill();

    currentAngle += sliceAngle;
  });

  // Draw center circle
  ctx.beginPath();
  ctx.arc(centerX, centerY, innerRadius, 0, 2 * Math.PI);
  ctx.fillStyle = "white";
  ctx.fill();
}

// Color palette for charts
const chartColors = {
  primary: "#0f4c5c",
  secondary: "#16697a",
  tertiary: "#489fb5",
  accent: "#9bc53d",
};

// Export functions for use in future chart implementations
window.dashboardUtils = {
  drawDonutChart,
  chartColors,
};
