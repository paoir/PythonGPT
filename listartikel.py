"""
Program ini dibuat dengan ChatGPT
Untuk menampilkan judul artikel yang terakhir/terbaru dipublish dalam sebuah halaman website berbasis Wordpress.
Yang ditampilkan adalah judul dan link url artikel. Jumlah page atau total artikel yang ditampikan disesuaikan dengan per_page yang diinginkan.
Hasilnya berupa list yang tidak tersimpan.
rioap.
"""

import requests

def get_wordpress_articles(site_url, per_page=10):
    """
    Get a list of articles from a WordPress site.

    Args:
    - site_url (str): The URL of the WordPress site.
    - per_page (int): Number of articles to retrieve per page.

    Returns:
    - list: A list of articles with their titles and URLs.
    """
    # Construct the API URL
    api_url = f"{site_url}/wp-json/wp/v2/posts?per_page={per_page}"
    
    # Make the request to the WordPress API
    response = requests.get(api_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        articles = response.json()
        
        # Create a list to store the article details
        article_list = []
        
        # Iterate through each article and extract the title and URL
        for article in articles:
            title = article.get('title', {}).get('rendered', 'No Title')
            link = article.get('link', 'No Link')
            article_list.append({'title': title, 'link': link})
        
        return article_list
    else:
        print(f"Failed to retrieve articles. Status code: {response.status_code}")
        return []

# Example usage
site_url = "https://namasite.co.id"
articles = get_wordpress_articles(site_url)

# Print the articles
if articles:
    for i, article in enumerate(articles, 1):
        print(f"{i}. {article['title']} - {article['link']}")
else:
    print("No articles found.")
