import numpy as np
import matplotlib.pyplot as plt

# ================= USER PARAMETERS =================
# Parabola definition: y = a(x - h)^2 + k

a = -8.55286   # <-- parabola curvature (IMPORTANT)
h = 4.35625    # <-- horizontal shift
k = 78.45862   # <-- vertical shift

# Outlier sensitivity (lower = more aggressive)
residual_sigma_multiplier = 2.0
# ===================================================


def remove_outliers_parabola(x, y, a, h, k, sigma_mult=2.0):
    """
    Remove outliers based on distance from a known parabola:
        y = a(x - h)^2 + k

    Parameters:
        x, y (list or array): data points
        a, h, k (float): parabola parameters
        sigma_mult (float): sensitivity (lower = stricter)

    Returns:
        clean_x, clean_y, mask, residuals, threshold, y_expected
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y):
        raise ValueError("X and Y must be the same length")

    # Expected Y from parabola
    y_expected = a * (x - h) ** 2 + k

    # Residuals (vertical distance from curve)
    residuals = np.abs(y - y_expected)

    # Threshold based on residual spread
    sigma = np.std(residuals)
    threshold = sigma_mult * sigma

    mask = residuals <= threshold

    return (
        x[mask].tolist(),
        y[mask].tolist(),
        mask,
        residuals,
        threshold,
        y_expected,
    )


# ------------------ Example usage ------------------

x_data = [1.53, 1.59, 1.69, 1.87, 2.13, 2.2, 2.5, 2.53, 2.54, 2.56, 2.71, 2.71, 2.73, 2.73, 2.77, 2.79, 2.85, 2.85, 2.95, 3.01, 3.02, 3.02, 3.06, 3.09, 3.09, 3.1, 3.18, 3.24, 3.48, 3.5, 3.51, 3.55, 3.57, 3.72, 3.72, 3.72, 3.72, 3.73, 3.74, 3.75, 3.81, 3.82, 3.83, 3.85, 3.86, 3.86, 3.92, 4.03, 4.05, 4.07, 4.09, 4.12, 4.14, 4.14, 4.16, 4.17, 4.2, 4.21, 4.21, 4.22, 4.27, 4.32, 4.33, 4.34, 4.36, 4.37, 4.38, 4.38, 4.39, 4.41, 4.41, 4.59, 4.59, 4.65, 4.7, 4.74, 4.79, 4.84, 5.02, 5.2]

y_data = [15.3, 51.2, 16.9, 74.7, 9.8, 11.9, 54.4, 51.7, 4.2, 42.7, 57.9, 57.9, 54.5, 54.5, 49.2, 50.8, 52.7, 52.7, 53.7, 61.3, 53.9, 53.9, 50.8, 44.2, 44.2, 26.7, 61.7, 54.0, 98.1, 59.4, 75.0, 81.2, 51.1, 99.4, 99.4, 99.4, 99.4, 96.3, 64.9, 100.0, 72.0, 98.8, 99.0, 68.0, 99.9, 99.9, 88.5, 47.9, 91.5, 92.8, 78.8, 72.3, 53.2, 53.2, 91.2, 88.9, 81.0, 99.1, 99.1, 99.1, 47.8, 82.1, 76.9, 95.6, 65.5, 99.1, 93.4, 93.4, 68.4, 60.6, 60.6, 99.1, 99.1, 93.1, 82.7, 5.3, 57.7, 47.7, 56.7, 77.6]

(clean_x,clean_y, keep_mask, residuals, threshold, y_expected,) = remove_outliers_parabola(x_data, y_data, a, h, k, residual_sigma_multiplier)

# Prints the output first
print(f"Residual threshold: {threshold:.2f}")
print("Removed points:")
for i, keep in enumerate(keep_mask):
    if not keep:
        print(f"x={x_data[i]}, y={y_data[i]}, residual={residuals[i]:.2f}")

print("Kept points:")
print(f"x:{clean_x}")
print(f"y:{clean_y}")

# Plot
plt.figure()
plt.scatter(x_data, y_data, label="Original data")
plt.scatter(clean_x, clean_y, label="Kept points")
plt.plot(x_data, y_expected, label="Expected parabola")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Outlier Removal Using Known Parabola")
plt.show()
