import requests
import json

def fetch_data(url, headers, max_pages=10):
    all_data = []
    for page in range(1, max_pages + 1):
        response = requests.get(f"{url}&page={page}", headers=headers)
        if response.status_code == 200:
            data = response.json().get("data", [])
            all_data.extend(data)
        else:
            break
    return all_data

def save_to_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load_and_print_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    print(f"Số lượng dữ liệu trong tệp {filename}: {len(data)}")
    print(f"Dữ liệu mục đầu tiên: {data[0] if data else 'Không có dữ liệu'}")


url_1 = "https://tiki.vn/api/personalish/v1/blocks/listings?limit=10&sort=top_seller&urlKey=dien-thoai-may-tinh-bang&category=1789"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
category_data = fetch_data(url_1, headers)
save_to_json('category_data.json', category_data)
load_and_print_json('category_data.json')


category_urls = [
    "https://tiki.vn/api/personalish/v1/blocks/listings?limit=10&sort=top_seller&urlKey=dien-thoai-may-tinh-bang&category=1789",
    
]
all_categories_data = []
for url in category_urls:
    all_categories_data.extend(fetch_data(url, headers, max_pages=5))
    if len(all_categories_data) >= 3000:
        break

save_to_json('multiple_categories_data.json', all_categories_data)
load_and_print_json('multiple_categories_data.json')
