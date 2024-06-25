import requests
import csv

def get_wordpress_articles(site_url, per_page=10):
    """
    Get a list of articles from a WordPress site.

    Args:
    - site_url (str): The URL of the WordPress site.
    - per_page (int): Number of articles to retrieve per page.

    Returns:
    - list: A list of articles with their titles, URLs, and content.
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
        
        # Iterate through each article and extract the title, URL, and content
        for article in articles:
            title = article.get('title', {}).get('rendered', 'No Title')
            link = article.get('link', 'No Link')
            content = article.get('content', {}).get('rendered', 'No Content')
            article_list.append({'title': title, 'link': link, 'content': content})
        
        return article_list
    else:
        print(f"Failed to retrieve articles. Status code: {response.status_code}")
        return []

def save_articles_to_csv(articles, filename):
    """
    Save a list of articles to a CSV file.

    Args:
    - articles (list): A list of articles with their titles, URLs, and content.
    - filename (str): The name of the CSV file to save the articles.
    """
    # Define the CSV column names
    fieldnames = ['Title', 'URL', 'Content']
    
    # Write the articles to the CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            writer.writerow({'Title': article['title'], 'URL': article['link'], 'Content': article['content']})

# Example usage
site_url = "https://namasite.co.id"
articles = get_wordpress_articles(site_url, per_page=10)

# Save the articles to a CSV file
# buat namafile dengan akhiran .csv
if articles:
    save_articles_to_csv(articles, 'articles.csv')
    print("Articles have been saved to 'articles.csv'")
else:
    print("No articles found.")
