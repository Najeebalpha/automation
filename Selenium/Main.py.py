from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.get("http://automationpractice.pl/index.php")

driver.implicitly_wait(20)

# Click the sign in button
signin_button = driver.find_element(By.LINK_TEXT, "Sign in")
signin_button.click()



username = driver.find_element(By.ID, "email")
username.send_keys("Najib@yopmail.com")
password = driver.find_element(By.ID, "passwd")
password.send_keys("EOi8bdHZ")
password.send_keys(Keys.RETURN)

driver.implicitly_wait(20)


Home = driver.find_element(By.XPATH, '//*[@id="header_logo"]/a/img')
Home.click()

# loading landing page
title = "My Store"
WebDriverWait(driver, 10).until(EC.title_contains(title))

best_seller = driver.find_element(By.XPATH, '//*[@id="home-page-tabs"]/li[2]/a')
best_seller.click()


# Collect product information
product1_name = driver.find_element(By.CSS_SELECTOR, ".product-container h5 a").text
product1_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[1]/div/div[2]/div[1]/span').text

product2_name = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[2]/div/div[2]/h5/a').text
product2_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[2]/div/div[2]/div[1]/span').text

product3_name = driver.find_element(By.XPATH,  '//*[@id="blockbestsellers"]/li[3]/div/div[2]/h5/a').text
product3_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[3]/div/div[2]/div[1]/span').text

product4_name = driver.find_element(By.XPATH,  '//*[@id="blockbestsellers"]/li[4]/div/div[2]/h5/a').text
product4_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[4]/div/div[2]/div[1]/span').text

product5_name = driver.find_element(By.XPATH,  '//*[@id="blockbestsellers"]/li[5]/div/div[2]/h5/a').text
product5_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[5]/div/div[2]/div[1]/span[1]').text

product6_name = driver.find_element(By.XPATH,  '//*[@id="blockbestsellers"]/li[6]/div/div[2]/h5/a').text
product6_price = driver.find_element(By.XPATH, '//*[@id="blockbestsellers"]/li[6]/div/div[2]/div[1]/span[1]').text

# Create a list of products as tuples
products = [(product1_name, product1_price),
            (product2_name, product2_price),
            (product3_name, product3_price),
            (product4_name, product4_price),
            (product5_name, product5_price),
            (product6_name, product6_price)]

# Sort the list of products by price
sorted_products = sorted(products, key=lambda x: float(x[1].strip("$")))

# Print the sorted list of products
for product in sorted_products:
    print(f"Product Name: {product[0]}")
    print(f"Product Price: {product[1]}")
    print()


scroll = driver.find_element(By.XPATH, '//*[@id="header_logo"]/a')
driver.execute_script("arguments[0].scrollIntoView(true);", scroll)


# driver.find_element(By.LINK_TEXT, "Women").click
driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[1]').click()
driver.find_element(By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="categories_block_left"]/div/ul/li[2]/a').click()
driver.find_element(By.ID, "layered_id_attribute_group_2").click()
driver.find_element(By.ID, "layered_id_attribute_group_24").click()
driver.find_element(By.XPATH, "//div[@id='layered_price_slider']/a[2]").click()
driver.find_element(By.XPATH, "//div[@id='center_column']/ul/li/div/div[2]/div[2]/a[2]/span").click()
driver.find_element(By.ID, "quantity_wanted").click()
driver.find_element(By.ID, "quantity_wanted").clear()
driver.find_element(By.ID, "quantity_wanted").send_keys("3")
driver.find_element(By.ID, "group_1").click()
driver.find_element(By.ID, "group_1").select_by_visible_text("M")
driver.find_element(By.XPATH, "//p[@id='add_to_cart']/button/span").click()
      
      
wait = WebDriverWait(driver, 10)
cart_page_loaded = wait.until(EC.presence_of_element_located((By.ID, "cart_title")))

# Getting the product details from the cart
product_name = driver.find_element(By.ID, "layer_cart_product_title").text
product_size_color = driver.find_element(By.ID, "layer_cart_product_attributes").text
product_quantity = driver.find_element(By.ID, "layer_cart_product_quantity").text
product_price = driver.find_element(By.ID, "layer_cart_product_price").text


# total cost and shipping cost from the cart
total_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_block_products_total").text
shipping_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_cart_shipping_cost").text
Final_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_block_cart_total").text


print("Product Name: {product_name}, Product Size and Color: {product_size_color}, Product Quantity: {product_quantity}, Product Price: {product_price}, Total Products Cost: {total_cost}, Shipping Cost: {shipping_cost}, Final Total Cost: {Final_cost}")




driver.quit()