import requests
import os
import json

SAVE_DIR = "solution/dataset/vietnam_traffic_signs"
os.makedirs(os.path.join(SAVE_DIR, "meta"), exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 Edg/141.0.0.0"
}

def fetch_html(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.status_code != 200:
            print(f"Error fetching {url}: {response.status_code}")
            return None
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_content_between_tags(html, start_tag, end_tag):
    start_index = html.find(start_tag)
    if start_index == -1:
        return None, len(html)
    end_index = html.find(end_tag, start_index)
    if end_index == -1:
        return None, len(html)
    return html[start_index:end_index], end_index + len(end_tag)

def get_text(html):
    text = ""

    in_tag = False

    for char in html:
        if char == ">":
            in_tag = True
        elif char == "<":
            in_tag = False
        elif in_tag:
            text += char

    return text

def download_sign_image(sign_image, sign_tag):
    response = requests.get(sign_image, headers=headers)
    response.raise_for_status()
    if response.status_code != 200:
        print(f"Error downloading {sign_image}: {response.status_code}")
        return
    
    with open(os.path.join(SAVE_DIR, "meta", f"{sign_tag}.png"), "wb") as f:
        f.write(response.content)

def crawl_vietnam_traffic_signs():
    url = "https://vi.wikipedia.org/wiki/Bi%E1%BB%83n_b%C3%A1o_giao_th%C3%B4ng_t%E1%BA%A1i_Vi%E1%BB%87t_Nam"

    html = fetch_html(url)
    if html is None:
        return

    sign_category_count = 0
    signs = []
    while True:
        content, next_index = get_content_between_tags(html, "<ul class=\"gallery mw-gallery-traditional\">", "</ul>")

        if content is None:
            break

        sign_category_count += 1
        if sign_category_count > 8:
            break
        
        html = html[next_index:]
        while True:
            sign_content, next_index = get_content_between_tags(content, "<li class=\"gallerybox\"", "</li>")

            if sign_content is None:
                break

            content = content[next_index:]
            sign_name = get_text(get_content_between_tags(sign_content, "<div class=\"gallerytext\">", "</div>")[0])
            sign_image = "https://" + get_content_between_tags(sign_content, "upload.wikimedia.org", "\"")[0]

            signs.append({
                "sign_name": sign_name,
                "sign_image": sign_image
            })

            if os.path.exists(os.path.join(SAVE_DIR, "meta", f"{sign_name.split(':')[0]}.png")):
                continue
            
            download_sign_image(sign_image, sign_name.split(":")[0])

            with open(os.path.join(SAVE_DIR, "classes.txt"), "a", encoding="utf-8") as f:
                f.write(sign_name.split(":")[0] + "\n")
    
    print(f"Crawled {len(signs)} Vietnam traffic signs")

if __name__ == "__main__":
    crawl_vietnam_traffic_signs()