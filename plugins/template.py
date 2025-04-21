digital_business_table_report_html_email = """<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <style>
    body {{
      font-family: Arial, sans-serif;
      background-color: #f6f6f6;
      margin: 0;
      padding: 20px;
    }}

    .container {{
      max-width: 800px;
      margin: 0 auto;
      background-color: #ffffff;
      border-radius: 8px;
      padding: 20px;
      border: 1px solid #ddd;
    }}

    h2 {{
      color: #333333;
      border-bottom: 2px solid #ddd;
      padding-bottom: 5px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
      margin-bottom: 20px;
    }}

    th, td {{
      border: 1px solid #ddd;
      padding: 8px;
      text-align: left;
      font-size: 14px;
    }}

    th {{
      background-color: #f2f2f2;
      font-weight: bold;
    }}

    .highlight {{
      font-weight: bold;
      color: #007BFF;
    }}

    .negative {{
      color: #dc3545;
    }}

    .positive {{
      color: #28a745;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h2>Báo cáo Tình hình Sức khỏe Công ty - Ngày {report_date}</h2>
    <p><em>Các metrics được so sánh mức tăng giảm dựa trên giá trị trung bình của 7 ngày trước đó.</em></p>

    <!-- Section 1 -->
    <h3>I. Chỉ số Kinh Doanh</h3>
    <table>
      <tr>
        <th>Mục tiêu</th>
        <th>Total</th>
        <th>{report_date}</th>
        <th>% Biến động</th>
      </tr>
      {business_rows}
    </table>

    <!-- Section 2 -->
    <h3>II. Chỉ số User</h3>
    <table>
      <tr>
        <th>Chỉ số</th>
        <th>Total</th>
        <th>{report_date}</th>
        <th>% Biến động</th>
      </tr>
      {user_rows}
    </table>

    <!-- Section 3 -->
    <h3>III. Chỉ số Marketing</h3>
    <table>
      <tr>
        <th>Mục tiêu</th>
        <th>Total</th>
        <th>{report_date}</th>
        <th>% Biến động</th>
      </tr>
      {marketing_rows}
    </table>

    <p style="font-size: 13px; color: #888;"><a href="#">Xem chi tiết</a></p>
  </div>
</body>
</html>
"""