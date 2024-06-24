## Môn học: Thị Giác Máy Tính
**Giảng viên hướng dẫn: TS. Mai Tiến Dũng**


## Danh sách thành viên

| Họ và Tên             | MSSV     | Công việc                                                                                          | Mức độ hoàn thành |
|-----------------------|----------|-----------------------------------------------------------------------------------------------------|-------------------|
| Đặng Hữu Phát         | 22521065 | - Chuẩn bị nội dung, viết báo cáo.<br>- Chuẩn bị nội dung slide thuyết trình.<br>- Thực nghiệm với phương pháp 2.<br>- Thuyết trình nội dung phương pháp 2 và kết quả thực nghiệm. | 100%              |
| Nguyễn Hữu Hoàng Long | 22520817 | - Chuẩn bị nội dung viết báo cáo.<br>- Chuẩn bị slide thuyết trình.<br>- Thực nghiệm với phương pháp 1.<br>- Thuyết trình nội dung giới thiệu, phát biểu bài toán và phương pháp 1. | 100%              |

## Mô tả dự án
Repo này chứa code của môn học Thị Giác Máy Tính, được hướng dẫn bởi TS. Mai Tiến Dũng.

Chi tiết về đồ án, phương pháp thực hiện, kết quả thực nghiệm được trình bày ở báo cáo sau:
[Báo cáo chi tiết](https://drive.google.com/file/d/1K8qI2d9eEjHK_VCfo9tTQO7Vqg3S8gwQ/view)



## Hướng dẫn chạy dự án

1. Clone repository:
   ```bash
   git clone https://github.com/EbisuRyu/Traffic_Sign_Detection.git
   ```

### Phương pháp 1: Sử dụng đặc trưng HOG và mô hình phân loại SVM

- Quá trình chuẩn bị dữ liệu và huấn luyện mô hình được trình bày trong file `svm_training.ipynb`.
- Sử dụng mô hình phân loại SVM huấn luyện để detect biển báo được thực hiện trong file `svm_hog_detection.ipynb`.

### Phương pháp 2: Sử dụng mô hình Faster RCNN

- Quá trình huấn luyện và đánh giá mô hình Faster RCNN được trình bày chi tiết trong file `fasterRCNN.ipynb`.


