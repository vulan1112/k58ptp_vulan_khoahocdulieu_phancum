import pandas as pd

# Tên file Excel
file_path = "TỔNG HỢP ĐIỂM K58KTP.xlsx"

# Đọc file Excel
df = pd.read_excel(file_path, header=None)

# -----------------------------
# Vị trí dữ liệu
# -----------------------------
mssv_row = 1
name_row = 2
score_start_row = 4
score_start_col = 3

# Lấy MSSV
mssv_list = df.iloc[mssv_row, score_start_col:]

# Lấy tên sinh viên
name_list = df.iloc[name_row, score_start_col:]

# Lấy bảng điểm
score_df = df.iloc[score_start_row:, score_start_col:]

# Chuyển dữ liệu thành số
score_df = score_df.apply(pd.to_numeric, errors='coerce')

# Tính điểm trung bình
avg_scores = score_df.mean(axis=0, skipna=True)

# Tạo bảng kết quả
result = pd.DataFrame({
    "MSSV": mssv_list.values,
    "Tên Sinh Viên": name_list.values,
    "Điểm TB": avg_scores.values
})

# Hàm xếp nhóm
def classify(score):
    if 3.0 <= score <= 4.0:
        return "Nhóm 1"
    elif 2.5 <= score < 3.0:
        return "Nhóm 2"
    else:
        return "Nhóm 3"

# Thêm cột nhóm
result["Nhóm"] = result["Điểm TB"].apply(classify)

# Sắp xếp giảm dần
result = result.sort_values(by="Điểm TB", ascending=False)

# Xuất file kết quả
result.to_excel("ket_qua.xlsx", index=False)

print(result)

print("\nĐã tạo file ket_qua.xlsx")