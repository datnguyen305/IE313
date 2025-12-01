import seaborn as sns
import matplotlib.pyplot as plt

def show(data, column_name):
    """
    Vẽ biểu đồ cột thể hiện số lượng/tần suất
    của các giá trị trong một cột.
    """
    plt.figure(figsize=(10, 6))

    # Vẽ biểu đồ đếm (Count Plot)
    # order=... dùng để sắp xếp cột theo thứ tự số lượng giảm dần
    sns.countplot(x=column_name, data=data, order=data[column_name].value_counts().index, palette='viridis')

    plt.title(f'Count Plot of {column_name}', fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()