from flask import Blueprint, render_template, request
from .scrape import scrape_img
from .scrape import scrape_rev

views_bp = Blueprint('views', __name__) #initialize blueprint

# Responsible for routing and connecting backend and frontend.
@views_bp.route('/') 
def home():
    return render_template('home.html')

@views_bp.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('product_url')
    if not url or ("www.lazada.com" not in url and "s.lazada.com.ph" not in url):
        error_msg = 'Enter a valid Lazada link.'
        return render_template('result.html', error_msg=error_msg)
    scraped_img = scrape_img(url)
    
    scraped_rev = scrape_rev(url)  
    
    # scraped_rev

    # If scrape_site returns product_detail_b64 and gallery_b64, render both
    if isinstance(scraped_img, dict) and ('product_detail_b64' in scraped_img or 'gallery_b64' in scraped_img):
        return render_template('result.html', product_detail_b64=scraped_img.get('product_detail_b64'), gallery_b64=scraped_img.get('gallery_b64'), product_url=url, scraped_rev=scraped_rev)
    else:
        error_msg = 'Failed to scrape the product details. Please check the URL or try again later.'
        return render_template('result.html', error_msg=error_msg, product_url=url, scraped_rev=scraped_rev)
