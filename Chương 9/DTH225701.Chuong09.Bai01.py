import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dữ liệu chiều cao (cm) và cân nặng (kg)
heights = np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]).reshape(-1, 1)
weights = np.array([49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# Tạo mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(heights, weights)

# Hàm để dự đoán cân nặng dựa vào chiều cao
def predict_weight(height):
    return model.predict(np.array([[height]]))[0]

# Lấy chiều cao từ người dùng và dự đoán cân nặng
user_height = float(input("Nhập chiều cao của bạn (cm): "))
predicted_weight = predict_weight(user_height)
print(f"Cân nặng dự đoán của bạn là: {predicted_weight:.2f} kg")

# Vẽ biểu đồ
plt.scatter(heights, weights, color='blue', label='Dữ liệu thực tế')
plt.plot(heights, model.predict(heights), color='red', label='Mô hình hồi quy')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Cân nặng (kg)')
plt.title('Hồi Quy Tuyến Tính - Dự Báo Cân Nặng Dựa Vào Chiều Cao')
plt.legend()
plt.show()